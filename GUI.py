import customtkinter
import tcp_client


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
fontname=("TkHeadingFont", 20)
#tlacitko connect a disconnect
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
        self.textbox = customtkinter.CTkTextbox(self,height=120,width=150)
        self.textbox.grid(row=1, column=0,columnspan=2, padx=5, pady=5,sticky="nsew")
        #self.connection_button = customtkinter.CTkButton(self,text="connect",command=tcp_client.client_program)
        #self.connection_button.grid(row=1,column=2)
        #ch1
        self.frame_ch1 = Channel(self,width=80,height=150)
        self.frame_ch1.grid(row=2,column=0,padx=10,pady=10)
        self.set_button_ch1 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=tcp_client.set_ch1)
        self.set_button_ch1.grid(row=3,column=0,sticky="w",padx=5)
        self.get_button_ch1 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch1.grid(row=3,column=0,padx=30,pady=5,sticky="e")
        #ch2
        self.frame_ch2 = Channel(self,width=80,height=150)
        self.frame_ch2.grid(row=2,column=1,padx=10,pady=10)
        self.set_button_ch2 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=tcp_client.set_ch2)
        self.set_button_ch2.grid(row=3,column=1,sticky="w",padx=5)
        self.get_button_ch2 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch2.grid(row=3,column=1,padx=30,pady=5,sticky="e")
        #ch3
        self.frame_ch3 = Channel(self,width=80,height=150)
        self.frame_ch3.grid(row=2,column=2,padx=10,pady=10)
        self.set_button_ch3 = customtkinter.CTkButton(self,text="SET",width=100,fg_color="red",command=tcp_client.set_ch3)
        self.set_button_ch3.grid(row=3,column=2,sticky="w",padx=5)
        self.get_button_ch3 = customtkinter.CTkButton(self,text="GET",width=100)
        self.get_button_ch3.grid(row=3,column=2,padx=30,pady=5,sticky="e")
     
    def set_ch1(self):
        self.channel = "1"
        self.volt = self.frame_ch1.set_volt_e.get()
        self.cur =self.frame_ch1.set_cur_e.get()
        self.limV = self.frame_ch1.set_limV_e.get()
        self.limC = self.frame_ch1.set_limC_e.get()
        tcp_client.client_program

    def set_ch2(self):
        self.channel = "2"
        self.volt = self.frame_ch1.set_volt_e.get()
        self.cur =self.frame_ch1.set_cur_e.get()
        self.limV = self.frame_ch1.set_limV_e.get()
        self.limC = self.frame_ch1.set_limC_e.get()
        #print(volt,cur,limV,limC) 
       
    def set_ch3(self):
        self.channel = "3"
        self.volt = self.frame_ch1.set_volt_e.get()
        self.cur =self.frame_ch1.set_cur_e.get()
        self.limV = self.frame_ch1.set_limV_e.get()
        self.limC = self.frame_ch1.set_limC_e.get()
        #print(volt,cur,limV,limC)



if __name__ == "__main__":
    app = App()
    #app.channel1()
    #app.channel2()
    #app.channel3()
    app.mainloop()