import random
import smtplib
from decimal import Decimal
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
from django.db.models import F
from CatFactory import settings
from Company.models import Company
from CatFactory.celery import celery
import qrcode


@celery.task(bind=True)
def async_clear_debet(self, company_id):
    company = Company.objects.get(id=company_id)
    company.debet = 0
    company.save()


@celery.task
def increasing_debet():
    """
    Task to increase the debt for each company by a random amount between 5 and 500.
    """
    # Generate random increase sums for each company
    random_increase_sums = {
        comp.id: Decimal(random.randint(5, 500)) for comp in Company.objects.all()
    }
    # Update the debt for each company with the calculated increase sum
    for comp_id, random_increase_sum in random_increase_sums.items():
        Company.objects.filter(id=comp_id).update(debet=F('debet') + random_increase_sum)


@celery.task
def decreasing_debet():
    """
    Task to decrease the debt for each company by a random amount between 100 and 10000.
    If the resulting debt is negative, it is set to 0.
    """
    for comp in Company.objects.all():
        random_decrease_sum = Decimal(random.randint(100, 10000))
        new_debet_sum = comp.debet - random_decrease_sum
        if new_debet_sum < 0:
            comp.debet = 0
        else:
            comp.debet = new_debet_sum
        comp.save()


@celery.task
def send_qr_code_to_email(company_id, user_email):
    company = Company.objects.get(pk=company_id)
    email = company.contact_id.email_id.email
    data_for_qr_code = f"Name: {company.name}\nAddress: {company.contact_id.address_id}\nEmail: {email}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data_for_qr_code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)

    from_email = settings.EMAIL_USER
    to_email = user_email

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
    msg = MIMEMultipart()

    message = "QR code contains contact information.\n" + data_for_qr_code
    msg.attach(MIMEText(message, "plain"))
    image = MIMEImage(img_byte_array.read(), name="qr.png", content_type="image/png")
    msg.attach(image)

    msg["Subject"] = f"CatFactory: Contact information about {company.name}"
    msg["From"] = from_email
    msg["To"] = to_email

    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
