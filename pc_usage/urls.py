"""Url для приложения pc_usage."""
from django.urls import path

from .views import (delete_redis_data,
                    get_redis_data,
                    index,
                    usage_all,
                    usage_detail)


urlpatterns = [
    path('', index),
    path('usage_all/', usage_all, name='usage_all'),
    path('usage_detail/', usage_detail, name='usage_detail'),
    path('get_redis_data/', get_redis_data, name='get_redis_data'),
    path('delete_redis_data/', delete_redis_data, name='delete_redis_data'),
]
