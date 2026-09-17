from datetime import time
import main


def test_get_distance():
    assert int(main.get_distance(1505) * 100_000) == 97825


def test_get_spent_calories():
    assert (
        int(main.get_spent_calories(0.97825, time(hour=9, minute=36))) == 1512
    )


def test_get_achievement():
    assert main.get_achievement(7) == 'Отличный результат! Цель достигнута.'
