"""Точка входа и цикл общения с пользователем."""

from commands import handle_command
from models import AppState


def main() -> None:
    """Запустить обработку команд и продолжать её до выхода."""
    # Представь диспетчера: он получает команду и передаёт её обработчику.
    # Создай AppState и выведи приветствие с упоминанием help и exit.
    # В цикле читай input("search> ") и вызывай handle_command со строкой и состоянием.
    # Если обработчик вернул False, заверши цикл.
    # ValueError и OSError покажи как «Ошибка: ...», затем продолжи ввод.
    # EOFError и KeyboardInterrupt должны спокойно завершать программу.
    # NotImplementedError не перехватывай: он указывает на незаполненную функцию.
    raise NotImplementedError


if __name__ == "__main__":
    main()
