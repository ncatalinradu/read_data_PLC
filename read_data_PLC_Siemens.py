import snap7

IP = '192.168.0.19' #ip PLC
RACK = 0  #rack PLC
SLOT = 1  # Slot PLC
plc = snap7.client.Client()
plc.connect(IP,RACK,SLOT)

state = plc.get_cpu_state() #Read state run/stop/error
print(f'State:{state}')

DB_nr = 1
Start = 0
Size = 4

db = plc.db_read(DB_nr, Start, Size)

