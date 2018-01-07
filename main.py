import network

import time

import ssd1306
from machine import I2C, Pin
i2c = I2C(sda=Pin(4), scl=Pin(5))
display=ssd1306.SSD1306_I2C(128,32,i2c,60)
display.fill(0)
display.show()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

authmode=["open","WEP","WPA-PSK","WPA2-PSK","WPA/WPA2-PSK","WPA/WPA2-Enterprise"]

while True:

    aps = sta_if.scan()
    display.fill(0)

    histchannel=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    histauth=[0,0,0,0,0,0]

    for ap in aps:
        display.text("SSID:"+str(ap[0])[2:-1],0,0,1)
        display.text("Channel:%d"%(ap[2]),0,8,1)
        histchannel[ap[2]-1] +=1
        display.text("RSSI:%0.1f"%(ap[3]),0,16,1)
        display.text("Mode:"+authmode[ap[4]],0,24,1)
        histauth[ap[4]]+=1
        display.show()
        time.sleep(1)
        display.fill(0)

    display.text("Open:%2d WEP:%2d" %(histauth[0],histauth[1]),0,0,1)
    display.text("WPA:%2d WPA2%2d" %(histauth[2],histauth[3]),0,8,1)
    display.text("WPA/WPA2-PSK:%2d" %histauth[4],0,16,1)
    display.text("WPA/WPA2-Ent:%2d" %histauth[5],0,24,1)
    display.show()

    time.sleep(10)

    display.fill(0)


    display.text(" 1 2 3 4 5 6 7",0,0,1)
    display.text("%2d%2d%2d%2d%2d%2d%2d" %(histchannel[0],histchannel[1],histchannel[2],histchannel[3],histchannel[4],histchannel[5],histchannel[6]),0,8,1)
    display.text(" 8 910111213",0,16,1)
    display.text("%2d%2d%2d%2d%2d%2d" %(histchannel[7],histchannel[8],histchannel[9],histchannel[10],histchannel[11],histchannel[12]),0,24,1)
    display.show()

    time.sleep(10)