import time
from selenium import webdriver
videoFileName = "list.txt"
viewFileName = "viewCount.txt"
btnPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

videoFile = open(videoFileName,"r")
listVideo = videoFile.readlines()
videoFile.close()

Number_Of_Tab = 4
Number_Of_Video = len(listVideo)
Time_Loop = 3

videoIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0 

executable_path = "C:\webdrive\chromedriver.exe"
#open browser
browser = webdriver.Chrome(executable_path)
#open url 1st => tabIndec = 0
browser.get(listVideo[videoIndex])
#click play button
time.sleep(2)
playButton = browser.find_element_by_css_selector(btnPlaySelector)
playButton.click()
# #open new tab with 2nd video => tabIndex = 1
# time.sleep(0.5)
# videoIndex = videoIndex +1
# js = "window.open('"+listVideo[videoIndex].strip()+"')" 
# browser.execute_script(js)
# # go to previous tab and open new video
# time.sleep(2)
# tabIndex = 0
# handle = browser.window_handles[tabIndex]
# browser.switch_to.window(handle)
# videoIndex = videoIndex +1
# browser.get(listVideo[videoIndex])
while True:
    videoIndex = (videoIndex +1 ) % Number_Of_Video
    tabIndex = (tabIndex + 1) % Number_Of_Tab
    if tabCount < Number_Of_Tab:
        tabCount = tabCount +1
        browser.execute_script("window.open('"+listVideo[videoIndex].strip()+"')") 
    else:
        browser.switch_to.window(browser.window_handles[tabIndex])
        time.sleep(0.5)
        browser.get(listVideo[videoIndex])
    
    viewCount = viewCount +1
    saveFile = open(viewFileName,"w")
    saveFile.write(str(viewCount))
    saveFile.close()
    time.sleep(Time_Loop)    
