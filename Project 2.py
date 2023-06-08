import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Exercitiu:


    def __init__(self):
        self.driver_service = Service(executable_path=r'C:\Users\Asus\PycharmProjects\pythonProject2\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()
        self.driver.get('https://magento.softwaretestingboard.com/')
        # self.driver.implicitly_wait(10)

    def Createaccount(self):
        Create_button = self.driver.find_element(By.XPATH, "//a[text() = 'Create an Account']")
        Create_button.click()

    def Personal_info(self, Firstname, Lastname):
        firstname_field = self.driver.find_element(By.CSS_SELECTOR, "#firstname")
        firstname_field.send_keys(Firstname)
        time.sleep(2)
        lastname_field = self.driver.find_element(By.CSS_SELECTOR, "#lastname")
        lastname_field.send_keys(Lastname)

    def checkbox(self):
        casuta_check = self.driver.find_element(By.XPATH, "//input[@type = 'checkbox']")
        casuta_check.click()
        # time.sleep(3)

    def singin_info(self, email, password):
        email_field = self.driver.find_element(By.XPATH, "//input[@id= 'email_address']")
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.XPATH, "//input[@id= 'password']")
        password_field.send_keys(password)
        password_conf = self.driver.find_element(By.XPATH, "//input[@name= 'password_confirmation']")
        password_conf.send_keys(password)
        time.sleep(4)

    def scroll_by_value(self, scroll_value):
        self.driver.execute_script(f'window.scrollBy(0, {scroll_value});')
        time.sleep(2)

    def Finish_creation_process(self):
        Buton_finish = self.driver.find_element(By.XPATH, "//span[text()= 'Create an Account']")
        Buton_finish.click()
        time.sleep(3)

    def check_user_singed_in(self):
        text_logged_in = self.driver.find_element(By.XPATH, "//span[@class= 'logged-in']")
        if text_logged_in.is_displayed():
            print("You are logged in")
        else:
            print("You are not logged in")
        time.sleep(3)

    def Gear(self):
        buton_gear = self.driver.find_element(By.XPATH, "//span[text()= 'Gear']")
        buton_gear.click()
        time.sleep(2)

    def Fitness(self):
        buton_fitness = self.driver.find_element(By.XPATH, "//a[text()= 'Fitness Equipment']")
        buton_fitness.click()
        time.sleep(5)

    def Item(self):
        buton_item = self.driver.find_element(By.XPATH, "//img[@alt= 'Dual Handle Cardio Ball']")
        buton_item.click()
        time.sleep(4)

    def Qty_box(self):
        casuta_qty = self.driver.find_element(By.XPATH, "//input[@id= 'qty']")
        casuta_qty.clear()
        casuta_qty.send_keys(10)

    def Add_to_cart(self):
        buton_add_to_cart = self.driver.find_element(By.XPATH, "(//span[text() = 'Add to Cart'])[1]")
        buton_add_to_cart.click()
        time.sleep(2)

    def Cart(self):
        cart_bt = self.driver.find_element(By.XPATH, "//a[@class = 'action showcart']")
        time.sleep(3)
        cart_bt.click()
        time.sleep(3)

    def Proceed_to_checkout(self):
        buton_proceed = self.driver.find_element(By.XPATH, "//button[@id= 'top-cart-btn-checkout']")
        buton_proceed.click()
        time.sleep(5)

    def Detalii_transport(self, Address, City, PostalCode, PhoneNumber):
        Adress_field = self.driver.find_element(By.XPATH, "//input[@name= 'street[0]']")
        Adress_field.send_keys(Address)
        City_field = self.driver.find_element(By.XPATH, "//input[@name= 'city']")
        City_field.send_keys(City)
        Postal_field = self.driver.find_element(By.XPATH, "//input[@name= 'postcode']")
        Postal_field.send_keys(PostalCode)
        Phone_field = self.driver.find_element(By.XPATH, "//input[@name= 'telephone']")
        Phone_field.send_keys(PhoneNumber)
        time.sleep(5)

    def Dropdown(self):
        dropdown_elements = self.driver.find_element(By.XPATH, "//select[@name= 'region_id']")
        dropdown_menu = Select(dropdown_elements)
        dropdown_menu.select_by_visible_text("Colorado")
        time.sleep(7)

    def Payment_method(self):
        buton_payment = self.driver.find_element(By.XPATH, "(//input[@type = 'radio'])[2]")
        buton_payment.click()
        time.sleep(2)

    def Next(self):
        next_button = self.driver.find_element(By.XPATH, "(//button[@type= 'submit'])[2]")
        next_button.click()
        time.sleep(5)

    def Place_order(self):
        buton_order = self.driver.find_element(By.XPATH, "//span[text()= 'Place Order']")
        buton_order.click()
        time.sleep(3)

    def Rezultat_order(self):
        text_order = self.driver.find_element(By.XPATH, "//a[@class = 'order-number']")
        print(text_order.text)
        time.sleep(2)

    def allmethods(self):
        self.Createaccount()
        self.Personal_info("Andrei", "Vasilca")
        self.checkbox()
        self.scroll_by_value(400)
        self.singin_info(f"andrei.vasilcaab4545464054s1@gmail.com", "Vasilca!Andrei123A")
        self.Finish_creation_process()
        self.check_user_singed_in()
        self.Gear()
        self.Fitness()
        self.Item()
        self.Qty_box()
        self.Add_to_cart()
        self.Cart()
        self.Proceed_to_checkout()
        self.Detalii_transport('Abcdef', "Bucuresti", 10022, f"0788449922")
        self.Dropdown()
        self.Payment_method()
        self.Next()
        self.Place_order()
        self.Rezultat_order()


i1 = Exercitiu()
i1.allmethods()
