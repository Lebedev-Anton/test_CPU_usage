"""Views для приложения pc_usage."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from pc_usage.services.Redis import RedisDriver
from pc_usage.services.Timer import count_request_time
from pc_usage.services.UsageManager import get_pc_usage, get_pc_usage_detail

from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request: HttpRequest) -> HttpResponse:
    """View с информацие об типах запросов."""
    return render(request, 'index.html')


@api_view(['GET'])
@count_request_time
def usage_all(request: HttpRequest) -> Response:
    """Запрос всех видов загрузки."""
    return Response(get_pc_usage())


@api_view(['POST'])
@count_request_time
def usage_detail(request: HttpRequest) -> Response:
    """Запрос определенного вида загрузки."""
    usage_type = request.POST.get('usage_type')
    return Response(get_pc_usage_detail(usage_type))


@api_view(['GET'])
@count_request_time
def get_redis_data(request: HttpRequest) -> Response:
    """Запрос данных из Redis."""
    redis = RedisDriver()
    redis.connect_db()
    return Response(redis.get_all_data_from_redis())


@api_view(['POST'])
@count_request_time
def delete_redis_data(request: HttpRequest) -> Response:
    """Запрос на удаление данных из Redis."""
    start_date = request.POST.get('start_date')
    stop_date = request.POST.get('stop_date')
    redis = RedisDriver()
    redis.connect_db()
    return Response(redis.del_data_from_redis(start_date, stop_date))
