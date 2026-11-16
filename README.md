# Парсер книг с Books to Scrape

Домашка 3 по Python. Скрипт обходит все 50 страниц каталога http://books.toscrape.com и собирает данные по каждой из 1000 книг: название, цену, рейтинг, наличие, описание и таблицу Product Information. Результат можно сохранить в `artifacts/books_data.txt`, одна книга на строку.

## Что где лежит

```
dz3/
├── artifacts/                       сюда пишется books_data.txt
├── notebooks/
│   └── HW_03_python_ds_2025.ipynb   ноутбук с заданиями и выводами
├── tests/
│   └── test_scraper.py              тесты на pytest
├── scraper.py                       функции get_book_data и scrape_books
├── conftest.py                      пустой, нужен чтобы pytest видел scraper.py
├── requirements.txt
└── README.md
```

## Библиотеки

- `requests` скачивает страницы сайта
- `beautifulsoup4` достаёт нужные теги из HTML
- `schedule` запускает сбор каждый день в заданное время (используется в ноутбуке, задание 3)
- `pytest` для тестов

Полный список с версиями в `requirements.txt`. Проект делался на Python 3.9.

## Как запустить

Создать виртуальное окружение и поставить зависимости:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Собрать все книги и сохранить в файл (из корня проекта):

```bash
python -c "from scraper import scrape_books; scrape_books(is_save=True)"
```

Сбор идёт пару минут, потому что на каждую книгу отдельный запрос. Потом появится `artifacts/books_data.txt`.

Сбор по расписанию сделан в ноутбуке, в ячейке задания 3. Там бесконечный цикл, остановить его можно кнопкой Stop / Interrupt.

## Тесты

Из корня проекта:

```bash
pytest
```

Тесты ходят на настоящий сайт, так что без интернета упадут. Проверяется, что `get_book_data` возвращает словарь с нужными ключами, а у книги A Light in the Attic правильные название, цена £51.77 и рейтинг Three.
