# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time
import random
from PIL import Image
import pytesseract

driver = webdriver.Chrome()
driver.get("http://att.tdtk.com:8092/system/login")
driver.maximize_window()
time.sleep(2)

# 通过页面title判断页面是否加载
print(EC.title_contains("翼票通"))

# 通过页面title判断页面是否加载，title包含返回true，不包含返回false
ss = EC.title_contains("翼票通1")
print(ss(driver))

# 查找3秒，检查username元素是否可见
locator = [By.ID, "username"]
a = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locator))
print(a)

# 输出元素的默认值和输入的值
name_node = driver.find_elements(By.CLASS_NAME, value="content")[0]
name = name_node.find_element(By.ID, value="username")
name.send_keys("yptadmin")
print(name.get_attribute("placeholder"))
print(name.get_attribute("value"))

# 按照一定的格式随机输入用户名
'''rad = ''.join(random.sample('123456asdfc', 4))+"163.com"
print(rad)
name.send_keys(rad)
print(name.get_attribute("value"))
'''

# 截图整个页面并保存
driver.save_screenshot("F:/Python/study/images/img.png")
# 获取要截取的元素
img_element = driver.find_element(By.CLASS_NAME, "otherBg")
print(img_element.location)
# 计算左上右下
left = 1.25*img_element.location['x']
top = 1.25*img_element.location['y']
right = 1.25*(left + img_element.size['width'])
height = 1.25*(top + img_element.size['height'])
print(left, right, top, height)
# 打开之前截取的整个页面
im = Image.open("F:/Python/study/images/img.png")
# 截取需要的部分并保存
image = im.crop((left, top, right, height))
image.save("F:/Python/study/images/img1.png")

# 打开图片
image = Image.open("F:/Python/study/images/img1.png")
# 解析图片
text = pytesseract.image_to_string(image)
print(text)

'''driver.find_element(by=By.ID, value="username").send_keys("123456")
driver.find_element(by=By.ID, value="password").send_keys("123456")
#driver.find_element(by=By.CLASS_NAME, value="checkbox icheck-default").click()
driver.find_element(by=By.ID, value="login_btn").click()

name_node = driver.find_elements(By.CLASS_NAME, value="content")[0]
name = name_node.find_element(By.ID, value="username")
name.send_keys("yptadmin")
'''
pwd = driver.find_element(By.XPATH, value="//*[@id='password']")
pwd.send_keys("tdtk2020")
login_button = driver.find_element(By.ID, value="login_btn")
login_button.click()
time.sleep(5)
aa = EC.title_is("翼票通全域票务系统")
print(aa(driver))
driver.close()