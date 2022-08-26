from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.okx.com/hk/trade-convert/stablecoin/usdt")
time.sleep(30)
while True:
    time.sleep(3)
    try:
        if float(driver.find_element("xpath", "/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div[4]/span[1]").text.replace(",", "")) < float(driver.find_element("xpath", "/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div[6]/span[1]").text.replace(",", "")):
            driver.find_element("xpath", "/html/body/div[7]/div/div[3]/div/button[2]").click()
            time.sleep(0.3)
            driver.find_element("xpath", "/html/body/div[7]/div/div[1]/div[3]/i").click()
            time.sleep(0.3)
            
    except:
        time.sleep(0.3)
        driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[3]').click()
        time.sleep(0.3)
        driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/span").click()
        time.sleep(0.3)
        driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/button").click()
