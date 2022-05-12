from selenium import webdriver
from csv import reader
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
import chromedriver_binary



contact =[]
with open('contact.csv',"r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        contacts.append(row[0])
s = Service('C:/Aplikasi chrome driver/chromedriver.exe')
driver=webdriver.Chrome(service=s)   
driver.get("https://web.whatsapp.com/")

while True:
	for name in contacts:
		try:
			user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
			user.click()

			text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			text_box.send_keys("Hello ",name)

		    
			sendbtn= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
			sendbtn.click()
		except Exception as e:
			# print('Scrolling Your whatsapp Contacts')
			pass  
		else :
			print('Successfully message sent to',name)
			print(len(contacts)-1, 'more msgs left to send')
			contacts.remove(name)

	if(len(contacts)==0):
		break

driver.close()

