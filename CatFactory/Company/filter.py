from statistics import mean

from django_filters import FilterSet, AllValuesFilter, ChoiceFilter


class CustomCompanyFilter(FilterSet):
    """
    uses for filter views by param
    """

    # filter by city
    city = AllValuesFilter(
        field_name="contact_id__address_id__city", label="City"
    )

    # filter by country
    country = AllValuesFilter(
        field_name="contact_id__address_id__country", label="Country"
    )

    # filter by product_id
    product_id = AllValuesFilter(field_name="product_id", label="Product id")

    # filter for companies debet >  average debet
    avg_debet = ChoiceFilter(
        choices=(("true", "Companies that have debet more than avg debet all companiest"),),
        label="Companies that have debet more than avg debet all companies",
        method="filter_companies_by_avg_debet",
    )

    def filter_companies_by_avg_debet(self, queryset, name, value):
        get_average_debet = mean([company.debet for company in queryset])
        return queryset.filter(debet__gte=get_average_debet)
