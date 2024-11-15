import allure
import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.id('1')
@allure.title('Проверить автозаполнение')
@allure.description('Тест проверят автозаполнение города напровления')
@allure.severity('Normal')
def test_check_autofill_moscow(driver):
    driver.get("https://fstravel.com/avia")
    try:
        driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
    except:
       pass
    assert "MOW" in driver.find_element(By.CSS_SELECTOR, ".v-select__iata").text


@allure.id('2')
@allure.title('Проверить на заполения поля')
@allure.description('Тест проверят пройдет ли если поле не заполненно')
@allure.severity('Normal')
def test_negative_empty_field(driver):
    driver.get("https://fstravel.com/avia")
    try:
        driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
    except:
       pass
    driver.find_element(By.CSS_SELECTOR, ".v-search-button").click()
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Заполните поле')]").is_displayed()


@allure.id('3')
@allure.title('Проверить вкладку бронирования отеля ')
@allure.description('Тест проверят бронирования отеля')
@allure.severity('Normal')
def test_header(driver):
    driver.get("https://fstravel.com/searchhotel")
    try:
        driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
    except:
       pass
    assert "Бронирование отелей" in driver.find_element(By.CSS_SELECTOR, ".meta-h1").text


@allure.id('4')
@allure.title('Проверить найденные туры')
@allure.description('Тест проверят какие есть туры')
@allure.severity('Normal')
def test_search_tour(driver):
    driver.get("https://fstravel.com/searchtour")
    try:
        driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
    except:
       pass
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.tour-search__button')))
    driver.find_element(By.CSS_SELECTOR, '.tour-search__button').click()
    assert "Туры в " in driver.find_element(By.CSS_SELECTOR, "h1.header-title").text
    assert "найдено" in driver.find_element(By.CSS_SELECTOR, "span.header-title").text


@allure.id('5')
@allure.title('Проверить заявку на тур')
@allure.description('Тест проверят мы можем оставить заявку')
@allure.severity('Normal')
def test_tour_request(driver):
    driver.get("https://fstravel.com/avia")
    try:
        driver.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
    except:
       pass
    driver.find_element(By.CSS_SELECTOR, ".v-header-left-link").click()
    assert "Оставьте заявку и мы подберём вам тур" in driver.find_element(By.CSS_SELECTOR, ".tour-order-popup__header-text").text

