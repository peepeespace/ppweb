from rest_framework import serializers
from quant.models import (
    Ticker,
    StockInfo,
    Index,
    ETF,
    OHLCV,
    BuySell,
    MarketCapital,
    Factor,
    MonitorStock,
    MinOHLCV,
    UserState,
    PortHistory,
)

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = '__all__'

class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'

class ETFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETF
        fields = '__all__'

class OHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = OHLCV
        fields = '__all__'

class BuySellSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuySell
        fields = '__all__'

class MarketCapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketCapital
        fields = '__all__'

class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = '__all__'

class MonitorStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorStock
        fields = '__all__'

class MinOHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinOHLCV
        fields = '__all__'

class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserState
        fields = '__all__'

class PortHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortHistory
        fields = '__all__'