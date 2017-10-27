from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver.close()
#driver.get("http://www.python.org")
#http://selenium-python.readthedocs.io/
#//*[@id="priceblock_saleprice"]
#//*[@id="price"]/table/tbody/tr[1]/td[2]/span[1]
#driver.find_element(By.CSS_SELECTOR, 'p.content:nth-child(1)')

class item:
	num_reviews = 0
	price_max = 0
	price_min = 0
	item_type = ""

	def __init__(self, reviews, maximum, minimum):
		num_reviews = reviews
		price_max = maximum
		price_min = minimum

	def __init__(self, maximum, minimum):
		num_reviews = reviews
		price_max = maximum
		price_min = minimum

	def __init__(self):
		num_reviews = 0
		price_max = 0
		price_min = 0

	#ASSUMED THAT REVIEWS WAS A MAXIMUM
	#aka we want our reviews to be less than input
	def evaluate(self, reviews, price):
		if reviews < self.reviews and  \
		self.maximum > price and self.minimum < price:
			return True
		else:
			return False

url = "https://www.amazon.com/dp/B071HN1MK6/ref=asc_df_B071HN1MK65202322/?tag=hyprod-20&creative=395033&creativeASIN=B071HN1MK6&linkCode=df0&hvadid=216540809005&hvpos=1o2&hvnetw=g&hvrand=7625559591158814614&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9016852&hvtargid=pla-349295148200"
url = "https://www.amazon.com/s/ref=nb_sb_noss/140-8184726-4949017?url=search-alias%3Dgarden&field-keywords=Hemp"

#Toggle if you want it to close when done
close = False 
driver = webdriver.Chrome()
driver.get(url)
print driver.title

# elem = driver.find_element_by_id("twotabsearchtextbox")
# print elem
# elem.clear()
# elem.send_keys("Hemp")
# elem.send_keys(Keys.RETURN)

elem2 = driver.find_element_by_id("s-results-list-atf")

print elem2
result = "result_"
result_num = 0
offset = 0

while (result_num < 20):
	elem2 = driver.find_element_by_id(result + str(result_num))
	print "RANK: ", elem2.get_attribute("data-result-rank"),
	print " ASIN: ", elem2.get_attribute("data-asin"),
	elem3 = driver.find_elements_by_class_name("sx-price-whole")[result_num]
	print "PRICE: ", elem3.text,
	
	elem3 = driver.find_elements_by_css_selector("a.a-size-small.a-link-normal.a-text-normal")[result_num + offset]
	while (not elem3.text[0].isnumeric()):
		offset += 1
		elem3 = driver.find_elements_by_css_selector("a.a-size-small.a-link-normal.a-text-normal")[result_num + offset]
	print  "REVIEWS: ", elem3.text

	result_num += 1 

if close:
	driver.close()

