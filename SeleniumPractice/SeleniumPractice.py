from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service("chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://sqengineer.com/practice-sites/practice-tables-selenium/")

table = browser.find_element(By.XPATH, "//table[@id='table1']")
rows = table.find_elements(By.TAG_NAME, "tr")
hcols = rows[0].find_elements(By.TAG_NAME, "th")

for i in range(1, len(rows)):
    cols = rows[i].find_elements(By.TAG_NAME, "td")
    for c in range(0, len(cols)):
        print(f"{hcols[c].text} : {cols[c].text}")
    print()
