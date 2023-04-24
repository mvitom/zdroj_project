def set_channel(channel,voltage,current,limitV,limitC):
    channel = f"INST CH{channel}"
    voltage = f";VOLT {voltage}"
    current = f";CURR {current}"
    limitV = f";VOLT:LIM {limitV}"
    limitC = f";CURR:LIM {limitC}"
    return channel + voltage + current + limitV + limitC

# def set_channel(channel,voltage,current,limitV,limitC):
#     set_voltage(channel,voltage)
#     set_current(channel,current)
#     set_limitV(channel,limitV)
#     set_limitC(channel,limitC)

# def get_channel(channel,voltage,current,limitV,limitC):
#     get_voltage(channel,voltage)
#     get_current(channel,current)
#     get_limitV(channel,limitV)
#     get_limitC(channel,limitC)    

# def set_current(channel,current):
#     channel = f"INST CH{channel}"
#     current = f";CURR {current}"
#     return channel + current

# def set_limitV(channel,limitV):
#     channel = f"INST CH{channel}"
#     limitV = f";VOLT:LIM {limitV}"
#     return channel + limitV

# def set_limitC(channel,limitC):
#     channel = f"INST CH{channel}"
#     limitC = f";CURR:LIM {limitC}"
#     return channel + limitC

#####################################

def get_channel(channel):
    channel = f"INST CH{channel}"
    voltage = f";VOLT?"
    current = f";CURR?"
    limitV = f";VOLT:LIM?"
    limitC = f";CURR:LIM?"
    return channel + current + limitV + limitC + voltage

# def get_voltage(channel):
#     channel = f"INST CH{channel}"
#     voltage = f";VOLT"
#     return channel + voltage

# def get_current(channel):
#     channel = f"INST CH{channel}" 
#     current = f";CURR?"
#     return channel + current

# def get_limitV(channel):
#     channel = f"INST CH{channel}"
#     limitV = f";VOLT:LIM?"
#     return channel + limitV

# def get_limitC(channel):
#     channel = f"INST CH{channel}"
#     limitC = f";CURR:LIM?"
#     return channel + limitC
    