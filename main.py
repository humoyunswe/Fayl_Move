import logging
from pathlib import Path

import argparse
def fayl_move(old_path, new_path, all_files=False, file_format=None):
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    file = logging.FileHandler('fayl_move.log')
    file.setFormatter(formatter)
    logger.addHandler(file)

    old_path = Path(old_path)
    new_path = Path(new_path)

    if not old_path.exists() or not old_path.is_dir():
        logger.error("Исходная папка не существует или не является директорией!")
        return

    for item in old_path.glob('*'):
        if not all_files and not item.is_file():
            continue

        if all_files or (item.is_file() and item.suffix == f".{file_format}"):
            new_file = new_path / item.name
            item.rename(new_file)

            logger.info(f'Переименовано: {item} -> {new_file}')
    logger.info("Готово!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Fayl Move",description="Это программу изменяет директории файлов")
    parser.add_argument('-all', action='store_true', help="Переименовывает все файлы включая папки.")
    parser.add_argument('--format', type=str, help="Переименовывает только файлы с указанным файлaм.")
    parser.add_argument('old_path', type=str, help="Путь до исходной папки.")
    parser.add_argument('new_path', type=str, help="Путь до новой папки.")
    args = parser.parse_args()
    # fayl_move(args.old_path, args.new_path, args.all, args.format)

