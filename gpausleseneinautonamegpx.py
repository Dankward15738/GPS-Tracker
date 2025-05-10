#!/usr/bin/python3#
"""
Programm speichert gps-Daten in einer csv-Datei ab.
Der Dateiname beinhaltet auch das Datum.
Format: 'gpsyyyy-mm-dd' + Extention
"""
from time import sleep
import serial
import os
try:
    ser=serial.Serial("/dev/ttyACM0",9600)
    
except:
    if os.path.exists('/media/dankward/DATA/speicher.txt'):
        with open('/media/dankward/DATA/speicher.txt','r')as file:
            dateiname=file.read()
            os.remove('/media/dankward/DATA/speicher.txt')
            with open(dateiname,'a') as file:
                file.write("  </trkseg>\r\n")
                file.write(" </trk>\r\n")
                file.write("</gpx>\r\n")
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
                #2011-01-16T23:59:01Z
                datum=liste[9][4:6]+"-"+liste[9][2:4]+"-"+liste[9][0:2]
                if os.path.exists('/media/dankward/DATA/gps'+datum+'.gpx'):
                    pass
                else:
                    with open('/media/dankward/DATA/speicher.txt','w')as file:
                        file.write('/media/dankward/DATA/gps'+datum+'.gpx')
                    with open('/media/dankward/DATA/gps'+datum+'.gpx','a')as file:
                        text="<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\r\n"\
                                +"<gpx xmlns=\"http://www.topografix.com/GPX/1/1\" version=\"1.1\" creator=\"Wikipedia\"\r\n"\
                                +  "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"\
                                +"xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\r\n"
                        file.write(text)
                        file.write(" <trk>\r\n")
                        file.write("  <trkseg>\r\n")
                h=liste[1][0:2]
                m=liste[1][2:4]
                s=liste[1][4:6]
                uhrzeit=h+":"+m+":"+s
                now=datum+"T"+uhrzeit+"Z"
                time="<time>"+now+"</time>\r\n"
                print(time)

                #print(h+":"+m+":"+s)
                #print(tag)

                if liste[2]=="A":
                    lat=liste[3][0:2]
                    
                   #print(lat)
                    latm=liste[3][2:9]
                    latitude =str(int(lat)+float(latm)/60)
                    print("Breite: "+lat+"  "+latm+" "+liste[4])
                    print(latitude)
                    lon=liste[5][0:3]
                   #print(lat)
                    lonm=liste[5][3:10]
                    longitude=str(int(lon)+float(lonm)/60)
                    print("Laenge: "+lon+"  "+lonm+" "+liste[6])
                    print(longitude)
                    trackpoint="    <trkpt lat=\""+latitude+"\" lon=\""+longitude+"\">\r\n"\
                                +"     "+time+"    </trkpt>\r\n"
                    print (trackpoint)
                    try:
                        with open('/media/dankward/DATA/gps'+datum+'.gpx','a')as file:
                                  file.write(trackpoint)
                    except:
                        with open('/home/dankward/DATA/gps'+datum+'.gpx','a')as file:
                                  file.write(trackpoint)
                        

                    try:
                       with open('/media/dankward/DATA/gps'+datum+'.csv','a') as file:
                           zeile = tag+","+h+","+m+","+s+","+lat+","+latm+","+lon+","+lonm+"\r\n"
                           file.write(zeile)
                    except FileNotFoundError:
                        with open('/home/dankward/gps'+datum+'.csv','a') as file:
                           zeile = tag+","+h+","+m+","+s+","+lat+","+latm+","+lon+","+lonm+"\r\n"
                           file.write(zeile)
except:
    pass


