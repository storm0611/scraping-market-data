from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pandas as pd
from pandas import DataFrame


def get_name_by_id(id: str):

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument(
        #     "--user-data-dir=" + os.path.expanduser("~") + "\\AppData\\Local\\Google\\Chrome\\User Data")
        # chromedriver = "./chromedriver"
        # driver = webdriver.Chrome(executable_path=chromedriver,
        #                         chrome_options=chrome_options)
        try:
            driver = webdriver.Chrome()
        except:
            os.system("taskkill /im chrome.exe /f")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        
        driver.get("https://www.manpower.gov.kw/Pages/Services/TrainingRegister.aspx")

        driver.execute_script("document.body.style.zoom='100%'")
        
        id_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder1_TrainingRegisterUC_txtCivilID")))
        action = ActionChains(driver) 
        action.move_to_element(id_element).click().perform()
        id_element.send_keys(id)
        time.sleep(1)
        action.send_keys(Keys.ENTER).perform()

        name_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder1_TrainingRegisterUC_lblName")))
        name = name_element.text
        driver.close()
        driver.quit()
        return name


if __name__ == "__main__":
    df = pd.read_excel("id.xlsx", sheet_name="Sheet1")
    list_id = []
    list_name = []
    for id in df['ID']:
        name = get_name_by_id(str(id))
        time.sleep(3)
        list_id.append(str(id))
        list_name.append(str(name))
    df = DataFrame(list(zip(list_id, list_name)), columns=['ID', 'NAME'])
    df.to_excel("name.xlsx", sheet_name='Sheet1')
