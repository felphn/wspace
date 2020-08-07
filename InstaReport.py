from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system, getlogin
system('cls')
'''
May be useful:
= https://www.youtube.com/watch?v=BGU2X5lrz9M
= https://selenium-python.readthedocs.io/
= https://www.quackit.com/html/tags/html_li_tag.cfm
= https://stackoverflow.com/questions/28415029/how-to-get-a-list-of-the-li-elements-in-an-ul-with-selenium-using-python
= https://stackoverflow.com/questions/53681446/scroll-down-followers-following-list-in-the-instagram-box
= https://medium.com/better-programming/lets-create-an-instagram-bot-to-show-you-the-power-of-selenium-349d7a6744f7
= https://stackoverflow.com/questions/38040300/scraping-instagram-followers-page-using-selenium-and-python
'''
instaUser = '********'
instaPass = '********'

class instaReport():
    def __init__(self, userStr, passStr):
        self.userStr = userStr
        self.passStr = passStr
        self.driver = webdriver.Edge(executable_path=f'C:\\Users\\{getlogin()}\\Documents\\msedgedriver.exe')
    

    def logMeIn(self):
        self.driver.get('https://www.instagram.com/')
        sleep(.5)
        userInput = self.driver.find_element_by_xpath("//input[@name='username']")
        passInput = self.driver.find_element_by_xpath("//input[@name='password']")
        userInput.send_keys(self.userStr)
        passInput.send_keys(self.passStr)
        passInput.send_keys(Keys.RETURN)
        sleep(3.5)
        self.driver.get(f'https://www.instagram.com/{self.userStr}')


    def getFollowing(self):
        statInput = self.driver.find_element_by_xpath(f"//a[@href='/{self.userStr}/following/']")
        statInput.click()
        '''
        followPanel = self.driver.find_element_by_xpath(
            '//body/div[3]/div/div/div[2]/div'
        )
        '''
        followPanel = self.driver.find_elements_by_class_name('PZuss')
        print(followPanel)


InstaRep = instaReport(instaUser, instaPass)
InstaRep.logMeIn()
InstaRep.getFollowing()