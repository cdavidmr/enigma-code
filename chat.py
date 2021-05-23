"""
Created 16/05/2021

@author: Proyecto final Codigo Enigma
"""
from os import name
from tkinter import *
import time
import enigma


class Chat:

    def __init__(self, master):
        self.myframe = Frame(master)
        self.myframe.pack()

        self.current_timer = time.time()
        self.timer = 10000
        self.status = 0
        self.clave = 123

        #Chat text variable
        self.chatText = StringVar()

        #load images icon
        self.send_img = PhotoImage(file = 'resource/send.png')
    
        #Set Chat display
        self.chat_display = Listbox(master, bg='black', fg='white')
        self.chat_display.place(x=15, y=5, width=645, height=390)

        self.chat_text = Text(master, bd=1, bg='#b5b5b5', width=80)
        self.chat_text.place(x=15, y=405, height=80)

        self.channels = Listbox(master, bd=1, bg='#0e00a6')
        self.channels.configure(fg='#94cdff')
        self.channels.insert(END, 'Channels')
        self.channels.place(x=670, y=5, width=120, height=390)

        self.enviar = Button(master, image=self.send_img, borderwidth=2, bg='#8adaff', command=self.send)
        self.enviar.place(x=670, y=402, width=120, height=80)

        self.check_inactivity()

    def send(self):
        text = time.strftime('%H:%M:%S > ') + '(me): ' + self.chat_text.get("1.0", END).strip().lower()
        self.chat_display.configure(fg='#95ff87')
        self.chat_display.insert(END, text)
        self.current_timer = time.time()

    def lock_chat(self):
        text_lock = []
        text = self.chat_display.get(0, END)
        self.chat_display.delete(0, END)
        for msg in text:
            msg_to_lock = enigma.Maquina(msg, 123)
            text_lock.append(msg_to_lock.cifrar_decifrar(0))
        for msg_lock in text_lock:
            self.chat_display.configure(fg='#ffe8bf')
            self.chat_display.insert(END, msg_lock)

    def check_inactivity(self):
        now = time.time()
        diff_time = now - self.current_timer
        if diff_time >= 10 and self.status != 1:
            self.status = 1
            self.lock_chat()
        self.myframe.after(self.timer, self.check_inactivity)


root = Tk()
root.title('Enigma Chat')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='resource/ico.png'))
root.geometry('800x500')
root.configure(bg='#535d61')

chat = Chat(root)


root.mainloop()
