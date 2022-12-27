#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Edge()

#open the webpage
driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
time.sleep(random.randint(2,3))
username.send_keys("igorladeia__")
password.clear()
time.sleep(random.randint(3,4))
password.send_keys("Igor.ladeia12")
time.sleep(random.randint(4,5))

#target the login button and click it
try:
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
except Exception as error:
    print("usuario ou senha errados")
    driver.close()
    pass

time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()

#target the search input field
# searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
# searchbox.clear()
#FIXING THE DOUBLE ENTER
# time.sleep(5) # Wait for 5 seconds
# my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
# my_link.click()



instagram = 'scaniagroup'
driver.get(f'https://www.instagram.com/{instagram}/')
time.sleep(4)

# print(web.page_source)
# print('---------------------**\n')
# print(web.title)
# print('---------------------**\n')
# print(web.current_url)
# print('---------------------**\n')

n_scrolls = 4
final_anchors = []
for j in range(0, n_scrolls):
    #target all the link elements on the page
    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

    try:
        final_anchors.extend(anchors)
    except:
        pass

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


    # for lin in final_anchors:
    #     new

final_anchors = list(set(final_anchors))
print(final_anchors)
print('Found ' + str(len(anchors)) + ' and '+ str(len(final_anchors)) + ' links to images')
anchors[:5]

for i in range (10):
    driver.get(final_anchors[random.randint(0,len(final_anchors)-1)])
    # button = WebDriverWait(driver, 2).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[3]/div/div/section[1]/span[1]/button/div[2]/span/svg"))).click()

    try:
        driver.find_element_by_css_selector(
            "#react-root > section > main > div > div.ltEKP > article > div > "
            "div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button > "
            "div.QBdPU.rrUvL > span > svg:nth-child(1)[aria-label='Curtir'").click()
        time.sleep(random.randint(19, 23))
    except Exception as e:
        print(e)
        time.sleep(5)