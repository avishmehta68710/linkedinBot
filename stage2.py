from dependencies import *
from login import *

df = pd.read_csv("try.csv")
profileLinks = df['ProfileLinks']
names = df['Name']

headers = ["Name", "Company_Name", "Duration", "Information"]
filename = "roles_of_person_in_pervious_list.csv"
File = open(filename,'a')
writer_object = writer(File)
writer_object.writerow(headers)

count = 0
for j in range(len(profileLinks)):
    if count>999:
        break
    print(profileLinks[j])
    driver.get(profileLinks[j])
    try:
        driver.find_element_by_xpath("//button[@class='pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted']").click()
    except:
        pass
    src = driver.page_source
    parser = soup(src,"html.parser")
    profiles = parser.find_all("li",{"class":"pv-entity__position-group-pager pv-profile-section__list-item ember-view"})
    for i in range(len(profiles)):
        count += 1
        name = names[j]
        try:
            company_name = profiles[i].find("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"}).find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text
            company_name = company_name.replace("\n","").strip(" ").replace(",","|").replace("None","")
        except:
            try:
                company_name = profiles[i].find("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section"}).find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text
                company_name = company_name.replace("\n","").strip(" ").replace(",","|").replace("None","")
            except:
                company_name = profiles[i].find("div",{"class":"pv-entity__company-summary-info"}).h3.text
                company_name = company_name.replace("\n","").strip(" ").replace(",","|")
        try:
            duration = (profiles[i].find("div",{"class":"display-flex"}).find("h4",{"class":"t-14 t-black--light t-normal"}).find("span",{"class":"pv-entity__bullet-item-v2"}).text)
            duration = duration.replace("\n","").strip(" ").replace(",","|").replace("None","")
        except:
            try:
                duration = profiles[i].find("div",{"class":"pv-entity__company-summary-info"}).h4.text
                duration = duration.replace("\n","").strip(" ").replace(",","|")
            except:
                duration = ""
        try:
            info = (profiles[i].find("div",{"class":"pv-entity__extra-details t-14 t-black--light ember-view"}).text)
            info = info.replace("\n","").strip(" ").replace(",","|").replace("None","")
        except:
            info = ""
        data = [name,company_name,duration,info]
        writer_object.writerow(data)
File.close()