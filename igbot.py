from selenium import webdriver
from time import sleep

class Instabot:
	def __init__(self, username,pw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(2)

		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)      #input username in the username column
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)            #input password in the password column
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()  #click login button
		sleep(5)
		self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()   #click not now button
		sleep(5)
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username)).click()  #click on the profile button
		sleep(5)
		
		#FOLLOWING
		self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click() #click on thr following botton
		sleep(5)

		#finding the heigth of the scroll box and then running the script to scroll down to the bottom of the list.
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)
		
		links = scroll_box.find_elements_by_tag_name('a')
		following = [name.text for name in links if name.text != '']
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
		sleep(2)
		#print("FOLLOWING \n")
		#print(following)
		

		#FOLLOWERS
		self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click() #click on thr followers botton
		sleep(5)

		#finding the heigth of the scroll box and then running the script to scroll down to the bottom of the list.
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)
		
		links = scroll_box.find_elements_by_tag_name('a')
		followers = [name.text for name in links if name.text != '']
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
		sleep(2)
		#print("FOLLOWERS \n")
		#print(followers)


		not_following_back = [user for user in following if user not in followers]
		print("NOT FOLLOWING BACK \n")
		print(not_following_back)



Instabot('username','password') # put your username and password to make it work.

