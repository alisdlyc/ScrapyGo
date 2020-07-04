import sys
import time
import xlwt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    keyword = 'JavaWeb' \
              ''
    if len(sys.argv) > 1:
        keyword = sys.argv[1]

    new_workbook = xlwt.Workbook()
    worksheet = new_workbook.add_sheet('jd')

    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)

    driver.get('https://www.jd.com/')

    kw = driver.find_element_by_id('key')
    kw.send_keys(keyword)
    kw.send_keys(Keys.RETURN)

    time.sleep(2)
    # 点击按照销量排行
    sort_btn = driver.find_element_by_xpath('.//div[@class="f-sort"]/a[2]')
    sort_btn.click()
    page = 1
    rows = []
    i = 1

    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(0.5)
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight/2)')
        # time.sleep(2)
        products = driver.find_elements_by_class_name('gl-item')
        url_model = 'https:%s'
        flag = False
        for p in products:
            row = {}
            sku = p.get_attribute('data-sku')
            row['price'] = p.find_element_by_css_selector('strong.J_%s' % sku).text
            row['name'] = p.find_element_by_css_selector('div.p-name>a>em').text
            row['comments'] = p.find_element_by_id('J_comment_%s' % sku).text
            try:
                row['shop'] = p.find_element_by_css_selector('div.p-shop>span>a').text
            except Exception:
                row['shop'] = '店名被恶龙吃掉了 嗷呜'
            print(row)
            # rows.append(row)
            worksheet.write(i, 0, row['price'])
            worksheet.write(i, 1, row['name'])
            worksheet.write(i, 2, row['comments'])
            i = i + 1
        try:
            next_page = driver.find_element_by_xpath('//a[@class="pn-next"]')
        except Exception:
            flag = True
            break

        if flag:
            break
        else:
            # if 'disabled' in next_page:
            if 'disabled' in next_page.get_attribute('class'):
                flag = True
        print("current page number is ",
              driver.find_element_by_xpath('//div[@id="J_bottomPage"]//a[@class="curr"]').text)

        try:
            next_page.click()
        except Exception:
            break


    # pyexcel.save_as(records=rows, dest_file_name='%s.xls' % keyword)
    new_workbook.save('./%s.xls' % keyword)
    driver.quit()
