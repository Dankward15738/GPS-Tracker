#!/usr/bin/python3#
"""
Programm speichert gps-Daten in einer csv-Datei ab.
Der Dateiname beinhaltet auch das Datum.
Format: 'gpsyyyy-mm-dd' + Extention
"""
from time import sleep
import serial

ser=serial.Serial("/dev/ttyACM0",9600)
try:
    received_data = ser.read(500)
    #print(received_data)
    text=received_data.decode("ascii")
    #print(text)
    text=text.split("$")
    for teiltext in text:
        if teiltext[0:5]=="GPRMC":
            liste=teiltext.split(",") #vollstaendige Datensaetze herausfiltern
            if len(liste)>12:
                print(teiltext)
                tag=liste[9][0:2]+"."+liste[9][2:4]+"."+liste[9][4:6]
                dateiname="gps"+liste[9][4:6]+"-"+liste[9][2:4]+"-"+liste[9][0:2]
                h=liste[1][0:2]
                m=liste[1][2:4]
                s=liste[1][4:6]

                print(h+":"+m+":"+s)
                print(tag)

                if liste[2]=="A":
                    lat=liste[3][0:2]
                   #print(lat)
                    latm=liste[3][2:9]
                    print("Breite: "+lat+"  "+latm+" "+liste[4])
                    lon=liste[5][0:3]
                   #print(lat)
                    lonm=liste[5][3:10]
                    print("Laenge: "+lon+"  "+lonm+" "+liste[6])
                    try:
                        # dankward sollte durch den Namen des home-Verzeichnis ersetzt werden.
                       with open('/media/dankward/DATA/'+dateiname+'.csv','a') as file:
                           zeile = tag+","+h+","+m+","+s+","+lat+","+latm+","+lon+","+lonm+"\r\n"
                           file.write(zeile)
                    except FileNotFoundError:
                        # dankward sollte durch den Namen des home-Verzeichnis ersetzt werden.
                        with open('/home/dankward/'+dateiname+'.csv','a') as file:
                           zeile = tag+","+h+","+m+","+s+","+lat+","+latm+","+lon+","+lonm+"\r\n"
                           file.write(zeile)
except:
    pass

