#Erstellt von Konrad Holsmoelle
#konrad.holsmoelle@wago.com
#Ansteuern der Ein- und Ausgaenge aus https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

import Cal
import time
#Funktionen zum Ansteuern und Auslesen der Ein- und Ausgaenge
def digitalWrite(xStatus, iAusgang):
    """
    xStatus: Status, auf welchen der ausgewaehlte Ausgang gesetzt werden soll
    iAusgang: Digitaler Ausgang welcher geschaltet werden soll

    Funktion schaltet den Ausgang auf den angegeben Status.
    Funktion ueberprueft nicht den aktuellen Status des Ausgangs.
    """
    #Auslesen des aktuell geschalteten Zustandes fuer die Berechnung des neuen Wertes in der Datei
    fname="/sys/kernel/dout_drv/DOUT_DATA"
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
    #Schreibt den fuer die neue Konfiguration errechneten Wert in die Datei auf dem CC100 
    datei = open(fname, "w")
    datei.write(str(schaltung))
    datei.close()
    #Gibt True nach Abschluss zurueck
    return True

def analogWrite(iSpannung, iAusgang):
    """
    iSpannung: Spannung welche am analogen Ausgang geschaltet werden soll
    iAusgang: Ausgang, welcher geschaltet werden soll

    Funktion schaltet den analogen Ausgang auf die angegebenen Spannung
    """
    iSpannung = Cal.calibrateOut(iSpannung, iAusgang)
    if iSpannung < 0:
        iSpannung = 0
    #Aktiviert die analogen Ausgaenge am CC100 durch schreiben 
    AO1_POWER_FILE="/sys/bus/iio/devices/iio:device0/out_voltage1_powerdown"
    f=open(AO1_POWER_FILE, "w")
    f.write("0")
    f.close()
    AO2_POWER_FILE="/sys/bus/iio/devices/iio:device1/out_voltage2_powerdown"
    datei=open(AO2_POWER_FILE, "w")
    datei.write("0")
    datei.close()
    #Schreibt den aus der Kalibrierung fuer den passenden Ausgang entnommenen Wert fuer die Spannung in die Datei fuer den Ausgang
    #Beim ausschalten wird eine Null in die Datei geschrieben
    #Kalibrierung mit calibration.py
    if iAusgang == 1:
        AO1_VOLTAGE_FILE="/sys/bus/iio/devices/iio:device0/out_voltage1_raw"
        datei=open(AO1_VOLTAGE_FILE, "w")
        #aenderung fuer die Spannung von Ausgang 1 in der folgenden Zeile
        datei.write(str(iSpannung))
        datei.close()
    if iAusgang == 2:
        AO1_VOLTAGE_FILE="/sys/bus/iio/devices/iio:device1/out_voltage2_raw"
        datei=open(AO1_VOLTAGE_FILE, "w")
        #aenderung fuer die Spannung von Ausgang 1 in der folgenden Zeile
        datei.write(str(iSpannung))
        datei.close()

def digitalRead(iEingang):
    """
    iEingang: Nummer des digitalen Eingangs welcher ausgelesen werden soll

    Liest den Eingang aus
    Gibt True oder False entsprechend dem Status zurueck
    """
    #Liest den Zustand der digitalen Eingaenge auf dem CC100
    fname="/sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0/din"
    datei = open (fname, "r")
    dig_in = datei.readline()
    datei.close()
    #Formt den aktuellen Zustand in einen 8-Stelligen binaer Code um
    dig_in = int (dig_in)
    dig_in_bin=format(dig_in, "08b")
    #Errechnet die Position des Bits vom gesuchten Eingang
    iBit = 8 - iEingang
    #Gibt den Wert von dem Zustand des gesuchten Einganges zurueck
    if int(dig_in_bin[iBit])==1:
        return True
    else:
        return False

def digitalReadWait(iEingang, xZustand):
    """
    iEingang: Nummer des Eingangs, welcher ueberprueft werden soll
    xZustand: Zustand, welcher an dem Eingang abgefragt werden soll

    Liest den angegebenen Eingang solange aus, bis der Zustand erreicht ist und gibt dann True zurueck.
    Funktion laeuft bis der Zustand erreicht ist.
    """
    eingangSchleife = True
    #Wandelt den angegebenen Zustand in eine Zahl um
    if xZustand:
        xZustand = 1
    else:
        xZustand = 0
    #Fragt solange den Eingang ab, bis dieser den angegebenen Zustand erreicht hat
    #Beendet dann die Schleife und gibt True zurueck
    while eingangSchleife:
        if digitalRead(iEingang)==xZustand:
            eingangSchleife = False
            return True

def analogRead(iEingang):
    """
    iEingang: Nummer des Eingangs, welcher ausgelesen werden soll

    Liest den Eingang aus und gibt den kalibrierten Wert in mV zurueck.
    """ 
    #Waehlt die fuer den Eingang passende Datei aus
    if iEingang == 1:
        fname="/sys/bus/iio/devices/iio:device3/in_voltage3_raw"
    if iEingang == 2:
        fname="/sys/bus/iio/devices/iio:device3/in_voltage0_raw"
    #oeffnet die Datei und liest die den Wert in dieser aus
    f=open(fname, "r")
    iSpannung=int(f.readline())
    f.close()
    #Kalibriert den Wert und gibt diesen zurueck
    return(Cal.calibrateIn(iSpannung, iEingang))

def delay(iTime):
    iTime = iTime/1000
    time.sleep(iTime)