import datetime


def test_exists_annotations():
    from main import __annotations__ as actual_annotations

    assert "storage_data" in actual_annotations, (
        "Убедитесь, что исправлена предупреждение от статического типизатора "
        "`mypy`, в модуле `main.py` для глобальной переменной `storage_data`."
    )

    actual_type_hint = actual_annotations["storage_data"]
    expected_type_hint = dict[datetime.time, int]
    assert actual_type_hint == expected_type_hint, (
        "Убедитесь, что в модуле `main.py` для глобальной переменной "
        "`storage_data` установлена верная аннотация типов."
    )
