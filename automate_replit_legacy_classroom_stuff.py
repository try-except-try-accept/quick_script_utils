from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

     
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




KEYS = Keys()

from os import listdir, path, getcwd, environ
from time import sleep

from importlib import import_module

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
     try:
          e.click()
     except Exception as error:
          print(error)
          print("Found it, but couldn't click this element.")
     return e




     
def replit_login():
     username = environ.get("google_user")
     password = environ.get("google_pass")
     wait_for_page("https://replit.com")
     find_and_click_html_elem("span", "textContent", "Log in")
     sleep(2)
     find_and_click_html_elem("span", "textContent", "Google")
     sleep(2)
     driver.switch_to.window(driver.window_handles[1])
     element = find_and_click_html_elem("input", "type", "email")
     if not username:
          username = input("Enter Google email: ")
     element.send_keys(username)
     find_and_click_html_elem("button", "textContent", "ถัดไป")
     sleep(2)
     element = find_and_click_html_elem("input", "type", "password")
     if not password:
          password = input("Enter Google password: ")
     element.send_keys(password)
     find_and_click_html_elem("button", "textContent", "ถัดไป")
     sleep(5)
     driver.switch_to.window(driver.window_handles[0])

def replit_go_to_assignment():
     wait_for_page(input("Enter URL of repl.it teams for Edu project and navigate to the input/output matching test setup page:"))   
     input("Ready?")
     EX_TEST_PATH = "C:\\Users\\chall\\Google Drive\\Python\\repl_scrape\\II_-_Selection\\II_-_Selection - Input_Output Matching.py"


def iterate_assignments():

     for folder in listdir():
          if path.isdir(folder) and "actual_export" not in folder:

               print(folder)


               scrape_path = getcwd()+"\\"+folder

               for export_folder in listdir("actual_export"):

                    export_strip = export_folder.replace(",", "").replace("&", "")

                    if all(chunk in folder for chunk in export_strip.split("_")):

                         break

               else:
                    print(f"Export folder not found for {folder}")
                    export_folder = input("Enter export folder name: ")

               export_path = getcwd()+"\\actual_export\\"+export_folder    

               
               print(get_test_type(scrape_path, export_path))
               print()

def get_test_type(scrape_path, export_path):

     for f in listdir(scrape_path):   
          if "Unit_Tests" in f:
               return scrape_path + "\\" + f


     
     for f in listdir(export_path):   
          if "input-output matching" in f:
               return export_path + "\\" + f
         
     print(f"No tests found")
     return None


def create_assignment(title, description):

     wait_for_page("https://replit.com/team/bkkprep2122")

     print("Please can you close the modal?")
     input()
     find_and_click_html_elem("span", "textContent", "Create project")
     sleep(3)     
     field = find_and_click_html_elem("input", "placeHolder", "Title")
     field.send_keys(title)
     field = find_and_click_html_elem("textarea", "placeHolder", "Description")
     field.send_keys(descrption)
     find_and_click_html_elem("span", "textContent", "This project is only accessible by team admins until it is published.")
     sleep(1)
     
     e = find_and_click_html_elem("button", "class", "jsx-4103319877")


def write_to_replit_editor(text_editor, data):
     tabwidth = 0
     last_tabwidth = None
     
     for line in data:
          if line.startswith("\t"):                         # found an indented line
               count = 0
               for index, char in enumerate(line):          # iterate through the chars
                    if char == "\t":                        # found a tab
                         count += 1
                    else:                                   # found end of indent
                         break
               tabwidth = count                             # store tab width
          else:
               tabwidth = 0


          if last_tabwidth is None:                         # it's the first line
               text_editor.send_keys(line)                  # so just write the line
          elif tabwidth == last_tabwidth:               
               text_editor.send_keys(line.strip()+"\n")     # if it's the same tab width, no indents are needed.       
          else:
               for i in range(last_tabwidth):               # remove all existing tabs
                    text_editor.send_keys(KEYS.BACKSPACE)
               text_editor.send_keys(line)                  # and write the line


          last_tabwidth = tabwidth
          

          
         
def add_starter_code_and_instructions(starter_code, instructions):

     # add starter code
     sleep(3)
     text_editor = find_and_click_html_elem("textarea", "class", "inputarea")
     
     with open(starter_code, encoding="utf-8") as f:
          write_to_replit_editor(text_editor, f)
          
     

     # add instructions markdown file
     find_and_click_html_elem("div", "class", "jsx-1317030708")
     filename_field = driver.switch_to.active_element
     filename_field.send_keys('instructions.md')
     filename_field.send_keys(KEYS.RETURN)
     sleep(3)
     text_editor = driver.switch_to.active_element

     with open(instructions, encoding="utf-8") as f:
          write_to_replit_editor(text_editor, f)
     
     


def automate_io_test_input(test_path):

     i = 0     

          
     for fn in listdir(test_path):

          if fn.endswith(".in"):
               i += 1

               with open(test_path+"/"+fn, encoding="utf-8") as in_file:
                    ins = in_file.readlines()
                    
               with open(test_path+"/"+fn.replace(".in", ".out"), encoding="utf-8") as out_file:
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

     print(f"Imported {i} tests")



driver = webdriver.Chrome("C:\\Users\\chall\\Desktop\\chromedriver_win32\\chromedriver.exe")
action = ActionChains(driver)

replit_login()

wait_for_page("https://replit.com/@bkkprep2122/Assignment-title")
sleep(5)
find_and_click_html_elem("button", "class", "jsx-3179763061")
starter_code = r"C:\Users\chall\Google Drive\Python\repl_scrape\actual_export\V_-_Definite_Iteration\main.py"
instructions = r"C:\Users\chall\Google Drive\Python\repl_scrape\V_-_Definite_Iteration\V_-_Definite_Iteration_instructions.md"

add_starter_code_and_instructions(starter_code, instructions)
