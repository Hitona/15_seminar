import os
from collections import namedtuple
import logging
import argparse

# Определение структуры данных для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

# Настройка логирования
logging.basicConfig(filename='15_log.log',
                    level=logging.INFO,
                    filemode='a+',
                    encoding='utf-8')


def scan_directory(path):
    """Функция для сканирования директории и логирования информации о содержимом."""
    for root, dirs, files in os.walk(path):
        # Обработка каталогов
        for directory in dirs:
            info = FileInfo(name=directory,
                            extension=None,
                            is_directory=True,
                            parent_directory=os.path.basename(root))
            logging.info(info)

        # Обработка файлов
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            info = FileInfo(name=file_name,
                            extension=file_extension,
                            is_directory=False,
                            parent_directory=os.path.basename(root))
            logging.info(info)


def main():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Сканирование директории и логирования информации о содержимом.')
    parser.add_argument('path',
                        type=str,
                        nargs='?',
                        default='C:/Users/Admin/Desktop/GB/15_sem',
                        help='Путь до директории для сканирования')

    # Разбор аргументов
    args = parser.parse_args()

    # Проверка существования директории
    if not os.path.isdir(args.path):
        print("Указанный путь не является директорией.")
        return

    # Запуск сканирования директории
    scan_directory(args.path)


if __name__ == '__main__':
    main()
