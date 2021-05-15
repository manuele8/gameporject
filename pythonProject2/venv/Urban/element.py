from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")

class BasePageElement2(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator2))
        driver.find_element_by_xpath(self.locator2).clear()
        driver.find_element_by_xpath(self.locator2).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator2))
        element = driver.find_element_by_xpath(self.locator2)
        return element.get_attribute("value")

class BasePageElement3(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator3))
        driver.find_element_by_xpath(self.locator3).clear()
        driver.find_element_by_xpath(self.locator3).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator3))
        element = driver.find_element_by_xpath(self.locator3)
        return element.get_attribute("value")

class BasePageElement4(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator4))
        driver.find_element_by_xpath(self.locator4).clear()
        driver.find_element_by_xpath(self.locator4).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator4))
        element = driver.find_element_by_xpath(self.locator4)
        return element.get_attribute("value")