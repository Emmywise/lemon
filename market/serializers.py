
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    side = serializers.CharField(max_length=4)
    isin = serializers.CharField(max_length=12) 

    class Meta:
        fields = '__all__'
        model = Order

    def validate_side(self, val):
        is_valid = val.lower() in ['sell', 'buy']
        if not is_valid:
           raise serializers.ValidationError(f'{val} is not a valid choice')
        return val.lower()

    def validate_isin(self, value):
        is_valid = len(value) == 12
        if not is_valid:
             raise serializers.ValidationError('word length must be equal to 12')
        if Order.objects.filter(isin=value):
            raise serializers.ValidationError('isin already in system')
        return value