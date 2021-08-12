# Webdriver Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Misc Imports
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://omicron.life/")
a = driver.find_element_by_link_text("About Omicron")
b = driver.find_element_by_link_text("Depression Detection")

i = 0
try:
    while True:
        a.click()
        i += 1
        print(i)
        time.sleep(2)
        b.click()
        i += 1
        print(i)
        time.sleep(2)

except KeyboardInterrupt:
    print("Bot Stopped")
    pass