import customtkinter
import commands



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
fontname=("TkHeadingFont", 18)

# host = "192.168.10.251"  # as both code is running on same pc
# port = 3000  # socket server port number
# client_socket = socket.socket()  # instantiate

#dodelat connect a disconect button podle knihovny tcp_klient

class Channel(customtkinter.CTkFrame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        #voltage
        self.volt_label = customtkinter.CTkLabel(self,text="Voltage:",width=90)
        self.volt_label.grid(row=1,column=0,sticky="w")
        
        self.set_volt_e = customtkinter.CTkEntry(self,placeholder_text="(min-0.01)",width=80)
        self.set_volt_e.grid(row=1,column=1,sticky="",padx=0,pady=5)

        # self.get_volt_button = customtkinter.CTkButton(self,text="GET",width=60,height=10)
        # self.get_volt_button.grid(row=1,column=2,padx=5)
        
        #current
        self.cur_label = customtkinter.CTkLabel(self,text="Current:",width=90)
        self.cur_label.grid(row=2,column=0,sticky="w")
        
        self.set_cur_e = customtkinter.CTkEntry(self,placeholder_text="(min-)",width=80)
        self.set_cur_e.grid(row=2,column=1,sticky="",padx=0,pady=5)

        # self.get_curr_button = customtkinter.CTkButton(self,text="GET",width=60,height=10)
        # self.get_curr_button.grid(row=2,column=2,padx=5)
        #limitV
        self.limV_label = customtkinter.CTkLabel(self,text="V-Limit:",width=90)
        self.limV_label.grid(row=3,column=0,sticky="w")
        
        self.set_limV_e = customtkinter.CTkEntry(self,placeholder_text="(min-)",width=80)
        self.set_limV_e.grid(row=3,column=1,sticky="",padx=0,pady=5)

        # self.get_limitV_button = customtkinter.CTkButton(self,text="GET",width=60,height=10)
        # self.get_limitV_button.grid(row=3,column=2,padx=5)
        #limitC
        self.limC_label = customtkinter.CTkLabel(self,text="C-Limit:",width=90)
        self.limC_label.grid(row=4,column=0,sticky="w")
        
        self.set_limC_e = customtkinter.CTkEntry(self,placeholder_text="(min-)",width=80)
        self.set_limC_e.grid(row=4,column=1,sticky="",padx=0,pady=5)

        # self.get_limitC_button = customtkinter.CTkButton(self,text="GET",width=60,height=10)
        # self.get_limitC_button.grid(row=4,column=2,padx=5)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("580x400")
        self.title("Nastaveni zdroje")

        self.output_label = customtkinter.CTkLabel(self,text="Output:",font=fontname)
        self.output_label.grid(row=0,column=0)
        self.get_label = customtkinter.CTkLabel(self,text="Get values of:",font=fontname)
        self.get_label.grid(row=0,column=1)
        self.get_values_ch1 = customtkinter.CTkButton(self,text="channel1",width=60,height=10)
        self.get_values_ch1.grid(row=1,column=1,pady=(0,60))
        self.get_values_ch2 = customtkinter.CTkButton(self,text="channel2",width=60,height=10)
        self.get_values_ch2.grid(row=1,column=1,pady=0)
        self.get_values_ch3 = customtkinter.CTkButton(self,text="channel3",width=60,height=10)
        self.get_values_ch3.grid(row=1,column=1,pady=(60,0))
        self.textbox = customtkinter.CTkTextbox(self,height=120,width=180)
        self.textbox.grid(row=1, column=0,columnspan=1, padx=5, pady=5,sticky="nsew")
        self.tcp_connect_button = customtkinter.CTkButton(self,text="connect",command=commands.socket_connect,fg_color="blue",width=70,height=10)
        self.tcp_connect_button.grid(row=0,column=2,sticky="e")#sticky="ne"
        self.tcp_connect_button = customtkinter.CTkButton(self,text="disconnect",command=commands.socket_disconnect,fg_color="red",width=65,height=10)
        self.tcp_connect_button.grid(row=1,column=2,sticky="ne")#padx=(50,0),pady=(0,30)



        #__________ch1
        self.channel_label1 = customtkinter.CTkLabel(self,text="Channel1:",font=fontname)
        self.channel_label1.grid(row=2,column=0,sticky="nsew")
        self.frame_ch1 = Channel(self,width=80,height=150)
        self.frame_ch1.grid(row=3,column=0,padx=10,pady=10)
        self.set_button_ch1 = customtkinter.CTkButton(self,text="SET",width=55,fg_color="blue",command=commands.set_ch1)
        self.set_button_ch1.grid(row=4,column=0,sticky="w",padx=10)
        self.switch_button_ch1 = customtkinter.CTkButton(self,text="ON",width=50,command=commands.switch_ch1)
        self.switch_button_ch1.grid(row=4,column=0)
        self.switch_off_button_ch1 = customtkinter.CTkButton(self,text="OFF",width=50,fg_color="red")
        self.switch_off_button_ch1.grid(row=4,column=0,sticky="e",padx=(0,15))

        #_____________ch2
        self.channel_label2 = customtkinter.CTkLabel(self,text="Channel2:",font=fontname)
        self.channel_label2.grid(row=2,column=1,sticky="nsew")
        self.frame_ch2 = Channel(self,width=80,height=150)
        self.frame_ch2.grid(row=3,column=1,padx=10,pady=10)
        self.set_button_ch2 = customtkinter.CTkButton(self,text="SET",width=55,fg_color="blue",command=commands.set_ch2)
        self.set_button_ch2.grid(row=4,column=1,sticky="w",padx=10)
        self.switch_button_ch2 = customtkinter.CTkButton(self,text="ON",width=50,command=commands.switch_ch2)
        self.switch_button_ch2.grid(row=4,column=1)
        self.switch_off_button_ch2 = customtkinter.CTkButton(self,text="OFF",width=50,fg_color="red")
        self.switch_off_button_ch2.grid(row=4,column=1,sticky="e",padx=(0,15))

        #ch3
        self.channel_label3 = customtkinter.CTkLabel(self,text="Channel3:",font=fontname)
        self.channel_label3.grid(row=2,column=2,sticky="nsew")
        self.frame_ch3 = Channel(self,width=80,height=150)
        self.frame_ch3.grid(row=3,column=2,padx=10,pady=10)
        self.set_button_ch3 = customtkinter.CTkButton(self,text="SET",width=55,fg_color="blue",command=commands.set_ch3)
        self.set_button_ch3.grid(row=4,column=2,sticky="w",padx=10)
        self.switch_button_ch3 = customtkinter.CTkButton(self,text="ON",width=50,command=commands.switch_ch3)
        self.switch_button_ch3.grid(row=4,column=2)
        self.switch_off_button_ch3 = customtkinter.CTkButton(self,text="OFF",width=50,fg_color="red")
        self.switch_off_button_ch3.grid(row=4,column=2,sticky="e",padx=(0,15))


    def set_ch1(self):
        channel = "1"
        volt = self.frame_ch1.set_volt_e.get()
        cur = self.frame_ch1.set_cur_e.get()
        limV = self.frame_ch1.set_limV_e.get()
        limC = self.frame_ch1.set_limC_e.get()
        message = commands.set_channel(channel,volt,cur,limV,limC)#return volt+cur+limV+limC
        try:
            commands.client_socket.send(message.encode())
            self.textbox.insert("end","ch1 data set succesfully\n")
        except:
            print("setch1: failed to send message")

    def set_ch2(self):
        channel = "2"
        volt = self.frame_ch2.set_volt_e.get()
        cur = self.frame_ch2.set_cur_e.get()
        limV = self.frame_ch2.set_limV_e.get()
        limC = self.frame_ch2.set_limC_e.get()
        message = commands.set_channel(channel,volt,cur,limV,limC)#return channel+volt+cur+limV+limC
        try:
            commands.client_socket.send(message.encode())
            self.textbox.insert("end","ch2 data set succesfully\n")
        except:
            print("setch2: failed to send message")

    def set_ch3(self):
        channel = "3"
        volt = self.frame_ch3.set_volt_e.get()
        cur = self.frame_ch3.set_cur_e.get()
        limV = self.frame_ch3.set_limV_e.get()
        limC = self.frame_ch3.set_limC_e.get()
        message = commands.set_channel(channel,volt,cur,limV,limC)#return volt+cur+limV+limC
        try:
            commands.client_socket.send(message.encode())
            self.textbox.insert("end","ch3 data set succesfully\n")
        except:
            print("setch3: failed to send message")
    #______________________________________________________________


if __name__ == "__main__":
    app = App()
  
    app.mainloop()