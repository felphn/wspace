from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from os import name, system, getlogin
from time import sleep

# May be useful -> https://medium.com/better-programming/lets-create-an-instagram-bot-to-show-you-the-power-of-selenium-349d7a6744f7
# know issue -> after showing the following/followers dialog, we're getting only single scroll on the list.

if name == 'nt':
    system('cls')
else:
    system('clear')


class instaWatch():
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


    def getFollowing(self, totalFollowing):
        statInput = self.driver.find_element_by_xpath(f"//a[@href='/{self.userStr}/following/']")
        statInput.click()
        sleep(2.5)
        getFollowingList = self.driver.find_element_by_css_selector("div[role='dialog'] ul")
        numberOfFollowInList = len(getFollowingList.find_elements_by_css_selector("li"))
        getFollowingList.click()
        actionChain = webdriver.ActionChains(self.driver)
        while numberOfFollowInList < totalFollowing:
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowInList = len(getFollowingList.find_elements_by_css_selector("li"))
        followingList = []

        for user in getFollowingList.find_elements_by_css_selector("li"):
            userName = user.find_element_by_css_selector("a").get_attribute("title")
            sleep(.5)
            followingList.append(userName)
            if len(followingList) == totalFollowing:
                break
        #print(followingList)
        return followingList
    

    def getFollowers(self, totalFollowers):
        statInput = self.driver.find_element_by_xpath(f"//a[@href='/{self.userStr}/followers/']")
        statInput.click()
        sleep(2.5)
        getFollowersList = self.driver.find_elements_by_css_selector("div[role='dialog'] ul")
        numberOfFollowInList = len(getFollowersList.find_elements_by_css_selector("li"))
        getFollowersList.click()
        actionChain = webdriver.ActionChains(self.driver)
        while numberOfFollowInList < totalFollowers:
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowInList = len(getFollowersList.find_elements_by_css_selector("li"))
        followersList = []

        for user in getFollowersList.find_elements_by_css_selector("li"):
            userName = user.find_element_by_css_selector("a").get_attribute("title")
            sleep(.5)
            followersList.append(userName)
            if len(followersList) == totalFollowers:
                break
        #print(followersList)
        return followersList

    
    def compareLists(self, followingList, followersList):
        i = j = 0
        notFollowingBack = []
        while True:
            if followingList[i] == followersList[j]:
                i+=1
                j+=1
                if i == len(followingList):
                    break
            else:
                j+=1
                if j == len(followingList):
                    notFollowingBack.append(followingList[i])
                    i+=1
                    j=0

        for k in range(0, len(notFollowingBack)):
            print(f'{k}- {notFollowingBack[k]}\n')
        

instaUser = '******'
instaPass = '******'

InstaWatch = instaWatch(instaUser, instaPass)
InstaWatch.logMeIn()
followingList = InstaWatch.getFollowing(999999)
followersList = InstaWatch.getFollowers(999999)
InstaWatch.compareLists(followingList, followersList)
