Die Datei 'gpsauslesenein.py' enhält einen einfachen Code in Python3, mit dem man eine GPS-Maus an einem Raspberry Pi 3+ auslesen kann. Aus den Daten wird eine CSV-Datei (gps.csv) mit Datum, Weltuhrzeit, Breitengrad und Längengrad generiert bzw. fortgeführt und auf einen USB-Stick mitdem Namen DATA abgespeichert.
Das Skript kann reglmäßig mit cron aufgerufen werden.

Die Datei 'gpausleseneinautoname.py' unterscheidet sich von der ersten Datei dadurch, dass jetzt der Dateiname auch das Datum der Aufzeichnung enthält. Damit wird jeden Tag eine neue csv-Datei angelegt und nicht die bestehende einfach erweitert.
Das Script sollte ebenfalls mit cron aufgerufen werden.
