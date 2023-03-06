#Erstellt von Konrad Holsmölle, Mattis Schrade
#konrad.holsmoelle@wago.com
#mattis.schrade@wago.com

#Auslesen und schreiben der Ein- und Ausgänge aus https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

import time
import CC100IO 

#Variablen Namen für die genutzten Ausgänge am CC100
#1 und 2 Doppeln sich, da Motor1 durch den Analogen Ausgang gesteuert wird
Motor1_G = 1
Motor1_U = 2
Motor2_H = 1
Motor2_R = 2
Motor3_Auf = 3
Motor3_Zu = 4

#Variablen Namen für die digitalen Eingänge 1 bis 6 welche genutzt werden
#xS1 bis xS4 für die Fischertechnikschalter 1 bis 4
#DI1 und DI2 für die Schalter auf der Schiene
xS1 = 1
xS2 = 2
xS3 = 3
xS4 = 4
DI1 = 5
DI2 =6

def oeffnen():
    """
    Öffnet die Klemme des Roboters
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis der Endschalter gedrückt ist
    CC100IO.digitalWrite(True, Motor3_Auf)
    if CC100IO.digitalReadWait(xS3, False):
        CC100IO.digitalWrite(False, Motor3_Auf)
        return True

def schliessen():
    """
    Schließt die Klemme des Roboters
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis zum Ablauf der Zeit
    CC100IO.digitalWrite(True, Motor3_Zu)
    time.sleep(2.2)
    CC100IO.digitalWrite(False, Motor3_Zu)
    return True

def armHoch():
    """
    Fährt den Arm Hoch
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis der Endschalter gedrückt ist
    CC100IO.digitalWrite(True, Motor2_H)
    if CC100IO.digitalReadWait(xS2, False):
        CC100IO.digitalWrite(False, Motor2_H)
        return True

def armRunter():
    """
    Fährt den Arm Runter
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis zum Ablauf der Zeit
    CC100IO.digitalWrite(True, Motor2_R)
    time.sleep(3.12)
    CC100IO.digitalWrite(False, Motor2_R)
    return True

def aufnehmen():
    """
    Führt den Bewegungsablauf zum aufnehemen eines Gegenstandes aus
    """
    oeffnen()
    armRunter()
    schliessen()
    armHoch()
    
def ablegen():
    """
    Führt den Bewegungsablauf zum ablegen eines Gegenstandes aus
    """
    armRunter()
    oeffnen()
    armHoch()

def drehung_G():
    """
    Dreht den Arm gegen den Uhrzeigersinn
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis zum Ablauf der Zeit
    CC100IO.analogWrite(True, Motor1_G)
    time.sleep(5.5)
    CC100IO.analogWrite(False, Motor1_G)
    return True

def drehung_U():
    """
    Dreht den Arm im Uhrzeigersinn
    Gibt nach Ausführung True zurück
    """
    #Schaltet den Motor an, bis der Endschalter gedrückt ist
    CC100IO.analogWrite(True, Motor1_U)
    if CC100IO.digitalReadWait(xS1, False):
        CC100IO.analogWrite(False, Motor1_U)
        return True

def main():
    """
    Nimmt einen Gegenstand bei L1 auf und legt ihn bei L2 ab
    Fährt in die Startposition zurück
    Startet die Bewegung durch aktivieren von Schalter DI1
    """
    if CC100IO.digitalReadWait(DI1, True):
        aufnehmen()
        drehung_G()
        ablegen()
        drehung_U()

def Uhrsprung():
    """
    Fährt den Arm in den Ursprungszustand
    """
    armHoch()
    oeffnen()
    drehung_U()

#Führt die Main-Funktion aus bis DI2 zum Start eines Zyklus aktiviert ist
#Beendet dann das Programm
Uhrsprung()
while True:
    if CC100IO.digitalRead(DI2):
        exit()
    else:
        main()
