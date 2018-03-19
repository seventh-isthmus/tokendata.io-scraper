from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

csv_filename = "tokendata.csv"

driver = webdriver.Firefox()
sleep(5)
driver.get("https://www.tokendata.io/advanced")
assert "Token Data" in driver.title

csv_rows = []

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tr[5]"))
    )

    #Loads the text data from every line
    text = []
    rows = driver.find_elements_by_xpath("//tr")
    for r in rows:
        text.append(r.text)
    text.pop(0)
    text.pop(0)

    for t in text:
        name = t.split('$')[0].strip()
        t = t[len(name):].strip()
        USD_raised = t.split(" ")[0]
        t = t[len(USD_raised):].strip()
        Month = t.split('$')[0].strip()
        t = t[len(Month):].strip()
        Token_Sale_Price = t.split(" ")[0]
        t = t[len(Token_Sale_Price):].strip()
        Current_Token_Price = t.split(" ")[0]
        t = t[len(Current_Token_Price):].strip()
        Token_Return = t.split(" ")[0]
        t = t[len(Token_Return):].strip()
        ETH_Return = t.split(" ")[0]
        t = t[len(ETH_Return):].strip()
        BTC_Return  = t.split(" ")[0]
        t = t[len(BTC_Return):].strip()

        d = {'name':name, 'USD Raised':USD_raised, 'Month':Month, 'Token Sale Price': Token_Sale_Price, 'Current Token Price':Current_Token_Price, 'Token Return':Token_Return, 'ETH Return':ETH_Return, 'BTC Return':BTC_Return}
        csv_rows.append(d)



finally:
    driver.quit()

    with open(csv_filename, 'w') as csvfile:
        fieldnames = ['name', 'USD Raised', 'Month', 'Token Sale Price', 'Current Token Price', 'Token Return', 'ETH Return', 'BTC Return']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)
