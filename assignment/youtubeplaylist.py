from selenium import webdriver
driver=webdriver.Chrome()
def setup():
	
	driver.get("https://www.youtube.com")
	driver.maximize_window()
def login():
	signin=driver.find_element_by_class_name("yt-uix-button-content")
	signin.click()
	id=driver.find_element_by_id("Email")
	id.send_keys("jdfnjdf@gmail.com")
	next=driver.find_element_by_id("next")
	next.click()
	password=driver.find_element_by_id("Passwd")
	password.send_keys("dfjd")
	signin=driver.find_element_by_id("signIn")
	signin.click()
	driver.implicitly_wait(30)
def playvideo():
	try:
		menu=driver.find_element_by_css_selector("#appbar-guide-button > span > span")
		menu.click()
	except:
		print"Menu not found"
	driver.implicitly_wait(30)
	try:
		rhymes=driver.find_element_by_css_selector("#VLPL8AIZoZrs1JSTH6kXO6KnulHJiXVo-eF4-guide-item > a > span > span.display-name.no-count > span")
		rhymes.click()
	except:
		print "Rhymes playlist "
	try:
		playall=driver.find_element_by_css_selector("#pl-header > div.pl-header-content-container > div.pl-header-content-front > div.pl-header-content.privacy-icon-present > div.playlist-actions > a > span")
		playall.click()
	except:
		print "Playall button not found"
	print "Playing Nurseryrhyme"
	print driver.title

setup()
login()
playvideo()