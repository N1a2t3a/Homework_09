# Homework_09

Це домашнє завдання передбачає створення програми для веб-скрапінгу та збереження отриманих даних. У цьому завданні ми використовуємо бібліотеку BeautifulSoup для збору цитат зі сторінки http://quotes.toscrape.com і збереження їх у форматі JSON.

## Вимоги

1. Запустіть `pip install beautifulsoup4 requests` для встановлення необхідних бібліотек.

2. Запустіть скрипт `scrape_quotes.py` для виконання веб-скрапінгу та створення файлу `quotes.json`, в якому збережені всі зібрані цитати.

3. Переконайтеся, що у вас вже є файл моделі для збереження даних в базі даних MongoDB.

4. Запустіть скрипт `load_quotes_to_db.py` для завантаження цитат з файлу `quotes.json` у вашу базу даних MongoDB.

5. Запустіть скрипт `load_authors_to_db.py` для завантаження інформації про авторів з файлу `authors.json` у вашу базу даних MongoDB.

## Структура `authors.json`

`authors.json` - це файл, який містить інформацію про авторів цитат. Приклад структури:

[
    {
        "fullname": "Albert Einstein",
        "born_date": "March 14, 1879",
        "born_location": "in Ulm, Germany",
        "description": "In 1879, Albert Einstein was born in Ulm, Germany..."
    },
    {
        "fullname": "J.K. Rowling",
        "born_date": "July 31, 1965",
        "born_location": "in Yate, Gloucestershire, England",
        "description": "J.K. Rowling is the author of the much-loved series of seven Harry Potter novels..."
    },
    {
        "fullname": "Jane Austen",
        "born_date": "December 16, 1775",
        "born_location": "in Steventon, Hampshire, England",
        "description": "Jane Austen was an English novelist known primarily for her six major novels..."
    },
    {
        "fullname": "Marilyn Monroe",
        "born_date": "June 1, 1926",
        "born_location": "in Los Angeles, California, The United States",
        "description": "Marilyn Monroe was an American actress, model, and singer..."
    },
    {
        "fullname": "André Gide",
        "born_date": "November 22, 1869",
        "born_location": "in Paris, France",
        "description": "André Gide was a French author and winner of the Nobel Prize in Literature..."
    },
    {
        "fullname": "Thomas A. Edison",
        "born_date": "February 11, 1847",
        "born_location": "in Milan, Ohio, The United States",
        "description": "Thomas A. Edison was an American inventor and businessman..."
    },
    {
        "fullname": "Eleanor Roosevelt",
        "born_date": "October 11, 1884",
        "born_location": "in New York, New York, The United States",
        "description": "Eleanor Roosevelt was an American political figure, diplomat, and activist..."
    },
    {
        "fullname": "Steve Martin",
        "born_date": "August 14, 1945",
        "born_location": "in Waco, Texas, The United States",
        "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer..."
    }
]



Структура quotes.json

quotes.json - це файл, який містить інформацію про цитати. Приклад структури:

json
[
    {
        "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
        "author": "Albert Einstein",
        "tags": ["change", "deep-thoughts", "thinking", "world"]
    },
    {
        "quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.",
        "author": "J.K. Rowling",
        "tags": ["abilities", "choices"]
    },
    {
        "quote": "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
        "author": "Albert Einstein",
        "tags": ["inspirational", "life", "classic", "humor"]
    },
    {
        "quote": "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
        "author": "Jane Austen",
        "tags": ["aliteracy", "books", "classic", "humor"]
    },
    {
        "quote": "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.",
        "author": "Marilyn Monroe",
        "tags": ["be-yourself", "inspirational"]
    },
    {
        "quote": "Try not to become a man of success. Rather become a man of value.",
        "author": "Albert Einstein",
        "tags": ["adulthood", "success", "value"]
    },
    {
        "quote": "It is better to be hated for what you are than to be loved for what you are not.",
        "author": "André Gide",
        "tags": ["life", "love"]
    },
    {
        "quote": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas A. Edison",
        "tags": ["edison", "failure", "inspirational", "paraphrased"]
    },
    {
        "quote": "A woman is like a tea bag; you never know how strong it is until it's in hot water.",
        "author": "Eleanor Roosevelt",
        "tags": ["misattributed-eleanor-roosevelt"]
    },
    {
        "quote": "A day without sunshine is like, you know, night.",
        "author": "Steve Martin",
        "tags": ["humor", "obvious", "simile"]
    }
]

