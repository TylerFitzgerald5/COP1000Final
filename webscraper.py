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
links = "No links found"
websiteList = driver.page_source.split("\n")
for i in websiteList:
    if '<ul class="linklist">' in i:
        links = i
        print("LINKS PROC")

print(links)
# Close the driver
driver.quit()
#tier = "?format=" + input("Give tier/format")
#website = requests.get("https://replay.pokemonshowdown.com/")










