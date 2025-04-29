from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException

from util import copy_image_to_clipboard 
import time

class Sender:
    text_box_xpath = (
        '//div[@contenteditable="true" and @data-tab="10"]'
    )

    image_box_xpath = (
        '//div[@contenteditable="true" and @role="textbox" and not(@tabindex)]'
    )

    def __init__(self, phone):
        BASE_URL = "https://web.whatsapp.com/"
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        self.driver.get(BASE_URL)

        self.driver.get(CHAT_URL.format(phone=phone))

    def send_message(self, message, amount=1):
        for _ in range(amount):
            try:
                text_box = WebDriverWait(self.driver, 60).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.text_box_xpath))
                )
                text_box.send_keys(message)
                text_box.send_keys(Keys.ENTER)
            except StaleElementReferenceException:
                print("Elemento de texto no válido. Reintentando...")
                time.sleep(1)

    def send_image(self, path, amount=1):
        copy_image_to_clipboard(path)

        count = 0
        while count < amount:
            for _ in range(10):
                text_box = WebDriverWait(self.driver, 60).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.text_box_xpath))
                )
                text_box.send_keys(Keys.CONTROL, 'v')

                count += 1
                if count >= amount: break

            image_box = WebDriverWait(self.driver, 60).until(
                expected_conditions.presence_of_element_located((By.XPATH, self.image_box_xpath))
            )
            image_box.send_keys(Keys.ENTER)
            time.sleep(1)

    def destroy(self):
        self.driver.quit()