from django.urls import path

from quant.views import index, detail, TickerList, TickerDetail

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('ticker/', TickerList.as_view()),
    path('ticker/<int:pk>/', TickerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)