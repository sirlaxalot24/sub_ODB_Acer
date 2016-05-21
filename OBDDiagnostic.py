# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import obd


ports = obd.scan_serial

obd.debug = True
connection = obd.OBD(ports)

ver = connection.query(obd.commands('ELM_VERSION'))
#volts = connection.query(obd.commands('ELM_VOLTAGE'))
#status = connection.query(obd.commands('STATUS'))
#trouble  = connection.query(obd.commands('GET_DTC'))

print (ports)
#print ("ELM Version :",ver.value, ver.unit)
#print ("ELM Voltage :",volts, volts.value)
#print ("Status :",status.value, status.unit)
#print ("Trouble Codes :",trouble.value, trouble.unit)


#connection = obd.OBD(ports)

#print(connection)


#cmd = obd.commands('Status')

#response = connection.query(cmd)

#print(response.value)
#print(response.unit)