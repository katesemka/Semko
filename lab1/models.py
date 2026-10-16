"""Классы-контейнеры: хранят данные, а действия выполняют функции других модулей.

@dataclass сам создаёт конструктор по перечисленным полям.
field(default_factory=...) создаёт отдельную коллекцию для каждого объекта.
"""

from dataclasses import dataclass, field

from config import DEFAULT_THRESHOLD


@dataclass
class Earthquake:
    """Карточка одного землетрясения с полями исходного JSON-объекта.

    id нужен для связи записи с оценкой, title — заголовок карточки.
    None означает отсутствие значения. Исходные строки сохраняются без очистки.
    Этот класс ничего не загружает и не ищет: он хранит одну запись.
    """

    id: str
    title: str
    kind: str | None = None
    network: str | None = None
    time: str | None = None
    magnitude: float | None = None
    depth_km: float | None = None
    latitude: float | None = None
    longitude: float | None = None
    reviewed: bool | None = None
    url: str | None = None


@dataclass
class Filter:
    """Одно условие фильтрации — как одно сито для записей каталога.

    field_name — поле, operator — сравнение, value — значение нужного типа.
    Filter("magnitude", "ge", 4.0) означает «магнитуда не меньше четырёх».
    Саму проверку выполняет filters.py.
    """

    field_name: str
    operator: str
    value: str | float | bool


@dataclass
class SearchResult:
    """Запись вместе с результатами её проверки по конкретному запросу.

    record — карточка, relevance — соответствие запросу, rating — оценка или None.
    Рейтинг stars выводится пользователю, но не меняет порядок результатов.
    """

    record: Earthquake
    relevance: float
    rating: int | None = None


@dataclass
class AppState:
    """Память текущего запуска — общий рабочий блокнот приложения.

    loaded отличает пустой загруженный каталог от отсутствия загрузки.
    records хранит каталог, filters и threshold — настройки следующего поиска.
    ratings связывает ID с оценками, которые сохраняются между запросами.
    last_ids содержит ID последней показанной выдачи для проверки команды rate.
    last_output хранит готовый текст для save; None означает отсутствие выдачи.
    """

    loaded: bool = False
    records: list[Earthquake] = field(default_factory=list)
    filters: list[Filter] = field(default_factory=list)
    threshold: float = DEFAULT_THRESHOLD
    ratings: dict[str, int] = field(default_factory=dict)
    last_ids: set[str] = field(default_factory=set)
    last_output: str | None = None
