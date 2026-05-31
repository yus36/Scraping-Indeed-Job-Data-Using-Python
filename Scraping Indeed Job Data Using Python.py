from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("https://in.indeed.com/jobs?q=data+scientist&l=Siliguri%2C+West+Bengal&from=searchOnHP%2Cwhereautocomplete&vjk=49bbeb894266779c")
    wait = WebDriverWait(driver, 25)

    Job_Titles= wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,  '[id^="jobTitle-"]')))
    all_Job_Titles = [j.text.strip() for j in  Job_Titles]


    Company_Names= wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,  '.css-19eicqx.eu4oa1w0')))
    all_Company_Names = [c.text.strip() for c in  Company_Names]

    Company_Locations= wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,  ".css-1f06pz4.eu4oa1w0")))
    all_Company_Locations = [l.text.strip() for l in  Company_Locations]


    all_data = pd.DataFrame({
    'Job Titles': all_Job_Titles,         # Use the cleaned text lists here!
    'Company Names': all_Company_Names,
    'Company Locations': all_Company_Locations
})

    print(all_data)
finally:
    driver.quit()



