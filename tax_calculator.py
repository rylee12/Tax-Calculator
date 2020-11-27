import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

PATH = "C:\Program Files (x86)\chromedriver.exe"
# Website: https://www.whatismybrowser.com/detect/what-is-my-user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"

options = Options()
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, executable_path=PATH)

# inputs
state = input("Enter the state you want the tax for: ")
local = input("Enter the city you want the tax for: ")
principle = input("Enter the amount you want to calculate: ")

# Get string ready
local = local.replace(" ", "-")
state = state.replace(" ", "-")

# Storage
tax_list = []
tax_desc = []

# Website string to parse
tax_url_x = f"https://www.avalara.com/taxrates/en/state-rates/{state.lower()}/cities/{local.lower()}.html"
#print(tax_url_x)

# Test website
test_url = "https://www.avalara.com/taxrates/en/state-rates/california/cities/san-francisco.html"
test_url_2 = "https://www.avalara.com/taxrates/en/state-rates/California/cities/San-Fran.html"

driver.get(tax_url_x)
soup = BeautifulSoup(driver.page_source, "lxml")

# Find the 404 Not Found message on the website
exception = soup.find(class_="ava-black font-weight-bold text-left")
if exception is not None:
    print("Page not Found.")
    print("Either the input you entered is not correct or the program is outdated")
else:
    taxes = soup.find_all("div", class_="state-profile--dynamic__entry")

    for item in taxes:
        t1 = item.find(class_="h6 state-profile--dynamic__entry__title")
        if t1 is None:
            t1 = item.find(class_="h6 w-75 float-left state-profile--dynamic__entry__title state-profile--dynamic__semi-bold")
        t2 = item.find(class_="h6 state-profile--dynamic__entry__value")
        if t2 is None:
            t2 = item.find(class_="h6 state-profile--dynamic__entry__value state-profile--dynamic__semi-bold")
        tax_desc.append(t1.text)
        tax_list.append(t2.text)

    print(tax_desc)
    print(tax_list)

    print("Breakdown of the sales tax in your area")

    for i in range(len(tax_list)):
        print(tax_desc[i], tax_list[i])

    # last element = total sales tax
    hello = tax_list[-1]
    hello = float(hello[:-1])
    principle = float(principle)
    subtax = principle * float(hello/100)
    total = subtax + principle
    print("The tax amount is: ", round(subtax, 2))
    print("The total amount you must pay is: ", round(total, 2))

driver.quit()