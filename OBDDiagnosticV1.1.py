# -*- coding: utf-8 -*-
"""
Spyder Editor

This s a temporary script

"""

import obd

thisPORTS = obd.OBD(ports)
connection = obd.OBD("/dev/rfcomm0")

ver = connection.query(obd.commands.ELM_VERSION)
print ver.value
#volt = connection.query(obd.commands('ELM_VOLTAGE'))
status = connection.query(obd.commands.STATUS)
trouble  = connection.query(obd.commands.GET_DTC)
dtc_Stat = connection.query(obd.commands.TIME_SINCE_DTC_CLEARED)
cat1 = connection.query(obd.commands.CATALYST_TEMP_B1S1) 

print(thisPORTS)
print ("Status :",status.value, status.unit)
print ("Trouble Codes :",trouble.value, trouble.unit)
print ("Last Cleared: ", dtc_Stat.value, dtc_Stat.unit)
print ("cat1: ", cat1.value, cat1.unit)





