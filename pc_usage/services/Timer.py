"""Модуль для сохранения времени запроса."""
from datetime import datetime

from pc_usage.services.Redis import RedisDriver


def count_request_time(func):
    """Декоратор для view."""

    def wrapper(*args, **kwargs):
        request_time = datetime.now()
        key = request_time.strftime('%m:%d:%H:%M:%S')
        redis_value = {}
        request = args[0]
        method = request.method
        redis_value['method'] = method
        if method == 'POST':
            data = request.POST.dict()
            redis_value['data'] = data
        res = func(*args, **kwargs)
        redis = RedisDriver()
        redis.connect_db()
        redis.set_data_to_redis(key, redis_value)
        return res

    return wrapper
