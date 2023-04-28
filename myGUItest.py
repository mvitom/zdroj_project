import customtkinter
import command
import tcp_client


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
fontname=("TkHeadingFont", 20)

# host = "192.168.10.251"  # as both code is running on same pc
# port = 3000  # socket server port number
# client_socket = socket.socket()  # instantiate

#dodelat connect a disconect button podle knihovny tcp_klient

class Channel(customtkinter.CTkFrame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_label = customtkinter.CTkLabel(self,text="Channel1:",font=fontname)
        self.set_label.grid(row=0,column=0,sticky="nsew")
        #voltage
        self.volt_label = customtkinter.CTkLabel(self,text="Voltage:",font=fontname)
        self.volt_label.grid(row=1,column=0,sticky="w")
        
        self.set_volt_e = customtkinter.CTkEntry(self,placeholder_text="(min-0.01)")
        self.set_volt_e.grid(row=1,column=1,sticky="",padx=0,pady=5)
        #current
        self.cur_label = customtkinter.CTkLabel(self,text="Current:",font=fontname)
        self.cur_label.grid(row=2,column=0,sticky="w")
        
        self.set_cur_e = customtkinter.CTkEntry(self,placeholder_text="(min-)")
        self.set_cur_e.grid(row=2,column=1,sticky="",padx=0,pady=5)
        #limitV
        self.limV_label = customtkinter.CTkLabel(self,text="V-Limit:",font=fontname)
        self.limV_label.grid(row=3,column=0,sticky="w")
        
        self.set_limV_e = customtkinter.CTkEntry(self,placeholder_text="(min-)")
        self.set_limV_e.grid(row=3,column=1,sticky="",padx=0,pady=5)
        #limitC
        self.limC_label = customtkinter.CTkLabel(self,text="C-Limit:",font=fontname)
        self.limC_label.grid(row=4,column=0,sticky="w")
        
        self.set_limC_e = customtkinter.CTkEntry(self,placeholder_text="(min-)")
        self.set_limC_e.grid(row=4,column=1,sticky="",padx=0,pady=5)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x400")
        self.title("Nastaveni zdroje")
        self.output_label = customtkinter.CTkLabel(self,text="Output:",font=fontname)
        self.output_label.grid(row=0,column=0)
        self.textbox = customtkinter.CTkTextbox(self,height=120,width=180)
        self.textbox.grid(row=1, column=0,columnspan=2, padx=5, pady=5,sticky="nsew")
        self.tcp_connect_button = customtkinter.CTkButton(self,text="connect",command=tcp_client.socket_connect,fg_color="blue",font=fontname)
        self.tcp_connect_button.grid(row=0,column=2,pady=(10,0))
        self.tcp_connect_button = customtkinter.CTkButton(self,text="disconnect",command=tcp_client.socket_disconnect,fg_color="red",font=fontname)
        self.tcp_connect_button.grid(row=1,column=2)
        #__________ch1
        self.frame_ch1 = Channel(self,width=80,height=150)
        self.frame_ch1.grid(row=2,column=0,padx=10,pady=10)
        self.set_button_ch1 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=self.set_ch1)
        self.set_button_ch1.grid(row=3,column=0,sticky="w",padx=10)
        self.get_button_ch1 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch1.grid(row=3,column=0,padx=30,pady=5,sticky="e")
        #_____________ch2
        self.frame_ch2 = Channel(self,width=80,height=150)
        self.frame_ch2.grid(row=2,column=1,padx=10,pady=10)
        self.set_button_ch2 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=self.set_ch2)
        self.set_button_ch2.grid(row=3,column=1,sticky="w",padx=10)
        self.get_button_ch2 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch2.grid(row=3,column=1,padx=30,pady=5,sticky="e")
        #ch3
        self.frame_ch3 = Channel(self,width=80,height=150)
        self.frame_ch3.grid(row=2,column=2,padx=10,pady=10)
        self.set_button_ch3 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=self.set_ch3)
        self.set_button_ch3.grid(row=3,column=2,sticky="w",padx=10)
        self.get_button_ch3 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch3.grid(row=3,column=2,padx=30,pady=5,sticky="e")
        # self.scrbar = customtkinter.CTkComboBox(self,values=["channel1", "channel2","channel3"])
        # self.scrbar.grid(row=2,column=1)
    
    def set_ch1(self):
        channel = "1"#tohle bude promenna
        volt = self.frame_ch1.set_volt_e.get()
        cur = self.frame_ch1.set_cur_e.get()
        limV = self.frame_ch1.set_limV_e.get()
        limC = self.frame_ch1.set_limC_e.get()
        message = command.set_channel(channel,volt,cur,limV,limC)#return volt+cur+limV+limC
        try:
            tcp_client.client_socket.send(message.encode())
        except:
            print("setch1: failed to send message")

    def set_ch2(self):
        channel = "2"
        volt = self.frame_ch2.set_volt_e.get()
        cur = self.frame_ch2.set_cur_e.get()
        limV = self.frame_ch2.set_limV_e.get()
        limC = self.frame_ch2.set_limC_e.get()
        message = command.set_channel(channel,volt,cur,limV,limC)#return channel+volt+cur+limV+limC
        try:
            tcp_client.client_socket.send(message.encode())
        except:
            print("setch2: failed to send message")

    def set_ch3(self):
        channel = "3"
        volt = self.frame_ch3.set_volt_e.get()
        cur = self.frame_ch3.set_cur_e.get()
        limV = self.frame_ch3.set_limV_e.get()
        limC = self.frame_ch3.set_limC_e.get()
        message = command.set_channel(channel,volt,cur,limV,limC)#return volt+cur+limV+limC
        try:
            tcp_client.client_socket.send(message.encode())
        except:
            print("setch3: failed to send message")

    
    


if __name__ == "__main__":
    app = App()
  
    app.mainloop()