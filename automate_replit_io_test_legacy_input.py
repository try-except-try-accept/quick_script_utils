from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from os import listdir
from time import sleep


testing = True

ACTION_TIME = 0.25
LINE_HEIGHT = 20

def wait_for_page(url):
     
     driver.get(url)

     timeout = 5
     try:
         element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
         WebDriverWait(driver, timeout).until(element_present)
     except TimeoutException:
         print("Timed out waiting for page to load")
     finally:
         print("Page loaded")

   

def find_and_click_html_elem(tag, attr, value):
     elems = driver.find_elements_by_tag_name(tag)
     for e in elems:
          if e.get_attribute(attr) is None:
               continue
          if value in e.get_attribute(attr):
               break
     else:
          raise Exception(f"Couldn't find html elem {tag} {attr} {value}")
     e.click()
     return e


driver = webdriver.Chrome("C:\\Users\\chall\\Desktop\\chromedriver_win32\\chromedriver.exe")
wait_for_page("https://replit.com")
find_and_click_html_elem("span", "textContent", "Log in")
sleep(2)
find_and_click_html_elem("span", "textContent", "Google")
sleep(2)
driver.switch_to.window(driver.window_handles[1])
element = find_and_click_html_elem("input", "type", "email")
element.send_keys(input("Enter Google email: "))
find_and_click_html_elem("button", "textContent", "ถัดไป")
sleep(2)
element = find_and_click_html_elem("input", "type", "password")
element.send_keys(input("Enter Google password: ")
find_and_click_html_elem("button", "textContent", "ถัดไป")
sleep(5)
driver.switch_to.window(driver.window_handles[0])


wait_for_page(input("Enter URL of repl.it teams for Edu project and navigate to the input/output matching test setup page:"))

   
input("Ready?")





i = 0

for fn in listdir():
     

   

     if fn.endswith(".in"):
          i += 1

          with open(fn, encoding="utf-8") as in_file:
               ins = in_file.readlines()
               
          with open(fn.replace(".in", ".out"), encoding="utf-8") as out_file:
               outs = out_file.readlines()


          find_and_click_html_elem("span", "textContent", "Create test")

          test_name = find_and_click_html_elem("input", "aria-label", "Test name")
          

          test_name.send_keys(fn.replace(".in", ""))

          inputs = find_and_click_html_elem("textarea", "placeholder", "The input for the test")

          for line in ins:
               inputs.send_keys(line)

          outputs = find_and_click_html_elem("textarea", "placeholder", "The expected")

          for line in outs:
               outputs.send_keys(line)


          test_name = find_and_click_html_elem("span", "textContent", "Save")

          sleep(1)
          
          print("Completed auto input of ", fn)
