from rest_framework import serializers

from Company.models import Company


class CompanyObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('debet',)
