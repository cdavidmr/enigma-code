"""
Created 16/05/2021

@author: Proyecto final Codigo Enigma
"""

from tkinter import *
from PIL import Image, ImageTk
import time
import enigma

root = Tk()
root.title('Enigma Chat')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='resource/enigma_ico.png'))
root.geometry('800x500')
root.configure(bg='#535d61')

def load_chat(nick, key, time):
    chat = Chat(root, nick, key, time)

class Chat:

    def __init__(self, master, nick, key, timer):
        self.myframe = Frame(master)
        self.myframe.pack()

        self.key = key
        self.nick_name = nick
        self.timer_diff = timer

        self.current_timer = time.time()
        self.timer_check = 2000
        self.status = 0

        #Chat text variable
        self.chatText = StringVar()

        #load images icon
        self.send_icon = PhotoImage(file = 'resource/send.png')
        self.lock_icon = PhotoImage(file = 'resource/lock.small.png')
    
        #Set Chat display
        self.chat_display = Listbox(bg='black', fg='white')
        self.chat_display.place(x=15, y=5, width=645, height=390)

        self.chat_text = Text(bg='#b5b5b5', width=80)
        self.chat_text.place(x=15, y=405, height=80)

        self.channels = Listbox(bd=1, bg='#0e00a6')
        self.channels.configure(fg='#94cdff')
        self.channels.insert(END, 'Channels')
        self.channels.place(x=670, y=5, width=120, height=390)

        self.send_btn = Button(image=self.send_icon, borderwidth=2, bg='#8adaff', command=self.send)
        self.send_btn.place(x=670, y=402, width=120, height=80)

        self.chat_text.bind("<KeyPress>", self.keydown)

        self.check_inactivity()

    def send(self):
        if self.status == 0:
            text = time.strftime('%H:%M:%S > ') + f'({self.nick_name}): ' + self.chat_text.get("1.0", END).strip().lower()
            self.chat_text.delete('1.0', END)
            self.chat_display.configure(fg='#95ff87')
            self.chat_display.insert(END, text)
            self.reset_timer()

    def unlock_btn_load(self):
        self.unlock_btn = Button(bg='black', borderwidth=0, highlightthickness=0, command=self.unlock_chat_popup)
        self.unlock_btn.config(image=self.lock_icon)
        self.unlock_btn.place(x=600, y=15, width=50, height=50)

    def frame_destroy(self, frame):
        frame.destroy()

    def lock_chat(self, text_list):
        text = text_list
        text_lock = []
        self.chat_display.delete(0, END)
        for msg in text:
            msg_to_lock = enigma.Maquina(msg, self.key)
            text_lock.append(msg_to_lock.cifrar_decifrar(0))
        for msg_lock in text_lock:
            self.chat_display.configure(fg='#ffe8bf')
            self.chat_display.insert(END, msg_lock)
        self.unlock_btn_load()

    def unlock_chat_popup(self):
        self.load_popup()
    
    def unlock_chat(self):
        text = self.chat_display.get(0, END)
        text_unlock = []
        self.status = 0
        self.chat_display.delete(0, END)
        for msg in text:
            msg_to_unlock = enigma.Maquina(msg, self.key)
            text_unlock.append(msg_to_unlock.cifrar_decifrar(1))
        for msg_unlock in text_unlock:
            self.chat_display.configure(fg='#95ff87')
            self.chat_display.insert(END, msg_unlock)
        self.reset_timer()
        self.check_inactivity()

    def keydown(self, event):
        self.reset_timer()

    def reset_timer(self):
        self.current_timer = time.time()

    def check_inactivity(self):
        now = time.time()
        diff_time = now - self.current_timer
        text_list = self.chat_display.get(0, END)
        print(diff_time)
        if self.status == 0:
            if diff_time >= self.timer_diff and len(text_list) > 0:
                self.status = 1
                self.lock_chat(text_list)
            self.myframe.after(self.timer_check, self.check_inactivity)

    def load_popup(self):
        self.popup = Tk()
        self.popup.wm_title("Unlock Chat")
        self.popup.configure(bg='#535d61')

        self.lb_key_popup = Label(self.popup, font=('Courier', 12, 'bold'), bg='#535d61', fg='#4fff7b', text='Key Code: ')
        self.lb_key_popup.place(x=50, y=10)

        self.key_code_popup = Entry(self.popup, font=('Courier', 12), bg='black', fg='white')
        self.key_code_popup.place(x=55, y=40, width=80,height=35)

        self.unlock_btn_popup = Button(
            self.popup,
            font=('Courier', 12, 'bold'), bg='#535d61', 
            fg='#8adaff', borderwidth=1, 
            highlightthickness=1,
            text='Unlock', 
            command=self.check_unlock_chat
            )
        self.unlock_btn_popup.place(x=55, y=100)
        self.lb_error = Label(self.popup, font=('Courier', 10, 'bold'), bg='#535d61', fg='#fa6666', text='')
        self.popup.mainloop()
    
    def check_unlock_chat(self):
        try:
            key = int(self.key_code_popup.get())        
            if key == self.key:
                self.unlock_btn.destroy()
                self.unlock_chat()
                self.popup.destroy()
            else:    
                self.lb_error.config(text='Key Code not match!')
                self.lb_error.place(x=30, y=150)
        except ValueError:
            self.lb_error.config(text='Key Code Invalid!')
            self.lb_error.place(x=30, y=150)
    
class SignUp():

    def __init__(self, master):
        self.myframe = Frame(master)
        self.myframe.pack()

        img_enigma = Image.open('resource/enigma_ico.png')
        img_enigma_r = img_enigma.resize((200, 200), Image.ANTIALIAS)

        self.time_to_lock = IntVar()

        #load images icon
        self.sign_in_icon = PhotoImage(file = 'resource/sign_in.small.png')
        self.enigma_icon = ImageTk.PhotoImage(img_enigma_r)

        self.img_icon = Label(bg='#535d61', image=self.enigma_icon )
        self.img_icon.place(x=15, y=15)

        self.lb_welcome = Label(font=('Courier', 16, 'bold'), bg='#535d61', fg='#08d6ff', 
        text=""" Welcome to Enigma Chat !
        Safe and Easy       
        """)
        self.lb_welcome.place(x=200, y=100)

        self.lb_nick = Label(font=('Courier', 16, 'bold'), bg='#535d61', fg='#4fff7b', text='Nick Name: ')
        self.lb_nick.place(x=230, y=200)
        
        self.nick_name = Text(font=('Courier', 16), bg='black', fg='white')
        self.nick_name.place(x=400, y=200, width=150,height=35)

        self.lb_key = Label(font=('Courier', 16, 'bold'), bg='#535d61', fg='#4fff7b', text='Key Code: ')
        self.lb_key.place(x=230, y=250)

        self.key_code = Entry(font=('Courier', 16), bg='black', fg='white')
        self.key_code.place(x=400, y=250, width=150,height=35)

        self.lb_sec_lock = Label(font=('Courier', 16, 'bold'), bg='#535d61', fg='#4fff7b', text='Time to Lock: ')
        self.lb_sec_lock.place(x=230, y=300)

        self.sec_lock = Spinbox(font=('Courier', 16), bg='black', fg='white', from_= 10, to=3600, increment=1, textvariable=self.time_to_lock)
        self.sec_lock.place(x=410, y=300, width=80,height=35)

        self.sign_btn = Button(image=self.sign_in_icon, borderwidth=0, highlightthickness=0, bg='#535d61', command=self.sign_in)
        self.sign_btn.place(x=350, y=370)

    def sign_in(self):
        nick_name = self.nick_name.get("1.0", END).strip().lower()
        loging_check = True
        try:
            time_diff = int(self.sec_lock.get())
            key = int(self.key_code.get())
        except ValueError:        
            self.lb_key = Label(font=('Courier', 16, 'bold'), bg='#535d61', fg='#fa6666', text='Key Code and Time must be numeric!')
            self.lb_key.place(x=230, y=460)
            loging_check = False
        if loging_check:
            load_chat(nick_name, key, time_diff)
            self.clear()

    def clear(self):
        self.myframe.destroy()
        self.img_icon.destroy()
        self.lb_welcome.destroy()
        self.lb_nick.destroy()
        self.nick_name.destroy()
        self.lb_key.destroy()
        self.key_code.destroy()
        self.sign_btn.destroy()
        self.lb_key.destroy()


login = SignUp(root)


root.mainloop()
