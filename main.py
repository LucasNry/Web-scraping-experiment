from selenium import webdriver
import time

userTeam = input("Qual time você deseja procurar: ")
browser = webdriver.Chrome("./chromedriver")

browser.get("http://www.google.com")
time.sleep(1)
searchbar = browser.find_element_by_class_name("gLFyf")
searchbar.send_keys(userTeam)
searchButton = browser.find_element_by_class_name("gNO89b")
time.sleep(1)
searchButton.click()
time.sleep(1)
expandButton = browser.find_element_by_class_name("PUDfGe")
time.sleep(1)
expandButton.click()
time.sleep(1)
results = []
teams = []
results_filtered = []
for score in browser.find_elements_by_class_name("imspo_mt__tt-w"):
    if(len(score.get_attribute('innerHTML')) < 8):
        results.append(score.get_attribute('innerHTML'))
# print(len(results))
sTeamScore = 1
for fTeamScore in range(0, len(results), 2):
    results_filtered.append([results[fTeamScore], results[sTeamScore]])
    sTeamScore += 2
for team in browser.find_elements_by_class_name("ellipsisize"):
    for name in team.find_elements_by_tag_name('span'):
        if name.get_attribute('innerHTML') != '' and len(name.get_attribute('innerHTML')) < 21 and len(teams) <= len(results):
            teams.append(name.get_attribute('innerHTML'))
browser.close()
second = 1
for first in range(0, len(results), 2):
    print(teams[first] + ": " + results[first])
    print(teams[second] + ": " + results[second])
    print("")
    second += 2
