from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

driver.get('https://www.google.com')

driver.save_screenshot("screenshot.png")

driver.quit()
display.stop()