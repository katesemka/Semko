"""Формирование строк: печать выполняют обработчики команд, а не этот модуль."""

from config import FIELD_TYPES, FILTER_OPERATORS, SEARCH_FIELDS
from models import Earthquake, Filter, SearchResult


def format_record(
    record: Earthquake,
    relevance: float | None = None,
    rating: int | None = None,
) -> str:
    """Подготовить полную карточку и, для поиска, релевантность и оценку."""
    # Как оформление карточки: в заголовке ID и title, ниже остальные поля FIELD_TYPES.
    # Пустые значения обозначь «—»; логические значения можно показать как true и false.
    # Если relevance is not None, добавь релевантность и оценку 4/5 либо «нет».
    # Для show relevance равна None: дополнительные поисковые строки не нужны.
    # plain — обычный текст без подсветки, stars — оценка без итоговых баллов boost.
    raise NotImplementedError


def format_records(records: list[Earthquake]) -> str:
    """Собрать текст show со всеми загруженными записями."""
    # Покажи общее число записей, затем вызови format_record для каждой карточки.
    # Между карточками оставь пустые строки; не применяй фильтры и ограничение top10.
    raise NotImplementedError


def format_search_results(
    results: list[SearchResult],
    found_count: int,
    elapsed_ms: float,
) -> str:
    """Собрать выдачу поиска с количествами, карточками и временем."""
    # «Найдено» возьми из found_count, «Показано» — из длины results.
    # Для карточек вызови format_record с relevance и rating каждого результата.
    # Добавь время в миллисекундах; дробные числа удобно округлить до двух знаков.
    # При пустой выдаче тоже покажи количества и время, не возвращай прежние карточки.
    # Верни единую строку для экрана и сохранения в last_output.
    raise NotImplementedError


def format_fields() -> str:
    """Подготовить справку о полях, типах и разрешённых операторах."""
    # Используй SEARCH_FIELDS, FIELD_TYPES и FILTER_OPERATORS из config.
    # Перечисли поля поиска и собери таблицу типов и операторов фильтрации.
    # Поясни обозначения сравнений и логические значения true и false.
    raise NotImplementedError


def format_filters(conditions: list[Filter]) -> str:
    """Подготовить нумерованный список активных фильтров."""
    # Если список пуст, верни «Фильтров нет».
    # Иначе перечисли условия через enumerate с началом 1: поле, оператор, значение.
    # Номера вычисляй по текущему списку: после удаления пропусков быть не должно.
    raise NotImplementedError


def format_ratings(ratings: dict[str, int]) -> str:
    """Подготовить список всех сохранённых пользовательских оценок."""
    # Если оценок нет, верни «Оценок нет».
    # Иначе собери строки вида «ID: 4/5» по всем парам словаря.
    # Не ограничивай оценки текущей выдачей: они сохраняются при смене запроса.
    raise NotImplementedError
