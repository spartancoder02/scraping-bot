import requests 
from bs4 import BeautifulSoup
import re

url = "https://pythonjobs.github.io/jobs/"
page_list = ["hbk-strats-developer.html", "open-data-services-co-operative-python-software-developer.html", "oomnitza-back-end-sw-enginneer-irl-remote.html", "bmat-python-backend-engineer.html", "bmat-senior-backend-engineer.html"]

# loop thru the urls of diff pages
# print out the relevant info
# i.e:
# print out title from first page, email, appliction link
for i in range(0, len(page_list), 1):
    main_url = url + page_list[i]
    #print(main_url)
    resp = requests.get(main_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    job_title = soup.find("article").find("h1")
    print("Job Title:", job_title.text.strip(), end="\n")

    contact_elts = soup.find("article").find(class_="contact").find_all("div")#.find(string=" Email ")
  
    # # # print out all jobs, add 2 new lines @ end of job string
    for j in range(0, len(contact_elts), 1):
        link = contact_elts[j].find("a") # href="/jobs/hbk-strats-developer.html") #href="/jobs/hbk-strats-developer.html")

        if link != None and j == 1:
            # we extracted the email, print it out
            print("Email:", link.text.strip())
        elif link != None and j == 2:
            # we extracted the application link, print it out
            print("Application Link:", link.text.strip())

    print("\n"*2)
