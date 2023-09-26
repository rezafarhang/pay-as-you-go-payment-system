from rest_framework import serializers
from .models import Price


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ['unit_price', 'service_name', 'created_at']
    

class TotalCostSerializer(serializers.Serializer):
    total_request_cost = serializers.DecimalField(max_digits=10 ,decimal_places=4)
    total_request_count = serializers.IntegerField()



    



