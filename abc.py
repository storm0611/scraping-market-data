from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def start_of_upload():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "--user-data-dir=C:\\Users\\HOPE\\AppData\\Local\\Google\\Chrome\\User Data")
    # chrome_options.add_argument('--profile-directory=Default')
    # chromedriver = "./chromedriver"
    # capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    # driver = webdriver.Chrome(executable_path=chromedriver,
    #                         chrome_options=chrome_options, desired_capabilities=capabilities)
    # driver = webdriver.Chrome(executable_path=chromedriver,
    #                           chrome_options=chrome_options)
    driver = webdriver.Chrome()

    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[-1])

    driver.get("https://www.idealista.com/en/alquiler-viviendas/madrid-madrid/")
    # time.sleep(3)
    elements = driver.find_elements(
        By.CSS_SELECTOR, "div.listing-title > h1")
    while not len(elements):
        elements = driver.find_elements(
            By.CSS_SELECTOR, "svg[aria-label='Your profile']")
    if len(elements):
        txt = elements[0].text.replace(',', '')
        print(txt)
        i = 0
        while not (txt[i] >= '0' and txt[i] <= '9'):
            i += 1
        txt = txt[i:]
        print(txt)
        i = 0
        while txt[i] >= '0' and txt[i] <= '9':
            i += 1
        print(int(txt[:i]))
        time.sleep(2)

    time.sleep(3)
    driver.close()
    driver.quit()
    time.sleep(3)

if __name__ == '__main__':
    start_of_upload()
