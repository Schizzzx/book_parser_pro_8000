import os
import requests
from bs4 import BeautifulSoup


def get_book_data(book_url: str) -> dict:
    otvet = requests.get(book_url)
    otvet.encoding = 'utf-8'
    sup = BeautifulSoup(otvet.text, 'html.parser')

    nazvanie = sup.find('h1').text

    glavnyi_blok = sup.find('div', class_='product_main')
    cena = glavnyi_blok.find('p', class_='price_color').text

    reiting_teg = glavnyi_blok.find('p', class_='star-rating')
    reiting = reiting_teg['class'][1]

    nalichie = glavnyi_blok.find('p', class_='instock').text.strip()

    opisanie_zagolovok = sup.find('div', id='product_description')
    if opisanie_zagolovok:
        opisanie = opisanie_zagolovok.find_next_sibling('p').text
    else:
        opisanie = ''

    dannie = {
        'Название': nazvanie,
        'Цена': cena,
        'Рейтинг': reiting,
        'Наличие': nalichie,
        'Описание': opisanie
    }

    tablica = sup.find('table', class_='table-striped')
    for stroka in tablica.find_all('tr'):
        klyuch = stroka.find('th').text
        znachenie = stroka.find('td').text
        dannie[klyuch] = znachenie

    return dannie


def scrape_books(is_save: bool = False) -> list:
    vse_knigi = []
    nomer_stranicy = 1

    while True:
        ssilka_stranicy = f'http://books.toscrape.com/catalogue/page-{nomer_stranicy}.html'
        otvet = requests.get(ssilka_stranicy)
        if otvet.status_code != 200:
            break

        sup = BeautifulSoup(otvet.text, 'html.parser')
        kartochki = sup.find_all('article', class_='product_pod')

        for kartochka in kartochki:
            hvost = kartochka.find('h3').find('a')['href']
            ssilka_knigi = 'http://books.toscrape.com/catalogue/' + hvost
            kniga = get_book_data(ssilka_knigi)
            vse_knigi.append(kniga)

        nomer_stranicy += 1

    if is_save:
        os.makedirs('artifacts', exist_ok=True)
        with open('artifacts/books_data.txt', 'w', encoding='utf-8') as fail:
            for kniga in vse_knigi:
                fail.write(str(kniga) + '\n')

    return vse_knigi