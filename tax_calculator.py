import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

PATH = "C:\Program Files (x86)\chromedriver.exe"
# Website: https://www.whatismybrowser.com/detect/what-is-my-user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
# Warning: website is not secure. (alternative)
# tax_url_2 = "http://www.sale-tax.com/"
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, executable_path=PATH)

# Primary website
tax_url = "https://www.avalara.com/"

test_url = "https://www.avalara.com/taxrates/en/state-rates/california/cities/san-francisco.html"

#r = requests.get(test_url)
#result = r.content
driver.get(test_url)

soup = BeautifulSoup(driver.page_source, "lxml")
print("1")

# it says dynamic, so I may need selenium
# state-profile--dynamic__entry
#chart = soup.find(class_="state-profile--dynamic__main")
#print(chart)

taxes = soup.find_all("div", class_="state-profile--dynamic__entry")
#print(taxes)

for item in taxes:
    #print("hello")
    t1 = item.find(class_="h6 state-profile--dynamic__entry__title")
    t2 = item.find(class_="h6 state-profile--dynamic__entry__value")
    print(t1)
    print(t2)

driver.quit()


#m = "california"
#c = "san-francisco"
#print(f"https://www.avalara.com/taxrates/en/state-rates/{m}/cities/{c}.html")
