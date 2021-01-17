import pyautogui,time,win32api,win32con,keyboard,random
from PIL import ImageGrab

seurattu = []
x = 480
y = 410

x_min = 480
y_min = 410
x_max = 880
y_max = 770

kuva = 0
time.sleep(2)
screen = ImageGrab.grab(bbox=(x_min,y_min,x_max,y_max))
while True:
    #kuinka montaa seurataan kerralla
    if len(seurattu) == 40:
        break
    if keyboard.is_pressed("l"):
        break

    if screen.getpixel((x-x_min,y-y_min)) == (0,149,246):
        x_plus = random.randint(1,40)
        y_plus = random.randint(5,20)
        
        if random.randint(1,10) < 5:  
            pyautogui.moveTo(x-random.randint(5,40),y-random.randint(10,20),1/random.randint(5,10))
        else:
            pyautogui.moveTo(x+random.randint(5,40),y-random.randint(10,20),1/random.randint(5,10))
            
        pyautogui.moveTo(x+x_plus,y+y_plus,2/random.randint(1,5))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x+x_plus,y+y_plus,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x+x_plus,y+y_plus,0,0)
        seurattu.append([x,y])
        time.sleep(3)
        screen = ImageGrab.grab(bbox=(x_min,y_min,x_max,y_max))
        y += 10 #kommentoi pois kun alat klikkailemaan

    x += 10
    if x >= x_max:
        x = x_min
        y += 5

    if y >= y_max:
        y = y_min
        x_siirto = random.randint(x_min+20,x_max-20)
        pyautogui.moveTo(x_siirto, y_max-10,random.randint(1,2)/random.randint(1,6))
        pyautogui.dragTo(x_siirto,392, 2, button='left')
        screen = ImageGrab.grab(bbox=(x_min,y_min,x_max,y_max))
