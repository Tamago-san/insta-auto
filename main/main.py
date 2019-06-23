from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import random
import chromedriver_binary

#Webdriver
browser = webdriver.Chrome() #ここには任意のWebdriverを入れる

#URL
loginURL = "https://www.instagram.com/"
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"

#selectors
loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
likePath = "//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']" #未いいね時のcss
likeButtonPath = "//button[@class='dCJp8 afkep _0mzm-']"

mediaSelector = 'div._9AhH0'
nextPagerSelector = 'a.coreSpriteRightPaginationArrow'

#USER INFO
username = "osaka_tamasan"
password = "Kohasi123"

#params

base_tagName = "たまごサンド","玉子サンド","タマゴサンド","타마고산도"
#base_tagName=[]
add_tagName ="東京モーニング", "名古屋モーニング", "星乃珈琲店",\
            "carabinabreadstand", "コメダ珈琲", "嵜本", "乃が美", "レブレッソ", \
            "スタバ", "厚切りトースト", "コバトパン工場", "明日の食パン", "に志かわ", \
            "大阪ラーメン", "北新地ランチ", "パンとエスプレッソと", "大阪居酒屋",\
            "lebresso", "乃が美", "泉北堂", "route271","鳥貴族"


like_tag = 100
likedMax = 600 #規制されないように注意
tag_number=5
tagNames = list(base_tagName )+ random.sample(add_tagName, tag_number)



#初期化
WAIT_LIMIT = 3
iliked =0
liked =10
likedCounter01 = 0
likedCounter02 = 0
print(tagNames)
if __name__ == '__main__':

    #login
    browser.get(loginURL)
    time.sleep(3)
    browser.find_element_by_xpath(loginPath).click()
    time.sleep(3)
    usernameField = browser.find_element_by_name('username')
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_name('password')
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)

    for tagName in tagNames:
        #tag search
        time.sleep(3)
        likedCounter02 = 0
        iliked=0
        encodedTag = urllib.parse.quote(tagName)
        encodedURL = tagSearchURL.format(encodedTag)
        print("encodedURL:{}".format(encodedURL))
        browser.get(encodedURL)
    
        #media click
        time.sleep(3)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(mediaSelector).click()
    
        #次へボタンが表示されないか、いいねがlikedMax分いくまでいいねし続ける
        while likedCounter02 < like_tag and likedCounter01< likedMax:
            time.sleep(1)
            try:
 #               WebDriverWait(browser, WAIT_LIMIT).until(
 #                   expected_conditions.presence_of_all_elements_located((By.XPATH, likeButtonPath))
 #               )
                browser.find_element_by_xpath(likePath)
                browser.find_element_by_xpath(likeButtonPath).click()
                likedCounter01 += 1
                likedCounter02 += 1
                print("liked {}".format(likedCounter02), end='')
                print(" / allliked {}".format(likedCounter01))
            except:
                #読み込まれなかったり既にいいねしているならパス
                print("pass")
                iliked +=1
                if iliked>liked :
                    break
                pass
    
            #次へ
            try:
                browser.find_element_by_css_selector(nextPagerSelector).click()
            except:
                break

    print("You liked {} media".format(likedCounter01))
