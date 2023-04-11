import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_coordinate(browser,addr):
    try:
        search = browser.find_element(By.ID,"lat")
        search.clear()
        search.send_keys(addr)
        button = browser.find_element(By.XPATH,'//*[@id="geo"]/div[1]/button')
        button.click()
        time.sleep(1)
        text=browser.find_element(By.XPATH,'//*[@id="geo"]/div[1]/h2')
        lat,lon=float(text.text.split()[0]),float(text.text.split()[2])
        browser.refresh()
        print(addr,lat,lon)
    except:
        print(addr,'發生錯誤')
        pass
    return lat,lon

if __name__ == "__main__":
    browser = webdriver.Chrome("..\chromedriver_win32\chromedriver.exe")
    browser.get("https://share-my-location.com/zh-TW/geocoding")
    cookie_check = browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div[2]/div/div/div/label').click()
    with open('input.txt',encoding='utf-8') as f:
        with open('output.txt','w',encoding='utf-8') as fo:
            for i in f.readlines():
                addr=i.strip()
                lat,lon=get_coordinate(browser,addr)
                fo.write(f"{addr},{lat},{lon}\n")



