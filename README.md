Die Datei 'gpsauslesenein.py' enhält einen einfachen Code in Python3, mit dem man eine GPS-Maus an einem Raspberry Pi 3+ auslesen kann. Aus den Daten wird eine CSV-Datei (gps.csv) mit Datum, Weltuhrzeit, Breitengrad und Längengrad generiert bzw. fortgeführt und auf einen USB-Stick mit dem Namen DATA abgespeichert.
Das Skript kann reglmäßig mit cron aufgerufen werden.

Die Datei 'gpausleseneinautoname.py' unterscheidet sich von der ersten Datei dadurch, dass jetzt der Dateiname auch das Datum der Aufzeichnung enthält. Damit wird jeden Tag eine neue csv-Datei angelegt und nicht die bestehende einfach erweitert.
Das Script sollte ebenfalls mit cron aufgerufen werden.

Die Datei 'gpausleseneinautonamegpx.py' ist schließlich ein Script, das auf dem Stick mit dem Namen DATA sowohl eine CSV-Datei erstellt, bzw. erweitert als auch eine einfache gpx-Datei. Bei der ersten Aufzeichnung wird der Kopf der gpx-Datei erstellt und beim Herausziehen des Steckers der GPS-Maus aus dem USB-Port des Rasberry Pi's wird das Fußende der GPX-Datei erstellt und damit diese abgeschlossen.

Der kürzeste Abstand, mit dem man mit cron jobs ausführen kann, ist 1 Minute. Mit dem bash-Script gpsauslesen.sh habe ich den Abstand auf 10 Sekunden verkürzt.
