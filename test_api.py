import allure
import requests
from url import *


@allure.id('1')
@allure.title('Проверить по городу')
@allure.description('Тест проверят возврат кода 200 при отправке запроса на поиск города Душанбе')
@allure.severity('Normal')
def test_search_by_origin():
    response = requests.get(f'{base_upl1}/cities/search?value=DYU')
    assert response.status_code == 200


@allure.id('2')
@allure.title('Проверить по городам напровления')
@allure.description('Тест проверят возврат кода 200 при отправке запроса по городам направления')
@allure.severity('Normal')
def test_search_by_cities():
    response = requests.get(f'{base_upl2}/filters/DepartureCities')
    assert response.status_code == 200


@allure.id('3')
@allure.title('Проверить популярным городам')
@allure.description('Тест проверят возврат кода 200 при отправке запроса по популярным городам')
@allure.severity('Normal')
def test_search_by_popularcities():
    response = requests.get('https://avia-new.fstravel.com/api/avia/external/cities/get-popular-cities')
    assert response.status_code == 200


@allure.id('4')
@allure.title('Проверить города добавленные в избранные')
@allure.description('Тест проверят возврат кода 200 при отправке билеты из Москвы')
@allure.severity('Normal')
def test_search_by_wishList():
    response = requests.get(f'{base_upl2}/search/wishList')
    assert response.status_code == 200


@allure.id('5')
@allure.title('Проверить города из Москвы')
@allure.description('Тест проверят возврат кода 200 при отправке из Москвы')
@allure.severity('Normal')
def test_search_by_moskow():
    response = requests.get(f'{base_upl1}/cities/search?value=MOW')
    assert response.status_code == 200

