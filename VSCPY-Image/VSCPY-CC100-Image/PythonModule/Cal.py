#Erstellt von Konrad Holsmölle, Mattis Schrade
#konrad.holsmoelle@wago.com
#mattis.schrade@wago.com

#Kalibrierung der Ausgänge aus https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

def readCalibriationData():
    """
    Liest die Daten aus Kalibrierungsdatei auf dem CC100
    """
    global calib_data
    fname="/home/ea/cal/calib"
    f = open(fname, "r")
    #Liest die Daten aber Überspringt die Kopfzeile
    calib_data=f.readlines()[1:]
    f.close()

def getCalibrationData(value):
    """
    Gibt die Klalibrierungs Informationen für die gefragte Zeile der Tabelle zurück
    """
    return calib_data[value].rstrip().split(' ', 4)

def calcCalibrate(val_uncal, calib):
    """
    Errechnet den Wert für den Ausgang für die gewünschte Spannung
    """
    x1=int(calib[0])
    y1=int(calib[1])
    x2=int(calib[2])
    y2=int(calib[3])

    val_cal=(y2-y1)*int(val_uncal-x1)
    val_cal=val_cal/(x2-x1)
    val_cal=val_cal+y1

    return int(val_cal)

def calibrateOut(iSpannung: int, iAusgang: int):
    """
    iSpannung: Spannung welche an dem Ausgang anliegen soll
    iAusgang: Ausgang welcher geschaltet werden soll

    Gibt den Wert, welcher für die angegebenen Spannung am CC100 geschrieben werden muss.
    """
    
    readCalibriationData()
    #Nimmt je nach Ausgang einen anderen Satz Kalibrierungsdaten
    if iAusgang == 1:
        cal_ao = getCalibrationData(4)
    elif iAusgang == 2:
        cal_ao = getCalibrationData(5)
    #Berechnet und gibt den Wert zurück
    return calcCalibrate(iSpannung, cal_ao)

def calibrateIn(iWert: int, iEingang: int):
    """
    iWert: Aus der Datei für den Ausgang gegebenen Wert
    iEingang: Eingang an welchem der Wert ausgelesen wurde
    """
    readCalibriationData()
    #Nimmt je nach Eingang einen anderen Satz Kalibrierungsdaten
    if iEingang == 1:
        cal_ai = getCalibrationData(2)
    if iEingang == 2:
        cal_ai = getCalibrationData(3)
    #Errechnet den zu schreibenden Wert und gibt diesen zurück
    return calcCalibrate(iWert, cal_ai)