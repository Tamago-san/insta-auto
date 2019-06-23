from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.parse
import time
import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Webdriver
#non headless
browser = webdriver.Chrome() #ここには任意のWebdriverを入れる
#headless
#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#browser = webdriver.Chrome(options=options)
##

#executable_path='/mnt/c/workspace/pydev/chromedriver.exe'
#URL
WAIT_LIMIT = 20 #Wait limit
PAGING_WAIT_SEC = 1 #Paging wait time
loginURL = "https://www.instagram.com/" #ログインする際のページ
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja" #.format()で{}の中の値を入れられるようになっている

#TagSearchたまごサンド

tagName = "たまごサンド" #タグの名前 #大阪カフェ
#tagName = "大阪カフェ" #タグの名前 #大阪カフェ
#tagName = "大阪グルメ"
#tagName = "玉子サンド"
#tagName = "タマゴサンド"
#tagName = "東京モーニング"
#tagName = "名古屋モーニング"
#tagName = "星乃珈琲店"
#tagName = "carabinabreadstand"
#tagName = "コメダ珈琲"
#tagName = "嵜本"
#tagName = "乃が美"
#tagName = "レブレッソ"
#tagName = "スタバ"
#tagName = "厚切りトースト"
#tagName = "コバトパン工場"
#tagName = "明日の食パン"
#tagName = "に志かわ"
#tagName = "ラーメン女子"
#tagName = "大阪ラーメン"
#tagName = "北新地ランチ"
#tagName = "パンとエスプレッソと"
#tagName = "大阪居酒屋"
#tagName = "lebresso"
#tagName = "乃が美"
#tagName = "泉北堂"
#tagName = "route271"
#tagName = "サンドイッチの日"



#selectors
labelsXpath = '//label'
loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a' #xpath @https://www.instagram.com/
usernamePath = '#f276fbf946136f8' #xpath @https://www.instagram.com/
passwordPath = '//*[@id="f301d5bacf10de4"]' #xpath @https://www.instagram.com/

notNowPath = '//*[@id="react-root"]/div/div[2]/a[2]'

firstArticleXpath = '//article/div[1]/div[1]/div[1]/div[1]/div[1]/a'
#firstArticleXpath = '//article/div[1]/div/div/div[1]/div[2]/a'
#//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a
#//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div[1]/div[1]/img
#//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]/a/div[1]
#//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[3]/a
#likeXpath = '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/a[1]'
#nextPagerSelector = '/html/body/div[2]/div[2]/div/article/div[1]/div/div/div/div[2]/button/div' #次へボタン

likeButtonSelector = 'button.coreSpriteHeartOpen'
likeXpath = '//button/span[contains(@class,\'glyphsSpriteHeart__outline\')]'
likedXpath = '//button/span[contains(@class,\'glyphsSpriteHeart__filled\')]'
nextPagerSelector = 'a.coreSpriteRightPaginationArrow'
tagXpath="/html/body/div[2]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span/"
#body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button

#USER INFO
time.sleep(3)
username = "osaka_tamasan"
password = "Kohasi123"

#list

mediaList = []

#counter
likedCounter = 0

if __name__ == '__main__':

    #Login
    browser.get(loginURL)
    time.sleep(3)
    browser.find_element_by_xpath(loginPath).click()
    time.sleep(2)
    labelsField = browser.find_elements_by_xpath(labelsXpath)
    usernameField = browser.find_element_by_xpath("//*[@id=\"" + labelsField[0].get_attribute("for") + "\"]")
#f7b9308995e0a
#f1824ab673636fc
#//*[@id="f228ca382b2e2dc"]
    print(labelsField[0].get_attribute("for"))
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_xpath("//*[@id=\"" + labelsField[1].get_attribute("for") + "\"]")
    print(labelsField[1].get_attribute("for"))
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)

    #Finished logging in. now at
    time.sleep(3)
    encodedTag = urllib.parse.quote(tagName) #普通にURLに日本語は入れられないので、エンコードする
    encodedURL = tagSearchURL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)

    #Finished tag search. now at https://www.instagram.com/explore/tags/%E8%AA%AD%E5%A3%B2%E3%83%A9%E3%83%B3%E3%83%89/?hl=ja
    time.sleep(3)
    browser.implicitly_wait(10)

    #写真を取得してクリックする

 #   mediaList = browser.find_elements_by_css_selector(mediaSelector)
 #   mediaCounter = len(mediaList)

    firstArticle= browser.find_elements_by_xpath(firstArticleXpath)
#    mediaCounter = len(mediaList)
    firstArticle[0].click()
#    print("Found {} media".format(mediaCounter))

    #Loop while next button exist
    likedCounter = 0
#    while True:
    while likedCounter<400:
        browser.implicitly_wait(PAGING_WAIT_SEC)
        try:
            try:
                #Wait display like button.
                print("now")
#               time.sleep(2)
                WebDriverWait(browser, WAIT_LIMIT).until(
                    expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, likeButtonSelector))
                )
                browser.find_element_by_xpath(likeXpath).text
                #browser.find_element_by_css_selector(likeButtonSelector).click()
                browser.find_element_by_css_selector(likeButtonSelector).click()
                a=browser.find_element_by_css_selector(likeButtonSelector)
                print(a)
                #browser.findElement(By.className("dCJp8 afkep _0mzm-")).click();
                #Wait like status changed.
                WebDriverWait(browser, WAIT_LIMIT).until(
                    expected_conditions.presence_of_all_elements_located((By.XPATH, likedXpath))
                )
#                time.sleep(2)
                likedCounter += 1
                print("liked {} ".format(likedCounter))
                
            except NoSuchElementException as e1:
#                print(e1)
                print("already liked article")

            tagsuu=browser.find_element_by_class_name("C4VMK")
            hashtag=tagsuu.find_elements(By.TAG_NAME,"a")
#            print(hashtag)
            
            nextUrl = browser.find_element_by_css_selector(nextPagerSelector).get_attribute("href")
            browser.find_element_by_css_selector(nextPagerSelector).click()
            time.sleep(3)

        except Exception as e2:
            print(e2)
            break

    print("You liked {} media".format(likedCounter))

 #   for media in mediaList:
 #       media.click()
#
 #       # 次へボタンが表示されるまで
 #       while True:
 #           try:
 #               time.sleep(3)
 #               browser.find_element_by_xpath(likeXpath).click()
 #               browser.implicitly_wait(10)
 #               likedCounter += 1
 #               print("liked {} of {}".format(likedCounter,mediaCounter))
 #               browser.find_element_by_css_selector(nextPagerSelector).click()
 #               print("next")
 #           except:
 #               break #もう次へボタンが存在しない場合、エラーをはくのでそこで終了
 #       break #for文自体も終了させる
#
 #   print("You liked {} media".format(likedCounter))##