import time
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# from selenium.webdriver import ActionChains


def setup_module():
    pass


def teardown_module():
    pass


def test_google_search():
    # This example requires Selenium WebDriver 3.13 or newer
    # with webdriver.Chrome(executable_path="C:/WebDriver/bin/chromedriver.exe") as driver:
    with webdriver.Chrome() as driver:
        # with webdriver.Firefox() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://google.com/ncr")
        # driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
        driver.find_element_by_name("q").send_keys(
            "cheese" + Keys.RETURN)  # 加回车进行搜索
        first_result = wait.until(
            presence_of_element_located((By.CSS_SELECTOR, "#rcnt")))
        # print(first_result.get_attribute("textContent"))
        print('title: ' + driver.title)
        assert 'Google' in driver.title
        # driver.quit()


# https://blog.csdn.net/xiaosongbk/article/details/53188355
def test_move_to_menu():
    with webdriver.Chrome() as driver:
        driver.get('https://www.mi.com/global/index.html')
        # xiaomi_menu=driver.find_element(By.CSS_SELECTOR,'[data-stat-id="bec765342dd7b5cf"]')
        # xiaomi_menu=driver.find_element_by_css_selector('[data-stat-id="bec765342dd7b5cf"]')
        xiaomi_menu = driver.find_element(
            By.CSS_SELECTOR, '[data-stat-id="bec765342dd7b5cf"][target="_self"]')
        ac = ActionChains(driver)
        ac.move_to_element(xiaomi_menu).perform()
        time.sleep(3)

        # JAVA 写法：
        # products=driver.findElements(By.xpath('//a[contains(@href, "logout")]')) #Java
        # WebElement password = driver.findElement(By.xpath("//*[@id='J_login_form']/*/*/input[@id='J_password']"));#Java
        # WebElement password = driver.findElement(By.xpath("//*[@id='J_login_form']/dl/dt/input[@id='J_password']"));#Java
        # WebElement password = driver.findElement(By.cssSelector("#J_login_form>dl>dt>input[id='J_password']")); #Java

        products = driver.find_elements_by_xpath(
            '//div[@id="J_shopCategories"]/div/dl/dd/div/div')  # by_xpath
        print(len(products))
        products = driver.find_elements_by_css_selector(
            '#J_shopCategories>div>dl>dd>div>div')  # by_css_selector
        print(len(products))
        print(products)

        names = []
        for product in products:
            names.append(product.text)
        print(names)


if __name__ == '__main__':
    pytest.main(['test2.py', "-s"])
    # pytest.main(["test2.py", "-s", "--alluredir=report/allure"])
    os.system("allure serve ../report/allure")

# https://blog.csdn.net/xiaosongbk/article/details/53188355
# 此外，cssSelector还有一些高级用法，如果熟练后可以更加方便地帮助我们定位元素，如我们可以利用^用于匹配一个前缀，$用于匹配一个后缀，*用于匹配任意字符。例如：

# 匹配一个有id属性，并且id属性是以”id_prefix_”开头的超链接元素：a[id^='id_prefix_']

# 匹配一个有id属性，并且id属性是以”_id_sufix”结尾的超链接元素：a[id$='_id_sufix']

# 匹配一个有id属性，并且id属性中包含”id_pattern”字符的超链接元素：a[id*='id_pattern']
