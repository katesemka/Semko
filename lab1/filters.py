"""Создание условий и проверка записей по всем активным фильтрам."""

from config import FIELD_TYPES, FILTER_OPERATORS
from models import Earthquake, Filter


def convert_filter_value(field_name: str, raw_value: str) -> str | float | bool:
    """Привести аргумент команды к типу выбранного поля."""
    # Посмотри тип в FIELD_TYPES: строку оставь как есть, число преобразуй в float.
    # Для bool разреши только true и false и явно сопоставь им True и False.
    # Не используй bool(raw_value): любая непустая строка превратится в True.
    # Если значение неверно, подними ValueError с полем и ожидаемым типом.
    raise NotImplementedError


def parse_filter(field_name: str, operator: str, raw_value: str) -> Filter:
    """Проверить поле, оператор, значение и собрать условие Filter."""
    # Сначала проверь наличие поля в FIELD_TYPES.
    # По его типу найди допустимые операторы в FILTER_OPERATORS.
    # contains допустим для строки, но не для числового или логического поля.
    # Преобразуй значение через convert_filter_value и верни Filter.
    # В состояние условие добавит обработчик команды после успешной проверки.
    raise NotImplementedError


def matches_filter(record: Earthquake, condition: Filter) -> bool:
    """Проверить одну карточку по одному условию."""
    # Получи атрибут карточки по condition.field_name, например через getattr.
    # None и пустая строка не проходят никакое условие, даже ne.
    # Проверяй пустоту явно: число 0 и логическое False являются заполненными значениями.
    # Выбери сравнение по operator и сравни значение с condition.value.
    # Не меняй регистр строк перед сравнением.
    raise NotImplementedError


def matches_filters(record: Earthquake, conditions: list[Filter]) -> bool:
    """Проверить, что карточка проходит каждое активное условие."""
    # Несколько сит стоят подряд: достаточно не пройти одно, чтобы запись исключили.
    # Вызови matches_filter для каждого условия и объедини ответы логическим «И».
    # Подходит all(); при пустом списке условий запись проходит.
    raise NotImplementedError
