from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from time import sleep


def test_01(chrome):
    chrome.get('https://demoqa.com/text-box')

    chrome.find_element(By.XPATH, "//*[@id='userName']").send_keys('Iryna Moroz')
    chrome.find_element(By.XPATH, "//*[@id='userEmail']").send_keys('moroz9191777@gmail.com')
    chrome.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys('My current address')
    chrome.find_element(By.XPATH, "//*[@id='permanentAddress']").send_keys('My permanent address')
    # chrome.find_element(By.XPATH, "//*[@id='submit']").click()
    chrome.find_element(By.XPATH, "//*[@id='submit']").send_keys(Keys.ENTER)
    # sleep(5)
    print(chrome.find_element(By.XPATH, "//*[@id='output']").text)
