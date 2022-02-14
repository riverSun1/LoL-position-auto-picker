import pyautogui
import keyboard

print('---------------sun1\'s LOL position auto picker---------------')
print('|                                                            |')
want = input('   원하는 포지션을 입력해주세요. : ')
print('')
print('   1. 마우스를 채팅창에 놓은 뒤 space bar를 눌러주세요.')
print('   2. 게임이 잡히기 바로 직전에 enter를 눌러주세요.')
print('|                                                            |')
print('--------------------------------------------------------------')

location = (0,0)

while True:
    if keyboard.is_pressed('space'):
        location = pyautogui.position()

    if keyboard.is_pressed('enter'):
        for i in range(10):
            pyautogui.click(location)
            keyboard.write(want)
            keyboard.press('enter')
        break;