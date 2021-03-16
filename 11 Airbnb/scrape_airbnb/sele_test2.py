from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import json
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 尝试手动登录获得cookies
def login(driver, username="2297186491@qq.com", password="19980215xx@"):
    driver.delete_all_cookies()
    driver.get("https://zh.airbnb.com/users/show/160417028")
    wait = WebDriverWait(driver, 5)
    # loginElem = driver.find_element_by_xpath('//ul[@class="_1s04l2o"]/li[last()]//button')
    loginElem = wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="_1s04l2o"]/li[last()]//button')))
    loginElem.click()
    time.sleep(30)
    driver.refresh()
    cookies = driver.get_cookies()
    print(cookies)
    if len(cookies):
        f1 = open('cookie.txt', 'w')
        f1.write(json.dumps(cookies))
        f1.close


def visit(driver, prefix, user_id):
    # 房客有可能是房东,对是否存在[房客/房东评价进行判断]
    # 再加一个评论来源选项,xpath要用contain
    url = prefix + user_id
    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="_9ofhsl"]')))
        # 下载图片
        photoElem = driver.find_element_by_xpath('//img[@class="_9ofhsl"]').get_attribute("src")
        photo = requests.get(photoElem)
        with open(f'{user_id}.png', 'wb') as f:
            f.write(photo.content)
        # 获得评论内容
        # 先判断用户到底是纯房客还是房东/房客
        if_reviewer_button = True

        try:
            # 房客/参与者评价
            # selenium点击失败,执行js,解决seleniumclick按钮失灵的一个方法
            # reviewer_button = driver.find_element_by_xpath("//button[contains(text(), '房客/参与者评价')]")
            driver.execute_script('document.getElementById("tab--user-profile-review-tabs--0").click()')
            """
            document.querySelector("#tab--user-profile-review-tabs--0")
            """
        except:
            if_reviewer_button = False

        comments = None  # user_id = "160417028"
        comments1, comments2 = None, None  # user_id = "66056138"
        if not if_reviewer_button:
            comment_xpath = '//div[@class="_1v365y9"]/div[@class="_1v8nkzp"]/div[2]/span'
            comments = driver.find_elements_by_xpath(comment_xpath)
        else:
            # 先点击房客/参与者评价,这个一开始已经点过了
            # comment_xpath1 和 comment_xpath2 写错了,debug发现只对应上一条
            comment_xpath1 = '//*[@id="panel--user-profile-review-tabs--0"]/div[1]/div[1]/div[2]/span'
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, comment_xpath1)))
            comments1 = driver.find_elements_by_xpath(comment_xpath1)
            time.sleep(0.2)
            # 再点击房东/体验达人评价
            comment_xpath2 = '//*[@id="panel--user-profile-review-tabs--1"]/div[1]/div[1]/div[2]/span'
            driver.execute_script('document.getElementById("tab--user-profile-review-tabs--1").click()')
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, comment_xpath2)))
            comments2 = driver.find_elements_by_xpath(comment_xpath2)
        # 获得评价总数
        comment_number = driver.find_element_by_xpath('//*[@id="review-section-title"]')
        rets = []
        if comments:
            for comment in comments:
                if comment.text != "展开":
                    rets.append([user_id, comment.text, comment_number.text, "hosts"])
        else:
            # 先合并来自房客的评价
            for comment in comments1:
                if comment.text != "展开":
                    rets.append([user_id, comment.text, comment_number.text, "reviewers"])
            # 再合并来自房东的评价
            for comment in comments2:
                if comment.text != "展开":
                    rets.append([user_id, comment.text, comment_number.text, "hosts"])

        return rets
    # 页面打不开,返回空
    except TimeoutError as e:
        return [user_id, None, None, None]


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://zh.airbnb.com/users/show/160417028"

    login_in_cookies = True
    if login_in_cookies:
        driver.get("https://zh.airbnb.com/users/show/160417028")
        f1 = open('cookie.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
    else:
        login(driver)

    # # 刷新页面
    driver.refresh()
    prefix = "https://zh.airbnb.com/users/show/"
    user_ids_path = "0303id.csv"
    reader = pd.read_csv(user_ids_path, chunksize=100, header=None)
    num = 0
    with open("user_info.txt", 'w', encoding="utf-8") as f:
        for chunk in reader:
            for c in chunk.values:
                user_id = str(c[0])
                # 可以这两个分别尝试
                # user_id = "160417028"
                # user_id = "66056138"
                rets = visit(driver, prefix, user_id)
                for ret in rets:
                    f.write(f"{ret[0]},{ret[1]},{ret[2]},{ret[3]}")
                    f.write("\n")
                    f.flush()