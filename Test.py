from win10toast import ToastNotifier
from time import sleep

sleep(5)
n = ToastNotifier()
n.show_toast('Time Engine', '''
You've working on visual studio code for for about 2 Hours''',duration=20, icon_path='icon.png')
