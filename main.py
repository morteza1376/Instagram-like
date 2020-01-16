from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# This line Load Chrome Driver
# for my system, this code is commented below
# driver = webdriver.Chrome('/home/morteza/python/Instagram-like/chromedriver')
driver = webdriver.Chrome('*YOUR_CHROME_DRIVER_PATH*')

driver.get('https://www.instagram.com/accounts/login')


username = '*YOUR_INSTAGRAM_ACCOUNT_USERNAME*'
password = '*YOUR_INSTAGRAM_ACCOUNT_PASSWORD*'

# The ID of instagram account that you want to make full like
# page = 'morteza.gh1998'
page = '*INSTAGRAM_ACCOUNT_ID_WITHOUT_@*'

username_element = driver.find_element_by_name('username')
password_element = driver.find_element_by_name('password')

submit_element = driver.find_elements_by_css_selector('button[type="submit"]')[0]

username_element.send_keys(username)
password_element.send_keys(password)

submit_element.click()


time.sleep(5)

driver.get("https://www.instagram.com/" + page)
time.sleep(5)

all_post_count = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span')
first_post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article[2]/div/div/div/div[1]')
first_post.click()
time.sleep(5)

post_counts = int(all_post_count.text)
print('There Are ' + str(post_counts) + 'posts!')
i = 0
while(True):
    print('I want to like Post #' + str(i + 1))
    like_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    like_button.click()

    next_button = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
    if(i > 0 and i != (post_counts -1)):
        next_button = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
    next_button.click()
    i += 1
    print('Liked!')
    time.sleep(1)
    if((i) == post_counts):
        os.system('notify-send -i face-wink "All Posts Liked!"')
        break

driver.close()


