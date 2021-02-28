from asyncio import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_drag_drop():
    driver = webdriver.Chrome()
    driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
    element_drag_drop = driver.find_element_by_xpath('//*[@id="dragger"]')
    element_drag_drop_item1 = driver.find_element_by_xpath('/html/body/div[2]')
    element_drag_drop_item2 = driver.find_element_by_xpath('/html/body/div[3]')
    sleep(2)
    element_drag_drop_item3 = driver.find_element_by_xpath('/html/body/div[4]')
    sleep(2)
    element_drag_drop_item4 = driver.find_element_by_xpath('/html/body/div[5]')
    action =ActionChains(driver)

    action.drag_and_drop(element_drag_drop,element_drag_drop_item1)
    action.drag_and_drop(element_drag_drop, element_drag_drop_item2)
    # action.click_and_hold(element_drag_drop).move_to_element(element_drag_drop_item2).release()
    action.drag_and_drop(element_drag_drop,element_drag_drop_item3)
    action.drag_and_drop(element_drag_drop, element_drag_drop_item4)
    # action.click_and_hold(element_drag_drop).move_to_element(element_drag_drop_item4).release()
    action.perform()
    sleep(5)

