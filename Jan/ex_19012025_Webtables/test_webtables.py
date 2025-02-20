from selenium import webdriver

from selenium.webdriver.common.by import By

def test_webtable():

   driver=webdriver.Chrome()
   driver.get("https://cosmocode.io/automation-practice-webtable/")
   driver.maximize_window()
   row=driver.find_elements(By.XPATH,"//table[@id='countries']/tbody/tr")
   row_length=len(row)
   print(row_length)

   column=driver.find_elements(By.XPATH,"//table[@id='countries']/tbody/tr[2]/td")
   column_len=len(column)

   print(column_len)

   fp="//table[@id='countries']/tbody/tr["
   sp="]/td["
   tp="]"
   # To print all the table values
   for i in range(2,row_length+1):
      for j in range(1,column_len+1):
         path=f"{fp}{i}{sp}{j}{tp}"
         data=driver.find_element(By.XPATH,path).text
         #print(data)

         #To print the capital of austria
         if "Austria" in data:
            capital_path=f"{path}/following-sibling::td"
            capital_text=driver.find_element(By.XPATH,capital_path).text
            print(f"Capital of Austria is {capital_text}")



