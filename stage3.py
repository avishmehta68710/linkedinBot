from dependencies import *
from login import *
import config

df = pd.read_csv("roles_of_person_in_pervious_list.csv")
df.drop_duplicates(keep=False,inplace=True)
arr = list(df['Company_Name'])
names = list(df['Name'])
hitWords = ['full-time','part-time','internship','contract','crio.Do','girlscript foundation','girlscript summer of code','google summer of code','major league hacking','placementunit|bitspilani','highcommissionofcanadainindia','australiandepartmentofhomeaffairs','googlesummerofcode','majorleaguehacking','australiandepartmentofhomeaffairs','highcommissionofcanadainindia','britishrirways','resumevogue']
blockWords = ['placement','university','bachleors','college','institute','jecrc','daiict','student','ieee','dtu','self-employed','self','iit','da-iict','army','school','corona','mit','harvard','freelancing','freelancer','freelance','youtuber']
people = set()
for j in range(len(arr)):
    designation = " ".join(arr[j].split())
    flag = False
    if len(designation)>12:
        if designation[0:12].lower() == "company name":
            flag = True
            designation = designation.replace(designation[0:12],"")
    if flag == False and len(designation)>7:
        if (designation[0:7].lower() == "company"):
            designation = designation.replace(designation[:7],"")
    designation = designation.lower().split()
    checker = False
    for i in range(len(designation)):
        if designation[i] in blockWords:
            checker = True
            break
    s = ""
    if checker == False:
        if (designation[-1] in hitWords):
            designation = designation[:-1]
        if " ".join(designation) not in hitWords:
            people.add(" ".join(designation))
people = list(people)
count = 0
for j in range(len(people)):
    if count>99:
        break
    driver.get("https://www.linkedin.com/search/results/companies/?keywords="+str(people[j])+"&origin=GLOBAL_SEARCH_HEADER")
    src = driver.page_source
    parser = soup(src,"html.parser")
    userList = parser.find_all("li",{"class":"reusable-search__result-container"})
    if len(userList) != 0:
        links = userList[0].a['href']+"/people/"
        driver.get(links)
        time.sleep(10)
        src = driver.page_source
        parser = soup(src,"html.parser")
        time.sleep(4)
        user = parser.find_all("li",{"class":"grid grid__col--lg-8 pt5 pr4 m0"})
        print(len(user))
        count = 0
        for i in range(len(user)):
            count += 1
            print(i)
            time.sleep(2)
            src = driver.page_source
            parser = soup(src,"html.parser")
            WebDriverWait(driver,1000)
            try:
                connectRequest = driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width']").click()
                print(connectRequest)
                addNote = driver.find_element_by_xpath("//button[@class='mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view']")
                time.sleep(1)
                addNote.click()
                message = driver.find_element_by_xpath("//textarea[@class='ember-text-area ember-view connect-button-send-invite__custom-message mb3']")
                name = driver.find_element_by_xpath("//div[@class='org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view']").text
                print(name)
                message.send_keys(config.message)
                send = driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']")
                send.click()
            except:
                print(True)
                pass
    else:
        pass