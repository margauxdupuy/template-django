from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from app.views import TemplateDjangoView

app_name = 'app'

router = DefaultRouter()


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'hello', TemplateDjangoView.as_view(), name='hello'),
]
