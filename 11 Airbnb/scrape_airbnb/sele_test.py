from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import json

# 尝试手动登录获得cookies
def login(driver, username="2297186491@qq.com", password="19980215xx@"):
    # 登录
    homepage = "https://www.airbnb.cn/login"
    driver.get(homepage)
    time.sleep(2)
    elem = driver.find_element_by_xpath('//*[@class="_rqfxvmb"]/div[contains(text(),"账号密码登录")]')
    # accountElem = driver.find_element_by_xpath('//*[@id="signin_email"]')
    # accountElem.click()
    elem.click()
    time.sleep(0.5)
    # accountElem.send_keys(username)
    usernameElem = driver.find_element_by_xpath('//*[@id="phone-or-email-login-phone-or-email"]')
    usernameElem.click()
    time.sleep(0.5)
    usernameElem.send_keys(username)
    time.sleep(0.5)
    passwordElem = driver.find_element_by_xpath('//*[@id="phone-or-email-login-password"]')
    passwordElem.click()
    time.sleep(0.5)
    passwordElem.send_keys(password)
    time.sleep(0.5)
    confrimElem = driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div/form/div/div[5]/div/div/div[3]/div/button')
    confrimElem.click()
    time.sleep(5)
    # # cookies_list = driver.get_cookies()
    # for cookie in cookies_list:
    #     driver.add_cookie(cookie)
    # # 将cookies保存到本地
    # 从这里继续看:https://www.cnblogs.com/ytraister/p/13379779.html
    with open('cookies.txt', 'w') as f:
        cookies = driver.get_cookies()
        print(cookies)
        f.write(json.dumps(cookies))
    driver.close()


# 显性等待,直到出现用户账户信息
def downloadpicture(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="_9ofhsl"]')))
        photoElem = driver.find_element_by_xpath('//img[@class="_9ofhsl"]').get_attribute("src")
        photo = requests.get(photoElem)
        with open('test.png', 'wb') as f:
            f.write(photo.content)
    except TimeoutError as e:
        return



# url = "https://www.airbnb.com/users/show/160417028"
# driver.get(url)

if __name__ == '__main__':
    # driver = webdriver.Firefox()  # Firefox浏览器
    # login(driver)
    driver = webdriver.Firefox()
    with open('cookies2.txt', 'r') as f:
        cookies_list = json.load(f)
        for cookie in cookies_list:
            driver.add_cookie(cookie)
    downloadpicture(driver, "https://zh.airbnb.com/users/show/160417028")