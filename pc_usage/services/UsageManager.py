"""Модуль для отслеживания загружености ПК."""

import enum

import psutil


def get_pc_usage() -> dict:
    """Запрос загружености ПК."""
    return {
        'CPU_usage': psutil.cpu_percent(1),
        'RAM_usage': psutil.virtual_memory()[2]
    }


class UsageTypeEnum(enum.Enum):
    """Enum с допустимыми типами загрузки."""

    RAM = 'RAM'
    CPU = 'CPU'


def get_pc_usage_detail(usage_type: str) -> dict:
    """Запрос загружености ПК по типу."""
    if usage_type == UsageTypeEnum.CPU.value:
        usage_detail = {'CPU_usage': psutil.cpu_percent(1)}
    elif usage_type == UsageTypeEnum.RAM.value:
        usage_detail = {'RAM_usage': psutil.virtual_memory()[2]}
    else:
        usage_detail = {'Error': 'Not allowed usage type'}
    return usage_detail
