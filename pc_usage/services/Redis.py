"""Модуль управления базой Redis."""
from dataclasses import dataclass
from datetime import datetime

import redis
from redis.commands.json.path import Path


@dataclass
class RedisDriver:
    """Класс для выолнения операция с базой Redis."""

    host: str = 'localhost'
    port: int = 6379

    redis_db = None

    def connect_db(self):
        """Подключение к базе Redis."""
        self.redis_db = redis.Redis(host=self.host, port=self.port)

    def get_all_data_from_redis(self) -> dict:
        """Запрос всех данных из Redis."""
        keys = self.redis_db.scan_iter()
        redis_data = {}
        for key in keys:
            key_string = key.decode("utf-8")
            value_string = self.redis_db.json().get(key_string)
            redis_data[key_string] = value_string
        return redis_data

    def set_data_to_redis(self, key: str, value: dict) -> None:
        """Закгрузка json в Redis."""
        self.redis_db.json().set(key, Path.root_path(), value)

    def del_data_from_redis(self, start_date: str, stop_date: str) -> dict:
        """Удаление данных Redis."""
        keys = self.redis_db.scan_iter()

        # Проверка на не пустые значение start_date и stop_date
        if (start_date is None) or (stop_date is None):
            delete_status = True
            start_date_v = None
            stop_date_v = None
        else:
            delete_status = False

            # Проверка на корректность внесеных дат
            try:
                start_date_v = datetime.strptime(start_date, '%m:%d:%H:%M:%S')
                stop_date_v = datetime.strptime(stop_date, '%m:%d:%H:%M:%S')
            except ValueError:
                return {'Error': 'Bad format stop_date and start_date'}

            # Проверка на правильный порядок внесеных дат
            if stop_date < start_date:
                return {'Error': 'Bad sequence stop_date and start_date'}

        for key in keys:
            key_string = key.decode("utf-8")
            key_to_date = datetime.strptime(key_string, '%m:%d:%H:%M:%S')
            if delete_status:
                self.redis_db.json().delete(key_string)
            else:
                if start_date_v <= key_to_date <= stop_date_v:
                    self.redis_db.json().delete(key_string)

        return {'Status': 'Data deleted'}
