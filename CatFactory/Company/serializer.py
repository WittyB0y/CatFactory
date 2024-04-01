from rest_framework import serializers

from Company.models import Company


class CompanyObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('debet',)  # Allow only read this field.


class GenerateQRCodeAndSendEmailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
