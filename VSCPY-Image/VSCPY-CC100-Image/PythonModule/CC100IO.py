#Erstellt von Konrad Holsmölle
#konrad.holsmoelle@wago.com
#Ansteuern der Ein- und Ausgänge aus https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

import Cal
#Funktionen zum ansteuern und auslesen der Ein- und Ausgänge
def digitalWrite(xStatus: bool, iAusgang: int):
    """
    xStatus: Status, auf welchen der ausgewählte Ausgang gesetzt werden soll
    iAusgang: Digitaler Ausgang welcher geschaltet werden soll

    Funktion schaltet den Ausgang auf den angegeben Status.
    Funktion überprüft nicht den aktuellen Status des Ausgangs.
    """
    #Auslesen des aktuelle geschalteten Zustandes für die Berechnung des neuen Wertes in der Datei
    fname="/home/ea/dout/DOUT_DATA"
    datei = open(fname, "r")
    schaltung = int(datei.read())
    datei.close()
    #Addition bzw. Subtraktion zum aktuellen Zustand um den entsprechenden Ausgang zu schalten
    #Least Significant Bit entspricht dabei digitalem Ausgang 1, das 4. Bit entspricht Ausgang 8
    #In die Datei wird eine Zahl von 0 bis 15 geschrieben
    if iAusgang == 1:
        if xStatus:
            schaltung = schaltung + 1
        else:
            schaltung = schaltung - 1
    elif iAusgang == 2:
        if xStatus:
            schaltung = schaltung + 2
        else:
            schaltung = schaltung - 2
    elif iAusgang == 3:
        if xStatus:
            schaltung = schaltung + 4
        else:
            schaltung = schaltung - 4
    elif iAusgang == 4:
        if xStatus:
            schaltung = schaltung + 8
        else:
            schaltung = schaltung - 8
    else:
        print("Ausgang nicht korrekt")
    #Schhreibt den für die neue Konfiguration errechneten Wert in die Datei auf dem CC100 
    datei = open(fname, "w")
    datei.write(str(schaltung))
    datei.close()
    #Gibt True nach Abschluss zurück
    return True

def analogWrite(iSpannung: int, iAusgang: int):
    """
    iSpannung: Spannung welche am analogen Ausgang geschaltet werden soll
    iAusgang: Ausgang, welcher geschaltet werden soll

    Funktion schaltet den analogen Ausgang auf die angegebenen Spannung
    """
    iSpannung = Cal.calibrateOut(iSpannung, iAusgang)
    if iSpannung < 0:
        iSpannung = 0
    #Aktiviert die analogen Ausgänge am CC100 durch schreiben 
    AO1_POWER_FILE="/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_powerdown"
    f=open(AO1_POWER_FILE, "w")
    f.write("0")
    f.close()
    AO2_POWER_FILE="/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_powerdown"
    datei=open(AO2_POWER_FILE, "w")
    datei.write("0")
    datei.close()
    #Schreibt den aus der Kalibrierung für den passenden Ausgang entnommenen Wert für die Spannung in die Datei für den Ausgang
    #Beim ausschalten wird eine Null in die Datei geschrieben
    #Kalibrierung mit calibration.py
    if iAusgang == 1:
        AO1_VOLTAGE_FILE="/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_raw"
        datei=open(AO1_VOLTAGE_FILE, "w")
        #Änderung für die Spannung von Ausgang 1 in der folgenden Zeile
        datei.write(str(iSpannung))
        datei.close()
    if iAusgang == 2:
        AO1_VOLTAGE_FILE="/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_raw"
        datei=open(AO1_VOLTAGE_FILE, "w")
        #Änderung für die Spannung von Ausgang 1 in der folgenden Zeile
        datei.write(str(iSpannung))
        datei.close()

def digitalRead(iEingang: int):
    """
    iEingang: Nummer des digitalen Eingangs welcher ausgelesen werden soll

    Liest den Eingang aus
    Gibt True oder False entsprechend dem Status zurück
    """
    #Liest den Zustand der digitalen Eingänge auf dem CC100
    fname="/home/ea/din/din"
    datei = open (fname, "r")
    dig_in = datei.readline()
    datei.close()
    #Formt den aktuellen Zustand in einen 8-Stelligen binär Code um
    dig_in = int (dig_in)
    dig_in_bin=format(dig_in, "08b")
    #Errechnet die Position des Bits vom gesuchten Eingang
    iBit = 8 - iEingang
    #Gibt den Wert von dem Zustand des gesuchten Einganges zurück
    if int(dig_in_bin[iBit])==1:
        return True
    else:
        return False

def digitalReadWait(iEingang: int, xZustand: bool):
    """
    iEingang: Nummer des Eingangs, welcher überprüft werden soll
    xZustand: Zustand, welcher an dem Eingang abgefragt werden soll

    Liest den angegebenen Eingang solange aus, bis der Zustand erreicht ist und gibt dann True zurück.
    Funktion läuft bis der Zustand erreicht ist.
    """
    eingangSchleife = True
    #Wandelt den angegebenen Zustand in eine Zahl um
    if xZustand:
        xZustand = 1
    else:
        xZustand = 0
    #Fragt solange den Eingang ab, bis dieser den angegebenen Zustand erreicht hat
    #Beendet dann die Schleife und gibt True zurück
    while eingangSchleife:
        if digitalRead(iEingang)==xZustand:
            eingangSchleife = False
            return True

def analogRead(iEingang: int):
    """
    iEingang: Nummer des Eingangs, welcher ausgelesen werden soll

    Liest den Eingang aus und gibt den kalibrierten Wert in mV zurück.
    """
    #Wählt die für den Eingang passende Datei aus
    if iEingang == 1:
        fname="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage3_raw"
    if iEingang == 2:
        fname="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage0_raw"
    #Öffnet die Datei und liest die den Wert in dieser aus
    f=open(fname, "r")
    iSpannung=int(f.readline())
    f.close()
    #Kalibriert den Wert und gibt diesen zurück
    return(Cal.calibrateIn(iSpannung, iEingang))