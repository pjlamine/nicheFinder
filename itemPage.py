from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20090722 Chrome/38.0.2125.104 (X) Safari 6 Orca/1.2 build 2")

try:
    driver = webdriver.Chrome(chrome_options=options)
except:
    print "driver failed"

driver = webdriver.Chrome()


# url = "https://www.amazon.com/Toker-Poker-Black/dp/B00HCOTX6E/ref=pd_bxgy_201_img_2?_encoding=UTF8&pd_rd_i=B00HCOTX6E&pd_rd_r=YJZFK2CCS65B7VN05S78&pd_rd_w=sZOdh&pd_rd_wg=bmA6R&psc=1&refRID=YJZFK2CCS65B7VN05S78"
url = "https://www.amazon.com/"
# driver = webdriver.Chrome()
# url = "http://selenium-python.readthedocs.io/locating-elements.html"
driver.get(url);


price = driver.find_element_by_xpath("//*[@id='price']/table/tbody/tr[1]/td[2]/span[1]").text

print price

# print price.text
assert "No results found." not in driver.page_source
print "nada"
driver.close()
