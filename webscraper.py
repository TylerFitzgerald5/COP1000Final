# do NOT delete this. NOT MALICIOUS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By  

# Initialize Chrome driver instance
tier = "?format=" + input("Give tier/format")
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Navigate to the url

 
# Wait up to 10 seconds for the page to load (adjust as needed)  
WebDriverWait(driver, 30).until(  
    EC.presence_of_element_located((By.TAG_NAME, "body"))  # Wait for <body> tag  
)  

driver.get('https://replay.pokemonshowdown.com/' + tier)
links = []
releventSiteInfo = ""
websiteList = driver.page_source.split("\n")
for i in websiteList:
    if '<ul class="linklist">' in i:
        releventSiteInfo = i
        print("LINKS PROC")

print("<a href=\"gen9ou")
print("<a href=\"" + tier[8:])
substring = "<a href=\"" + tier[8:]
for i in range(55):
    #print("THIS LOOP IS RUNNING")
    nextLinkStart = releventSiteInfo.find(substring)
    #print(nextLinkStart)
    releventSiteInfo = releventSiteInfo[nextLinkStart + 9:] #Brings the start of the next link to the start of the relevent site information (since nothing else is relevent)
    nextLinkStop = releventSiteInfo.find('"') #Finds the next index of "
    link = releventSiteInfo[0:nextLinkStop]
    print(link)
    links.append(link)
    

# Close the driver
driver.quit()











