from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def scrapingLogin():
    options = Options()
    
    # Google Chrome Canaryのインストールパスを指定する
    options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'

    # Headless Chromeを使うためのオプション
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    
    # 設定したオプションを使ってwebdriverオブジェクトを作成
    driver = webdriver.Chrome()

    # Google Chrome Canaryを起動してTwtitterのトップページに接続
    driver.get('https://twitter.com/')

    # あなたのユーザー名/メールアドレス
    username = 'keeitaidenwaa1995@gmail.com'
    # あなたのパスワード
    password = 'Kohasi123'

    # ユーザー名の入力ボックスを探す
    username_box = driver.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[1]/form/div[1]/input")
    # パスワードの入力ボックスを探す
    password_box = driver.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[1]/form/div[2]/input")

    # ユーザ名とパスワードをインプットする
    username_box.send_keys(username)
    password_box.send_keys(password)

    # ログインボタンを探す
    login_button = driver.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[1]/form/input[1]")
    #ログインボタンをクリック
    login_button.click()

    # プログラムが動いたと判断するための待機時間
    sleep(3)
    # ブラウザを閉じる
    #driver.close()
    # Google Chrome Canaryを終了する
    #driver.quit()

    return "Worked it"

def main():
    # scrapingLogin関数を実行
    output = scrapingLogin()
    print(output)

# プログラム実行のおまじない
if __name__ == '__main__':
    main()