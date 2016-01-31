import ImageGrab, Image, ImageOps
import os
import time
import win32api, win32con
from numpy import *
import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,200,0)
# Globals
# ------------------
 
x_pad = 749
y_pad = 227
tileMouseLocations = {'t1':(x_pad+52, y_pad+75),
            't2':(x_pad+152, y_pad+75),
            't3':(x_pad+252, y_pad+75),
            't4':(x_pad+352, y_pad+75),
            't5':(x_pad+52, y_pad+225),
            't6':(x_pad+152, y_pad+225),
            't7':(x_pad+252, y_pad+225),
            't8':(x_pad+352,y_pad+225),
            't9':(x_pad+52,y_pad+375),
            't10':(x_pad+152,y_pad+375),
            't11':(x_pad+252,y_pad+375),
            't12':(x_pad+352,y_pad+375),
            't13':(x_pad+52,y_pad+525),
            't14':(x_pad+152,y_pad+525),
            't15':(x_pad+252,y_pad+525),
            't16':(x_pad+352,y_pad+525)}
# ------------------
def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+401, y_pad+601)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\game_snap' + str(int(time.time())) +
'.png', 'PNG')


def get_tile_one():
    box = (x_pad+2,y_pad+5,x_pad+101,y_pad+150)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 1 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]

def get_tile_two():
    box = (x_pad+102,y_pad+5,x_pad+201,y_pad+150)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 2 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_three():
    box = (x_pad+202,y_pad+5,x_pad+301,y_pad+150)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 3 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_four():
    box = (x_pad+302,y_pad+5,x_pad+401,y_pad+150)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 4 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_five():
    box = (x_pad+2,y_pad+155,x_pad+101,y_pad+300)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 5 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_six():
    box = (x_pad+102,y_pad+155,x_pad+201,y_pad+300)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 6 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_seven():
    box = (x_pad+202,y_pad+155,x_pad+301,y_pad+300)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 7 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_eight():
    box = (x_pad+302,y_pad+155,x_pad+401,y_pad+300)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 8 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_nine():
    box = (x_pad+2,y_pad+305,x_pad+101,y_pad+450)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 9 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_ten():
    box = (x_pad+102,y_pad+305,x_pad+201,y_pad+450)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 10 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_eleven():
    box = (x_pad+202,y_pad+305,x_pad+301,y_pad+450)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 11 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_twelve():
    box = (x_pad+302,y_pad+305,x_pad+401,y_pad+450)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 12 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_thirteen():
    box = (x_pad+2,y_pad+455,x_pad+101,y_pad+600)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 13 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_fourteen():
    box = (x_pad+102,y_pad+455,x_pad+201,y_pad+600)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 14 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_fifteen():
    box = (x_pad+202,y_pad+455,x_pad+301,y_pad+600)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 15 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
def get_tile_sixteen():
    box = (x_pad+302,y_pad+455,x_pad+401,y_pad+600)
    im = ImageGrab.grab(box)
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    hexchars = "0123456789ABCDEF"
    print "Tile 16 #" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]
    return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]

def moveMouse(x=(0,0)):
    win32api.SetCursorPos(x)
    
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "\nClick"
    time.sleep(.01)
    
def clickTile():
    click = 1
    while (click > 0):
        click = click + 1
        t9 = get_tile_nine()
        t10 = get_tile_ten()
        t11 = get_tile_eleven()
        t12 = get_tile_twelve()
        if t9 != '#111111' and t9 != '#FFFFFF':
            if t9 == '#FB3E38':
                print "We lost :)"
            else:
                print "We won :)"
            break
        if t9 == '#111111':
            moveMouse(tileMouseLocations['t9'])
            leftClick()
        if t10 == '#111111':
            moveMouse(tileMouseLocations['t10'])
            leftClick()
        if t11 == '#111111':
            moveMouse(tileMouseLocations['t11'])
            leftClick()
        if t12 == '#111111':
            moveMouse(tileMouseLocations['t12'])
            leftClick()
            
def main():
    clickTile();
    #get_tile_one()
    #get_tile_two()
    #get_tile_three()
    #get_tile_four()
    #get_tile_five()
    #get_tile_six()
    #get_tile_seven()
    #get_tile_eight()
    #get_tile_nine()
    #get_tile_ten()
    #get_tile_eleven()
    #get_tile_twelve()
    #get_tile_thirteen()
    #get_tile_fourteen()
    #get_tile_fifteen()
    #get_tile_sixteen()
 
if __name__ == '__main__':
    main()
