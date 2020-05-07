from django.urls import path

from core.views import UserViewList

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('user/', UserViewList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)