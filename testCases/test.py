# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
#
# # driver = webdriver.Chrome()
# driver = uc.Chrome()
# driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F")
# driver.find_element(By.CSS_SELECTOR, "#Email").clear()
# driver.find_element(By.CSS_SELECTOR, "#Password").clear()
# driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("admin@yourstore.com")
# driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, ".login-button").click()
# sleep(2)

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# 1. 必须先导入，再实例化
driver = uc.Chrome()

# 2. 访问网址
driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F")

# 3. 建议加上一点显式或隐式等待，防止页面没加载完就去找元素
driver.implicitly_wait(10)

try:
    # 清除默认内容
    driver.find_element(By.CSS_SELECTOR, "#Email").clear()
    driver.find_element(By.CSS_SELECTOR, "#Password").clear()

    # 输入账号密码
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("admin@yourstore.com")
    driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("admin")

    # 点击登录
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

    # 登录后等几秒看下结果
    time.sleep(5)
    print("当前页面标题是:", driver.title)

except Exception as e:
    print(f"发生错误: {e}")

# 调试完可以手动关闭或取消注释下行自动关闭
# driver.quit()