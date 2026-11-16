from scraper import get_book_data


def test_slovary_i_klyuchi():
    ssilka = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    dannie = get_book_data(ssilka)
    assert type(dannie) == dict
    assert 'Название' in dannie
    assert 'Цена' in dannie


def test_nazvanie():
    ssilka = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    dannie = get_book_data(ssilka)
    assert dannie['Название'] == 'A Light in the Attic'


def test_cena_i_reiting():
    ssilka = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    dannie = get_book_data(ssilka)
    assert dannie['Цена'] == '£51.77'
    assert dannie['Рейтинг'] == 'Three'