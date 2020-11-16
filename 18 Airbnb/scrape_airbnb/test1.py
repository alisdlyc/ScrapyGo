from selenium import webdriver
from selenium.webdriver.common.keys import Keys## 模拟键盘用的包
from selenium.webdriver.support.ui import Select##用来操作下拉列表中的选择题
from selenium.common.exceptions import NoSuchElementException## 找不到元素会报的错
import time##不能一直爬取页面所以需要睡一会儿
import json##用来保存网站登录cookie，以后可以免密登录网站

## 打开一个空白浏览器
driver = webdriver.Firefox()

## 进入airbnb官网
url = "https://www.airbnb.com/"
driver.get(url)

## 窗口最大化
driver.maximize_window()

## 通过xpath 找到并点击登录按钮
login_xpath = "/html/body/div[3]/div[1]/div/header/div/div/div[3]/div/div/nav/ul/li[9]/div/div/button"
driver.find_element_by_xpath(login_xpath).click()

## 选择用邮箱登录
email_xpath = "/html/body/div[11]/section/div/div/div[2]/div/div[2]/button"
driver.find_element_by_xpath(email_xpath).click()


## 输入email地址和密码

## inspect后这俩的id很独特，所以直接用了
email_id = "email"
pw_id = "password"

your_email = input("please enter your email address")
your_pw    = input("please enter your password")

e = driver.find_element_by_id(email_id)
e.clear()
e.send_keys(your_email)

p = driver.find_element_by_id(pw_id)
p.clear()
p.send_keys(your_pw)

## 点击登录按钮
enter_xpath = "/html/body/div[11]/section/div/div/div[2]/div/form/div[3]/button"
driver.find_element_by_xpath(enter_xpath).click()

## 保存cookie
cookies = driver.get_cookies()
#print(cookies)

## 新建json文件，将cookies保存进去
file = open("cookies.json", "w", encoding = 'utf-8')
json.dump(cookies, file, ensure_ascii = False)
file.close()