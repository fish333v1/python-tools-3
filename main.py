"""Модуль подсчёта калорий."""

import datetime as dt
from typing import Optional, Union, cast

FORMAT: str = "%H:%M:%S"
WEIGHT: int = 75  # Вес
HEIGHT: int = 175  # Рост
K_1: float = 0.035  # Коэффициент для подсчета калорий
K_2: float = 0.029  # Коэффициент для подсчета калорий
STEP_M: float = 0.65  # Длина шага в метрах

storage_data: dict[dt.time, int] = {}


def check_correct_data(data: tuple[Optional[str], int]) -> bool:
    """Проверка корректности полученного пакета."""
    length: int = len(data)
    if length != 2 or None in data:
        return False
    return True


def check_correct_time(time: dt.time) -> bool:
    """Проверка корректности параметра времени."""
    if storage_data and time <= max(storage_data):
        return False
    return True


def get_step_day(steps: int) -> int:
    """Получить количество пройденных шагов за день."""
    day_steps: int = sum(value for value in storage_data.values())
    return day_steps + steps


def get_distance(steps: int) -> float:
    """Получить дистанцию пройденного пути в км."""
    return steps * STEP_M / 1000


def get_spent_calories(dist: float, current_time: dt.time) -> float:
    """Получить значения потраченных калорий."""
    time: float = current_time.hour + current_time.minute / 60
    mean_speed: float = dist / time
    return (
        (K_1 * WEIGHT + (mean_speed ** 2 // HEIGHT) * K_2 * WEIGHT)
        * time * 60
    )


def get_achievement(dist: float) -> str:
    """Получить поздравления за пройденную дистанцию."""
    if dist < 2:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'
    if dist < 3.9:
        return 'Маловато, но завтра наверстаем!'
    if dist < 6.5:
        return 'Неплохо! День был продуктивным.'
    return 'Отличный результат! Цель достигнута.'


def show_message(
    time: dt.time,
    steps: int,
    dist: float,
    calories: float,
    achiev: str
) -> None:
    """Вывести на экран результаты вычислений."""
    print(
        f'''
        Время: {time}.
        Количество шагов за сегодня: {steps}.
        Дистанция составила {dist:.2f} км.
        Вы сожгли {calories:.2f} ккал.
        {achiev}
        '''
    )


def accept_package(
    data: tuple[Optional[str], int]
) -> Union[dict[dt.time, int], str]:
    """Обработать пакет данных."""
    if not check_correct_data(data):
        return 'Некорректный пакет'
    time, steps = data
    time = cast(str, time)
    pack_time: dt.time = dt.datetime.strptime(time, FORMAT).time()
    if not check_correct_time(pack_time):
        return 'Некорректное значение времени'
    day_steps: int = get_step_day(steps)
    dist: float = get_distance(day_steps)
    spent_calories: float = get_spent_calories(dist, pack_time)
    achievement: str = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = steps
    return storage_data


if __name__ == '__main__':
    # Пример запуска
    package_0: tuple[str, int] = ('2:00:01', 505)
    package_1: tuple[None, int] = (None, 3211)
    package_2: tuple[str, int] = ('9:36:02', 15000)
    package_3: tuple[str, int] = ('9:36:02', 9000)
    package_4: tuple[str, int] = ('8:01:02', 7600)

    accept_package(package_0)
    accept_package(package_1)
    accept_package(package_2)
    accept_package(package_3)
    accept_package(package_4)
