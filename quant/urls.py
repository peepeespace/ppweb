from django.urls import path

from quant.views import (
    index,
    detail,
    TickerList,
    TickerDetail,
    MonitorStockList,
    MinOHLCVList,
)


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('ticker/', TickerList.as_view()),
    path('ticker/<int:pk>/', TickerDetail.as_view()),
    path('monitorstock/', MonitorStockList.as_view()),
    path('minohlcv/', MinOHLCVList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)