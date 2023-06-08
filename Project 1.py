import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SauceDemo:

    def __init__(self):
        self.driver_service = Service(executable_path=r'C:\Users\Asus\PycharmProjects\pythonProject2\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com/')
        time.sleep(2)

    def username(self):
        casuta_user = self.driver.find_element(By.XPATH, "//input[@id= 'user-name']")
        casuta_user.send_keys('standard_user')

    def password(self):
        casuta_pass = self.driver.find_element(By.XPATH, "//input[@id= 'password']")
        casuta_pass.send_keys('secret_sauce')

    def submit(self):
        buton_submit = self.driver.find_element(By.XPATH, "//input[@class= 'submit-button btn_action']")
        buton_submit.click()
        time.sleep(2)

    def cart1(self):
        add_1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_1.click()
        time.sleep(2)

    def cart2(self):
        add_2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_2.click()
        time.sleep(2)

    def cart3(self):
        add_3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_3.click()
        time.sleep(2)

    def cart4(self):
        add_4 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        add_4.click()
        time.sleep(2)
        self.scroll_by_value(300)

    def cart5(self):
        add_5 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_5.click()
        time.sleep(2)

    def cart6(self):
        add_6 = self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        add_6.click()
        time.sleep(2)

    def scroll_by_value(self, scrollvalue):
        self.driver.execute_script(f'window.scrollBy(0, {scrollvalue});')
        time.sleep(2)

    def cos_cumparaturi(self):
        cosulet = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        self.scroll_by_value(-700)
        cosulet.click()
        time.sleep(3)

    def remove_item(self):
        buton_remove = self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
        buton_remove.click()
        self.scroll_by_value(300)
        time.sleep(3)

    def checkout(self):
        buton_checkout = self.driver.find_element(By.CSS_SELECTOR, "#checkout")
        buton_checkout.click()
        time.sleep(3)

    def first_name(self):
        firstname = self.driver.find_element(By.ID, "first-name")
        firstname.send_keys('andrei')

    def lastname(self):
        numedefamilie = self.driver.find_element(By.ID, "last-name")
        numedefamilie.send_keys('vasilca')

    def zipcode(self):
        codpostal = self.driver.find_element(By.ID, "postal-code")
        codpostal.send_keys('110092')

    def butonassubsmit(self):
        subbuton = self.driver.find_element(By.XPATH, "//input[@class = 'submit-button btn btn_primary cart_button btn_action']")
        subbuton.click()
        time.sleep(2)

    def Finish(self):
        buton_finish = self.driver.find_element(By.CSS_SELECTOR, "#finish")
        self.scroll_by_value(800)
        buton_finish.click()
        time.sleep(3)

    def backhome(self):
        buton_backhome = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn_primary btn_small']")
        buton_backhome.click()

    def toatedef(self):
        self.username()
        self.password()
        self.submit()
        self.cart1()
        self.cart2()
        self.cart3()
        self.cart4()
        self.cart5()
        self.cart6()
        self.cos_cumparaturi()
        self.remove_item()
        self.checkout()
        self.first_name()
        self.lastname()
        self.zipcode()
        self.butonassubsmit()
        self.Finish()
        self.backhome()

a1 = SauceDemo()
a1.toatedef()



