from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time

class Sender:
    def __init__(self, phone):
        BASE_URL = "https://web.whatsapp.com/"
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        self.driver.get(BASE_URL)

        self.driver.get(CHAT_URL.format(phone=phone))
        time.sleep(3)

        # chat text box location
        inp_xpath = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        )
        self.input_box = WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
        )

    def send_message(self, message, amount=1):
        for i in range(amount):
            self.input_box.send_keys(message)
            self.input_box.send_keys(Keys.ENTER)

    def destroy(self):
        self.driver.quit()



