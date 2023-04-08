from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self,setup):

        setup.driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        i = -1
        for product in products:
            i = i + 1
            productName = product.find_element(By.XPATH,"./div/h4/a").text
            if productName == "Blackberry":
                self.product.find_element(By.XPATH,"div/button").click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("ind")
        wait= WebDriverWait(self.driver,10).until
        EC.presence_of_element_located((By.LINK_TEXT,"India"))
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
        text = self.driver.find_element(By.CLASS_NAME,"//div[@class='alert alert-success alert-dismissible']").text
        assert "Succes! Thank you!" in text
