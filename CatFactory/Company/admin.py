from django.contrib import admin
from Company.models import Company
from django.utils.html import format_html
from Celery_tasks.tasks import async_clear_debet


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level_company",
        "debet",
        "date_created",
        "provider_link",
        "company_city",
        "copy_email_button",
    )
    list_filter = (
        "contact_id__address_id__city",
    )

    actions = (
        "clear_debet",
    )

    def company_city(self, obj):
        city = obj.contact_id.address_id.city
        if city:
            return city
        return "No city"

    def provider_link(self, obj):
        """
        to get a link to the provider
        """
        if obj.provider:
            return format_html('<a href="{}">{}</a>', obj.provider.id, obj.provider.name)
        return "Doesn't have provider"

    def copy_email_button(self, obj):
        return format_html(
            '<button type="button" class="email-btn" email="{}">Copy Email</button>',
            obj.contact_id.email_id
        )

    @admin.action(description="Clear debit")
    def clear_debet(self, request, queryset):
        """this action clears the debit (all selected items), if the length > 30, the async function is called"""
        count_element = queryset.count()
        if count_element > 20:
            for object_comp in queryset:
                async_clear_debet.delay(object_comp.id)
            self.message_user(request, f"Started async clearing debet for {count_element} companies.")
        else:
            queryset.update(debet=0)
            self.message_user(request, f"Cleared debet for {count_element} companies.")

    company_city.short_description = "City"
    provider_link.short_description = "Provider"

    class Media:
        js = ('js/copy_email_btn.js',)
        css = {
            'all': ('css/copy_email_btn.css',)
        }
