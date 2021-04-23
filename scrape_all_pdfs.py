

import requests
from bs4 import BeautifulSoup as Soup

from shutil import copyfileobj
url = "https://www.google.com/search?q=Grade+thresholds+{}"


ALL_COURSES = ["9608"]

for year in range (2015, 2021, 1):

     for month in ["November", "June"]:

          for code in ALL_COURSES:

               result = requests.get(url.format("+".join([str(year),month,code])))

               link = [a['href'] for a in Soup(result.content).find_all('a') if "pdf" in a['href']][0]

               pdf_link = link[7:].split("&")[0]

               if "Images" in pdf_link:
                    fn = pdf_link.split("/Images/")[1]
               else:
                    fn = pdf_link.split("/images/")[1]

               try:
                    with open(fn, "wb") as f:
                         f.write(requests.get(pdf_link, stream=True).content)
               except Exception as e:
                    print(e)
                    print("Problem scraping", pdf_link)
                    pass
               
                            

               
