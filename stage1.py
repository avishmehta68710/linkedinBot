from dependencies import *
import login
import config

headers = ["Name", "ProfileLinks", "current_designation", "current_location"]
filename = "names_and_positions.csv"
File = open(filename,'a')
writer_object = writer(File)
writer_object.writerow(headers)

companies_list = config.companies_list

for j in range(len(companies_list)):
    login.driver.get("https://www.linkedin.com/search/results/people/?keywords="+companies_list[j]+"&origin=SWITCH_SEARCH_VERTICAL")
    src = login.driver.page_source
    htmlParser = soup(src,"html.parser")
    content = htmlParser.find_all("li",{"class":"reusable-search__result-container"})
    for i in range(len(content)):
        try:
            name = content[i].find("div",{"class":"display-flex align-items-center"}).img['alt']
        except:
            name = content[i].find("span",{"class":"entity-result__title-text t-16"}).a.text
        name = name.replace("\n","").replace(",","|").strip(" ")
        profile_links = content[i].find("div",{"class":"display-flex align-items-center"}).a['href']
        profile_links = profile_links.replace("\n","").replace(",","|")
        current_designation = content[i].find("div",{"class":"entity-result__primary-subtitle t-14 t-black"}).text
        current_designation = current_designation.replace("\n","").replace(",","|")
        current_location = content[i].find("div",{"class":"entity-result__secondary-subtitle t-14"}).text
        current_location = current_location.replace("\n","").replace(",","|")
        current_designation = current_designation.replace("\n","").replace(",","|").strip(" ")
        data = [name,profile_links,current_designation,current_location]
        writer_object.writerow(data)
File.close()