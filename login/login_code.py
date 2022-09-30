# coding = utf-8

import time
import random
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

driver = webdriver.Chrome()


# 浏览器初始化
def driver_init():
    driver.get("http://att.tdtk.com:8092/system/login")
    driver.maximize_window()
    time.sleep(2)


# 获取element信息
def get_element(by, value):
    element = driver.find_element(by, value)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('xqk', 3))
    return user_info


# 获取图片
def get_image(file_name):
    driver.save_screenshot(file_name)
    img_element = driver.find_element(By.CLASS_NAME, "otherBg")
    left = 1.25 * img_element.location['x']
    top = 1.25 * img_element.location['y']
    right = 1.25 * (left + img_element.size['width'])
    height = 1.25 * (top + img_element.size['height'])
    im = Image.open("F:/Python/study/images/img.png")
    image = im.crop((left, top, right, height))
    image.save(file_name)


# 解析图片
def image_read(file_name):
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)
    return text


# 运行主程序
def run_main():
    user = get_range_user() + "admin"
    file_name = "F:/Python/study/images/img.png"
    driver_init()
    get_element(By.ID, "username").send_keys(user)
    get_element(By.ID, "password").send_keys(123456)
    get_image(file_name)
    text = image_read(file_name)
    get_element(By.ID, "login_btn").click()
    time.sleep(3)
    driver.close()


run_main()