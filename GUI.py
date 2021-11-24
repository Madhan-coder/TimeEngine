# import modules
from tkinter import *
import tkinter.ttk as ttk
import ttkthemes as tk
import os
import tkinter.font as font
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
from win32gui import GetForegroundWindow
import psutil
import win32process
from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
from datetime import date
import subprocess
from tkinter import *
import tkinter.font as font
import subprocess
from time import strftime
from time import *
from time import sleep
import os
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
from win32gui import GetForegroundWindow
import psutil
import win32process
import webbrowser
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from win10toast import ToastNotifier


# Register screen

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Time Engine")
    register_screen.geometry("300x250")
    register_screen.config(bg='Grey')
    PHOTO = PhotoImage(file='icon.png')
    register_screen.iconphoto(False, PHOTO)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    font_1 = font.Font(family='cooper black', size='20', weight='bold')
    font_2 = font.Font(family='cooper black', size='16', weight='bold')
    LABEL_1 = Label(register_screen, text="Please enter details below", bg="grey")
    LABEL_1['font'] = font_1
    LABEL_1.pack()
    Label(register_screen, text="").pack()
    LABEL_2 = Label(register_screen, text="Username * ", bg='Red')
    LABEL_2['font'] = font_2
    LABEL_2.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    LABEL_3 = Label(register_screen, text="Password * ", bg='Red')
    LABEL_3['font'] = font_2
    LABEL_3.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Time Engine")
    login_screen.config(bg='LightBlue')
    PHOTO = PhotoImage(file='icon.png')
    login_screen.iconphoto(False, PHOTO)
    font_1 = font.Font(family='Verdana', size='16')
    Label_1 = Label(login_screen, text="Please enter details below to login")
    Label_1['font'] = font_1
    Label_1.pack()
    Label(login_screen, text="", bg='LightBlue').pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    font_2 = font.Font(family='cooper black', size='20', weight='bold')
    font_3 = font.Font(family='Verdana', size='25', weight='bold')
    User_labl = Label(login_screen, text="Username * ", bg='LightBlue', fg='black')
    User_labl['font'] = font_2
    User_labl.pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg='LightBlue').pack()
    Pass_labl = Label(login_screen, text="Password * ", bg='LightBlue', fg='black')
    Pass_labl['font'] = font_2
    Pass_labl.pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg='LightBlue').pack()
    Button_1 = Button(login_screen, text="Login", width=10, height=2, command=login_verify)
    Button_1['font'] = font_3
    Button_1.pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    parent_dir = 'C:/'
    directory = 'Time Engine'
    Path = os.path.join(parent_dir, directory)
    os.mkdir(Path)

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("cooper body", 20)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_success():
    Menu_window = Tk()
    Menu_window.title('Time Engine')
    Menu_window.config(bg='#51FF53')
    Menu_window.geometry('800x500')

    def App_track():
        App_win = Tk()
        App_win.title('Time Engine')
        App_win.config(bg='Orange')
        Label_2 = Label(App_win, text='Start to get started', bg='orange')
        Label_2['font'] = Font_2
        Label_2.pack()
        Label(App_win, text='!!! This window will be closed when started.!!!', bg='orange').pack()
        Label(App_win, text='Press Submit in Menu to get data.', bg='orange').pack()
        Label(App_win, text="You'll get notified in every 1/2 hour").pack()

        def Track():
            App_win.destroy()
            from win32gui import GetForegroundWindow
            import psutil
            import time
            import win32process
            import uiautomation as auto
            import sys
            import win32gui

            def url_to_name(url):
                string_list = url.split('/')
                return string_list[2]

            def get_active_window():
                global _active_window_name
                _active_window_name = None
                if sys.platform in ['Windows', 'win32', 'cygwin']:
                    window = win32gui.GetForegroundWindow()
                    _active_window_name = win32gui.GetWindowText(window)

                return _active_window_name

            def get_chrome_url():
                if sys.platform in ['Windows', 'win32', 'cygwin']:
                    window = win32gui.GetForegroundWindow()
                    chromeControl = auto.ControlFromHandle(window)
                    edit = chromeControl.EditControl()
                    return 'https://' + edit.GetValuePattern().Value

                return _active_window_name

            process_time = {}
            timestamp = {}
            while True:
                current_app = get_active_window()
                if 'Google Chrome' in current_app:
                    current_app = url_to_name(get_chrome_url())
                timestamp[current_app] = int(time.time())
                time.sleep(1)
                if current_app not in process_time.keys():
                    process_time[current_app] = 0
                process_time[current_app] = process_time[current_app] + int(time.time()) - timestamp[current_app]
                print(process_time)
                a = process_time.values()

                LIST = list(a)

                key_list = list(process_time.keys())

                for i in LIST:
                    if i == 1800:
                        App = key_list[LIST.index(1800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                  You've been on {App} for 30 minutes.''', icon_path='icon.png', duration=10)
                    elif i == 3600:
                        App = key_list[LIST.index(3600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                You've been on {App} for a hour.''', icon_path='icon.png', duration=10)
                    elif i == 5400:
                        App = key_list[LIST.index(5400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for a 1.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 7200:
                        App = key_list[LIST.index(7200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for two hours.''', icon_path='icon.png', duration=10)
                    elif i == 9000:
                        App = key_list[LIST.index(9000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 2.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 10800:
                        App = key_list[LIST.index(10800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 3 hours.''', icon_path='icon.png', duration=10)
                    elif i == 12600:
                        App = key_list[LIST.index(12600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 3.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 14400:
                        App = key_list[LIST.index(14400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 4 hours.''', icon_path='icon.png', duration=10)
                    elif i == 16200:
                        App = key_list[LIST.index(16200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 4.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 18000:
                        App = key_list[LIST.index(18000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 21600:
                        App = key_list[LIST.index(21600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 5.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 23400:
                        App = key_list[LIST.index(23400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 6 hours.''', icon_path='icon.png', duration=10)
                    elif i == 25200:
                        App = key_list[LIST.index(25200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 7 hours.''', icon_path='icon.png', duration=10)
                    elif i == 27000:
                        App = key_list[LIST.index(27000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 7.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 28800:
                        App = key_list[LIST.index(28800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 8 hours.''', icon_path='icon.png', duration=10)
                    elif i == 30600:
                        App = key_list[LIST.index(30600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 8.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 32400:
                        App = key_list[LIST.index(32400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 9 hours.''', icon_path='icon.png', duration=10)
                    elif i == 34200:
                        App = key_list[LIST.index(34200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 9.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 36000:
                        App = key_list[LIST.index(36000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 10 hours.''', icon_path='icon.png', duration=10)
                    elif i == 37800:
                        App = key_list[LIST.index(37800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 10.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 39600:
                        App = key_list[LIST.index(39600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 11 hours.''', icon_path='icon.png', duration=10)
                    elif i == 41400:
                        App = key_list[LIST.index(41400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 11.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 43200:
                        App = key_list[LIST.index(3600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 12 hour.''', icon_path='icon.png', duration=10)
                    elif i == 45000:
                        App = key_list[LIST.index(45000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 12.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 46800:
                        App = key_list[LIST.index(46800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 13 hours.''', icon_path='icon.png', duration=10)
                    elif i == 48600:
                        App = key_list[LIST.index(48600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 13.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 50400:
                        App = key_list[LIST.index(50400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 14 hours.''', icon_path='icon.png', duration=10)
                    elif i == 52200:
                        App = key_list[LIST.index(52200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 14.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 54000:
                        App = key_list[LIST.index(54000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 15 hours.''', icon_path='icon.png', duration=10)
                    elif i == 55800:
                        App = key_list[LIST.index(55800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 15.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 57600:
                        App = key_list[LIST.index(57600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 16 hours.''', icon_path='icon.png', duration=10)
                    elif i == 59400:
                        App = key_list[LIST.index(59400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 16.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 61200:
                        App = key_list[LIST.index(61200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 17 hours.''', icon_path='icon.png', duration=10)
                    elif i == 63000:
                        App = key_list[LIST.index(63000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 17.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 64800:
                        App = key_list[LIST.index(64800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 18 hours.''', icon_path='icon.png', duration=10)
                    elif i == 66600:
                        App = key_list[LIST.index(66600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 18.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 68400:
                        App = key_list[LIST.index(68400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 19 hours.''', icon_path='icon.png', duration=10)
                    elif i == 70200:
                        App = key_list[LIST.index(70200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 19.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 72000:
                        App = key_list[LIST.index(72000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 20 hours.''', icon_path='icon.png', duration=10)
                    elif i == 73800:
                        App = key_list[LIST.index(7300)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 20.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 75600:
                        App = key_list[LIST.index(75600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 21 hours.''', icon_path='icon.png', duration=10)
                    elif i == 77400:
                        App = key_list[LIST.index(77400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 21.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 79200:
                        App = key_list[LIST.index(79200)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 22 hours.''', icon_path='icon.png', duration=10)
                    elif i == 81000:
                        App = key_list[LIST.index(81000)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 22.5 hours.''', icon_path='icon.png', duration=10)
                    elif i == 82800:
                        App = key_list[LIST.index(82800)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 23 hours.''', icon_path='icon.png', duration=10)
                    elif i == 84600:
                        App = key_list[LIST.index(84600)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 23.5 hour.''', icon_path='icon.png', duration=10)
                    elif i == 86400:
                        App = key_list[LIST.index(86400)]
                        n = ToastNotifier()
                        n.show_toast('Time Engine', f'''
                    You've been on {App} for 24 hours.''', icon_path='icon.png', duration=10)

                Button(App_win, text='Start', command=Track).pack()

    def Info():
        Info_window = Tk()
        Info_window.config(bg='#72FFF3')
        Info_window.title('Time Engine')
        Font_3 = font.Font(family='Verdana', size=20, weight='bold')
        global Font_4
        Font_4 = font.Font(family='Verdana', size=20, weight='bold')
        Label1 = Label(Info_window, text='Read the Read the Docs in C:/Time Engine directory', bg="#72FFF3",
                       fg='red')
        Label1['font'] = Font_4
        Label1.pack()
        Label3 = Label(Info_window, text='While using App usage Tracker, window might get closed', bg='#72FFF3')
        Label3['font'] = Font_3
        Label3.pack()
        Label4 = Label(Info_window,
                       text="Press the submit button in Menu to get data of app usage",
                       bg='#72FFF3')
        Label4['font'] = Font_3
        Label4.pack()
        Label5 = Label(Info_window, text="The data of the app will be stored in 'C:/Time Engine'", bg='#72FFF3')
        Label5['font'] = Font_3
        Label5.pack()
        Info_window.mainloop()

    def Sys_info():
        Sys_win = Tk()
        Sys_win.title('Time Engine')
        Sys_win.config(bg='#00fff2')
        file = open("C:/Time Engine/System Info.txt", "r+")
        file.truncate(0)
        file.close()

        Font_6 = font.Font(family='Cooper Black', size=25, weight='bold')
        Label6 = Label(Sys_win, text='Your system data have been saved to the C:/Time Engine, as a text file'
                       , bg='#00fff2')
        Label6['font'] = Font_6
        Label6.pack()

        file_ = open('C:/Time Engine/System Info.txt', 'w+')
        subprocess.run('python sys_info.py', shell=True, stdout=file_)
        file_.close()
        Label7 = Label(Sys_win, text='Press the down the down to get live data', bg='#00fff2')
        Label7['font'] = Font_6
        Label7.pack()
        Label(Sys_win, text='Please restart the app after getting the live info.', bg='#00fff2').pack()

        def Live_data():
            plt.figure(facecolor='w')

            cpu_bar = plt.subplot(221)
            cpu_line = plt.subplot(222)
            memory_bar = plt.subplot(223)
            memory_line = plt.subplot(224)

            cpu_bar.set_position([0.125, 0.536, 0.1, 0.3])
            cpu_line.set_position([0.3, 0.536, 0.6, 0.3])
            memory_bar.set_position([0.125, 0.1, 0.1, 0.3])
            memory_line.set_position([0.3, 0.1, 0.6, 0.3])

            cpu_line.set_ylim(0, 100)
            memory_line.set_ylim(0, 100)

            cpu_line.set_xlim(0, 20)
            memory_line.set_xlim(0, 20)

            miloc_1 = plt.MultipleLocator(1)
            miloc_2 = plt.MultipleLocator(10)
            cpu_line.xaxis.set_minor_locator(miloc_1)
            cpu_line.yaxis.set_minor_locator(miloc_2)
            cpu_line.grid(which='minor', color='darkgray')
            memory_line.xaxis.set_minor_locator(miloc_1)
            memory_line.yaxis.set_minor_locator(miloc_2)
            memory_line.grid(which='minor')

            cpu_bar.get_xaxis().set_visible(False)
            memory_bar.get_xaxis().set_visible(False)

            x_2 = []
            y_2 = []
            x_4 = []
            y_4 = []

            width = 1
            step = 0
            while True:
                cpu_bar.cla()
                cpu_bar.set_ylim(0, 100)
                temp_cpu = psutil.cpu_percent()
                x_1 = [0]
                y_1 = [temp_cpu]
                cpu_bar.set_title(str(temp_cpu) + "%")
                cpu_bar.bar(x_1, y_1, width=width)

                x_2.append(step)
                y_2.append(temp_cpu)
                if step > 20:
                    cpu_line.set_xlim(step - 20, step)
                    memory_line.set_xlim(step - 20, step)
                cpu_line.plot(x_2, y_2, color='b')
                cpu_line.legend(['CPU usage(%)'], loc="upper right")
                cpu_line.set_xlabel('Time(s)')

                memory_bar.cla()
                memory_bar.set_ylim(0, 100)
                temp_memory = psutil.virtual_memory().percent
                x_3 = [0]
                y_3 = [temp_memory]
                memory_bar.set_title(str(temp_memory) + '%')
                memory_bar.bar(x_3, y_3, width=width, color='r')

                x_4.append(step)
                y_4.append(temp_memory)
                memory_line.plot(x_4, y_4, color='r', label='Memory')
                plt.xlabel('Time(s)')
                step += 1
                plt.legend(['Memory(%)'], loc="upper right")
                plt.pause(0.5)

            plt.show()

        Button_5 = Button(Sys_win, text='Get Live Info', command=Live_data, height=2, width=15)
        Button_5['font'] = Font_6
        Button_5.pack()
        Sys_win.mainloop()

    Font_1 = font.Font(family='Verdana', size=16)
    Font_2 = font.Font(family='Cooper Black', size=25, weight='bold')

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

        # Styling the label widget so that clock

    # will look more attractive
    lbl = Label(Menu_window, font=('calibri', 40, 'bold'),
                background='#51ff53',
                foreground='blue')

    # Placing clock at the centre
    # of the tkinter window
    lbl.pack(anchor='center')
    time()
    DIR = 'C:/Time Engine/'
    Folder = str(date.today())
    way = os.path.join(DIR, Folder)
    try:
        os.mkdir(way)
    except OSError as error:
        print(error)

    def speed():
        win = Tk()
        win.config(bg='#51FF53')
        win.title('Network Speed')
        a = StringVar()
        from speedtest import Speedtest
        a.set('Download: ', Speedtest.download())
        label = Label(win, textvariable=a,
                      fg='red', bg='#51ff53')
        label['font'] = Font_1
        label.pack()
        b = StringVar()
        b.set('Upload: ', Speedtest.upload())
        LABEL = Label(win, textvariable=b, bg='#51ff53')
        LABEL['font'] = Font_1
        LABEL.pack()
        win.mainloop()

    Label_1 = Label(Menu_window, text='Choose what you want to trace out!!!', bg='#51FF53', fg='red')
    Label_1['font'] = Font_2
    Label_1.pack()
    Label(Menu_window, text='', bg='#51FF53').pack()
    Label(Menu_window, text='', bg='#51FF53').pack()
    photo_1 = PhotoImage(file='laptop.png')
    Button_1 = Button(Menu_window, text='App Usage Tracker', height='70', width='265',
                      image=photo_1, compound=LEFT, command=App_track)
    Button_1['font'] = Font_1
    Button_1.pack()
    Label(Menu_window, text='', bg='#51FF53').pack()
    Label(Menu_window, text='', bg='#51FF53').pack()
    photo_2 = PhotoImage(file='technology.png')
    Button_2 = Button(Menu_window, text='Speed Test', height='80', width='288', image=photo_2, compound=LEFT,
                      command=speed)
    Button_2['font'] = Font_1
    Button_2.pack()
    photo_3 = PhotoImage(file='info.png')
    Button_3 = Button(Menu_window, image=photo_3, command=Info)
    Button_3.place(x=10, y=10)
    Label(Menu_window, text='', bg='#51FF53').pack()
    Label(Menu_window, text='', bg='#51FF53').pack()
    Button_4 = Button(Menu_window, text='System Information', fg='red', command=Sys_info)
    Button_4['font'] = Font_1
    Button_4.pack()
    Menu_window.mainloop()


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="grey", width="300", height="4", font=("Verdana", 16)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
