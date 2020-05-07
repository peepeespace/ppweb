from rest_framework import serializers
from quant.models import Ticker, MonitorStock, MinOHLCV

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = '__all__'

class MonitorStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorStock
        fields = '__all__'

class MinOHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinOHLCV
        fields = '__all__'