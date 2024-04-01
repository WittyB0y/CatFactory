from datetime import datetime
from rest_framework import serializers
from Product.models import Product


class ProductObjectsSerializer(serializers.ModelSerializer):
    """
    Validate data, it doesn't have length is more 25 chars.
    And check date publish product.
    """
    name = serializers.CharField(max_length=25)

    def validate_date(self, date):
        if date > datetime.now().date():
            raise serializers.ValidationError(
                "Incorrect date."
            )
        return date

    class Meta:
        model = Product
        fields = '__all__'
