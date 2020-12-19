from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from your_creds import g_mail,g_mail_pw
from time import sleep


pickUpLoc = input('What is your pick-up location? ')
dropLoc = input("Enter drop location: ")

#opening uber login page
driver=webdriver.Chrome()
driver.delete_all_cookies()
driver.get(f'https://auth.uber.com/login/?breeze_local_zone=dca1&next_url=https%3A%2F%2Fm.uber.com%2F%3F_ga%3D2.45510756.1912739501.1588420391-285597623.1588420391&state=PaWCeYnQhIO1baS0k4N0LzWa1QzpT6RN2040fabrQD0%3D')


#choosing a social acc to login
soc_acc = driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div/div/div/div/div[2]/div/a/div')
soc_acc.click()
sleep(1)
uberHandle=driver.window_handles[0]


#login in with google acc
goog_acc = driver.find_element_by_xpath('//*[@id="googleLoginButton"]/div/div[2]')
goog_acc.click()
googHandle = driver.window_handles[1]


#login process
driver.switch_to_window(googHandle)
googSearchBox = driver.find_element_by_xpath('//*[@id="identifierId"]')
googSearchBox.send_keys(g_mail)
sleep(2)

nextButton1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
nextButton1.click()
sleep(2)

googPassBox = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
googPassBox.send_keys(g_mail_pw)
sleep(1)

nextButton2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
sleep(1)
nextButton2.click()


#back to uber
driver.switch_to_window(uberHandle)


#entering the pick up location

pickUpSearchBox = driver.find_element_by_xpath('//*[@id="booking-experience-container"]/div/div[3]/div[2]/div/div/div[1]/div/input')
pickUpSearchBox.send_keys(pickUpLoc)
sleep(5)
pickUpBar = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div/div[2]')
pickUpBar.click()
sleep(2)


#entering the drop location

dropSearchBox = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div/input')
sleep(4)
dropSearchBox.send_keys(dropLoc)
sleep(1)
dropBar = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]')
dropBar.click()


print("Your ride has been booked.")
