import pyautogui as pag
import time

speaker = pag.Point(206, 1045)
reset = pag.Point(210, 874)
reset2 = pag.Point(210, 844)

string = ['Chrome','VLC media player','Word','Microsoft Teams',
          'Reader DC','Zoom Webinar']

site = string[-1]
tw = pag.getWindowsWithTitle(site)
tw[0].maximize()

while True:
    
    tw[0].activate()
    init = pag.position()
    
    pag.moveTo(speaker, duration = 0.2)
    pag.leftClick(speaker)
    
    pag.moveTo(reset, duration = 0.2)
    pag.leftClick(reset)
    
    pag.moveTo(speaker, duration = 0.2)
    pag.leftClick(speaker)
    
    pag.moveTo(reset2, duration = 0.2)
    pag.leftClick(reset2)
    
    pag.moveTo(init, duration = 0.2)

    time.sleep(22)



