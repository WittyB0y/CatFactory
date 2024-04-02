from django.contrib.auth.models import User
from rest_framework import serializers
from Contact.models import Contact, Email, Address
from Company.models import Company
from Product.models import Product


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    address_id = AddressSerializer()
    email_id = EmailSerializer()

    def create(self, validated_data):
        address_data = validated_data.pop('address_id')
        email_data = validated_data.pop('email_id')

        address = Address.objects.create(**address_data)
        email = Email.objects.create(**email_data)

        contact = Contact.objects.create(address_id=address, email_id=email, **validated_data)
        return contact

    class Meta:
        model = Contact
        fields = '__all__'


class CompanyObjectsSerializer(serializers.ModelSerializer):
    contact_id = ContactSerializer()
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    staff_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    debet = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, default=0)
    # Can set value when create new Company, but can't update through API.

    def create(self, validated_data):
        contact_data = validated_data.pop('contact_id')
        products_data = validated_data.pop('product_id')
        staff_data = validated_data.pop('staff_id')

        contact = ContactSerializer().create(contact_data)
        company = Company.objects.create(contact_id=contact, **validated_data)

        company.product_id.set(products_data)
        company.staff_id.set(staff_data)
        return company

    class Meta:
        model = Company
        fields = '__all__'


class GenerateQRCodeAndSendEmailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
