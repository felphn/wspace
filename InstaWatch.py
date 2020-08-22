from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count
from explicit.waiter import find_element
from os import name, system, getlogin, sep
from os.path import abspath
from time import sleep


def clearDisplay():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def logIn(driver, instUser, instPass):
    driver.get('https://www.instagram.com/')
    sleep(1.5)
    findField = driver.find_element_by_xpath("//input[@name='username']")
    findField.send_keys(instUser)
    findField = driver.find_element_by_xpath("//input[@name='password']")
    findField.send_keys(instPass)
    findField.send_keys(Keys.RETURN)
    sleep(15.0)
    driver.get(f'https://www.instagram.com/{instUser}')
    clearDisplay()
    print(f'> Watching "{instUser}" profile.\n')


def getFollowg(driver, instUser):
    findField = driver.find_element_by_xpath(f"//a[@href='/{instUser}/following/']")
    findField.click()
    print('> Catching usernames in "Following" list ...')
    sleep(2.5)
    getFollowingCSS = 'ul div li:nth-child({}) a.notranslate'
    for listedUsers in count(start=1, step=12):
        for usrIndex in range(listedUsers, listedUsers+12):
            yield find_element(driver, getFollowingCSS.format(usrIndex)).text
        lastUserListed = find_element(driver, getFollowingCSS.format(usrIndex))
        driver.execute_script("arguments[0].scrollIntoView()", lastUserListed)


def getFollowr(driver, instUser):
    driver.get(f'https://www.instagram.com/{instUser}')
    findField = driver.find_element_by_xpath(f"//a[@href='/{instUser}/followers/']")
    findField.click()
    print('> Catching usernames in "Followers" list ...')
    sleep(2.5)
    getFollowerCSS = 'ul div li:nth-child({}) a.notranslate'
    for listedUsers in count(start=1, step=12):
        for usrIndex in range(listedUsers, listedUsers+12):
            yield find_element(driver, getFollowerCSS.format(usrIndex)).text
        lastUserListed = find_element(driver, getFollowerCSS.format(usrIndex))
        driver.execute_script("arguments[0].scrollIntoView()", lastUserListed)


def watchLists(driver, instUser, totalFollowing, totalFollowers):
    k = 0
    followingList = []
    followersList = []
    notFollowingBack = []
    try:
        sleep(7.5)
        try:
            for i, usr in enumerate(getFollowg(driver, instUser), 1):
                #print(f'({i})- {usr}')
                k = i
                followingList.append(usr)
                if i >= totalFollowing:
                    break
        except Exception as e:
            #print(e)
            pass
        if k < totalFollowing:
            print(f'> {totalFollowing-k} user(s) not found.\n> {k} username(s) appended.\n')
        else:
            print(f'> {k} username(s) appended.\n')

        sleep(7.5)
        try:
            for i, usr in enumerate(getFollowr(driver, instUser), 1):
                #print(f'({i})- {usr}')
                k = i
                followersList.append(usr)
                if i >= totalFollowers:
                    break
        except Exception as e:
            #print(e)
            pass
        if k < totalFollowers:
            print(f'> {totalFollowers-k} user(s) not found.\n> {k} username(s) appended.\n')
        else:
            print(f'> {k} username(s) appended.\n')

        sleep(2.5)
        print('> Iterating over lists ...\n')
        sleep(5.0)
        for j in range(0, len(followingList)):
            if followingList[j] not in followersList:
                notFollowingBack.append(followingList[j])

        clearDisplay()
        print('-'*34, '\n> Not following you back:\n')
        for k in range(0, len(notFollowingBack)):
            print(f'({k+1})- {notFollowingBack[k]}')
        print('\n')

    finally:
        driver.quit()


clearDisplay()
print('='*8, '<> InstaWatch <>', '='*8)
print(' '*7, 'written by felpshn')
instUser = str(input('\n> Username: '))
instPass = str(input('> Password: '))
totalFollowing = int(input('\n> Num of users that you follow: '))
totalFollowers = int(input('> Num of users that follows you: '))
sleep(2.5)
print('-'*34, '\n> Done!\n> Starting browser ...')
print('-'*34)
if name == 'nt':
    driver = webdriver.Edge(executable_path=f"{abspath(sep)}Users\\{getlogin()}\\Documents\\msedgedriver")
else:
    driver = webdriver.Firefox(executable_path=f"/home/{getlogin()}/Documents/geckodriver")
logIn(driver, instUser, instPass)
watchLists(driver, instUser, totalFollowing, totalFollowers)
system('pause')
