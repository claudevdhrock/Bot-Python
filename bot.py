from selenium import webdriver
import time


driver = webdriver.Chrome("chromedriver.exe")

while(True):
    driver.get('https://www.ytverts.com/')
    driver.maximize_window()

    try:
        time.sleep(1)
        login = driver.find_element_by_name("login")
        login.click()
        login.send_keys('***********@*********.com')

        contra = driver.find_element_by_name("pass")
        contra.click()
        contra.send_keys('************')
        time.sleep(1)

        btn_log = driver.find_element_by_name("connect")
        btn_log.click()
        time.sleep(1)
    except Exception as e:
        pass

    driver.get('https://www.ytverts.com/earn.php')
    search_btn = driver.find_element_by_id("surfButton")
    search_btn.click()
    while(True):
        time.sleep(5)
        countDown = driver.find_element_by_xpath(".//span[@id = 'countDown']").text
        if countDown == "0":
            time.sleep(10)
            countDownTwo = driver.find_element_by_xpath(".//span[@id = 'countDown']").text
            if countDownTwo == "0":

                window_before = driver.window_handles[1]
                driver.switch_to_window(window_before)
                driver.close()

                window_after = driver.window_handles[0]
                driver.switch_to_window(window_after)
                driver.close()

                time.sleep(1)

                driver = webdriver.Chrome("chromedriver.exe")
                driver.get('https://www.ytverts.com/')
                time.sleep(1)
                login = driver.find_element_by_name("login")
                login.click()
                login.send_keys('**********@******.com')

                contra = driver.find_element_by_name("pass")
                contra.click()
                contra.send_keys('**********')
                time.sleep(1)

                btn_log = driver.find_element_by_name("connect")
                btn_log.click()
                time.sleep(1)
                driver.get('https://www.ytverts.com/earn.php')
                search_btn = driver.find_element_by_id("surfButton")
                search_btn.click()
    break
    break







# driver.quit()
