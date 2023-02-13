# Created by Konrad Holsmölle
# konrad.holsmoelle@wago.com

# Control of input and output from https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py

import Cal
from enum import Enum

# Enum Types for the inputs and outputs:
DigitalOutputs = Enum("", ["DO1", "DO2", "DO3" , "DO4"])
DO1 = DigitalOutputs.DO1
DO2 = DigitalOutputs.DO2
DO3 = DigitalOutputs.DO3
DO4 = DigitalOutputs.DO4

DigitalInputs = Enum("", ["DI1", "DI2", "DI3" , "DI4" , "DI5" , "DI6" , "DI7" , "DI8"])
DI1 = DigitalInputs.DI1
DI2 = DigitalInputs.DI2
DI3 = DigitalInputs.DI3
DI4 = DigitalInputs.DI4
DI5 = DigitalInputs.DI5
DI6 = DigitalInputs.DI6
DI7 = DigitalInputs.DI7
DI8 = DigitalInputs.DI8

AnalogOutputs = Enum("", ["AO1", "AO2"])
AO1 = AnalogOutputs.AO1
AO2 = AnalogOutputs.AO2

AnalogInputs = Enum("", ["AI1", "AI2"])
AI1 = AnalogInputs.AI1
AI2 = AnalogInputs.AI2

# Functions to control and read the inputs and outputs.
def digitalWrite(xStatus: bool, iAusgang: DigitalOutputs):
    """
    xStatus: Status, which the selected output should be set to
    iAusgang: Digital output to be switched

    Function switches the output to the specified status.
    Function does not check the current status of the output
    """

    # Check if the type of the input is correct
    if(type(iAusgang) == DigitalOutputs & type(xStatus) == bool):
        # Changing iAusgang to the desired Integer
        if iAusgang == DO1:
            iAusgang = 1
        elif iAusgang == DO2:
            iAusgang = 2
        elif iAusgang == DO3:
            iAusgang = 3
        elif iAusgang == DO4:
            iAusgang = 4

        # Reading the outputs current sate to calculate the new value in the file
        fname="/home/ea/dout/DOUT_DATA"
        datei = open(fname, "r")
        schaltung = int(datei.read())
        datei.close()

        # Addition or rather subtraction to the current state to switch the corresponding output
        # Least Significant Bit corresponds to digital output 1, the 4th bit corresponds to output 8
        # A number from 0 to 15 is written to the file
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
            print("Output not correct")
        # Writes the calculated value for the new configuration to the file on the CC100


        datei = open(fname, "w")
        datei.write(str(schaltung))
        datei.close()
        # Returns True after completion
        return True
    else:
	    raise TypeError("iAusgang is not of type DigitalOutputs or xStatus is not of type bool")

def analogWrite(iSpannung: int, iAusgang: AnalogOutputs):
    """
    iSpannung: Voltage to be switched on the analog output given in mV
    iAusgang: Analog output to be switched

    Function switches the analog output to the specified voltage
    """
    # Check if the type of the input is correct
    if(type(iAusgang) == AnalogOutputs & type(iSpannung) == int):

        # Check if if iSpannung is in the range of 0 to 10000
        if(iSpannung >= 0 & iSpannung <= 10000):

            # Changing iAusgang to the desired Integer
            if iAusgang == AO1:
                iAusgang = 1
            elif iAusgang == AO2:
                iAusgang = 2
            

            iSpannung = Cal.calibrateOut(iSpannung, iAusgang)
            if iSpannung < 0:
                iSpannung = 0
            # Activates the analog outputs on the CC100 by writing
            AO1_POWER_FILE="/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_powerdown"
            f=open(AO1_POWER_FILE, "w")
            f.write("0")
            f.close()
            AO2_POWER_FILE="/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_powerdown"
            datei=open(AO2_POWER_FILE, "w")
            datei.write("0")
            datei.close()

            # Writes the value, taken from the calibration for the corresponding output, for the voltage to the file for the output
            # When turning off, a zero is written to the file
            # Calibration with calibration.py
            if iAusgang == 1:
                AO1_VOLTAGE_FILE="/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_raw"
                datei=open(AO1_VOLTAGE_FILE, "w")
                # Change for the voltage of output 1 in the following line

                datei.write(str(iSpannung))
                datei.close()
            if iAusgang == 2:
                AO1_VOLTAGE_FILE="/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_raw"
                datei=open(AO1_VOLTAGE_FILE, "w")
                # Change for the voltage of output 1 in the following line
                datei.write(str(iSpannung))
                datei.close()
        else:
            print("iSpannung is not in the range of 0 to 10000")
    else:
	    raise TypeError("iAusgang is not of type AnalogOutputs or xStatus is not of type bool")

def digitalRead(iEingang: DigitalInputs):
    """
    iEingang: Index of the digital input to be read out

    Reads the input
    Returns True or False depending on the status
    """

    # Check if the type of the input is correct
    if(type(iEingang) == DigitalInputs):

        # Changing iAusgang to the desired Integer
        if iEingang == DI1:
            iEingang = 1
        if iEingang == DI2:
            iEingang = 2
        if iEingang == DI3:
            iEingang = 3
        if iEingang == DI4:
            iEingang = 4
        if iEingang == DI5:
            iEingang = 5
        if iEingang == DI6:
            iEingang = 6
        if iEingang == DI7:
            iEingang = 7
        if iEingang == DI8:
            iEingang = 8
        
        # Reads the state of the digital inputs on the CC100
        fname="/home/ea/din/din"
        datei = open (fname, "r")
        dig_in = datei.readline()
        datei.close()
        # Formats the current state into an 8-digit binary code
        dig_in = int (dig_in)
        dig_in_bin=format(dig_in, "08b")
        # Calculates the position of the bit from the desired input
        iBit = 8 - iEingang
        # Returns the value of the state of the desired input
        if int(dig_in_bin[iBit])==1:
            return True
        else:
            return False
    else:
	    raise TypeError("iEingang is not of type DigitalInputs")

def digitalReadWait(iEingang: DigitalInputs, xZustand: bool):
    """
    iEingang: Index of the input to be checked
    xZustand: State to be queried at the input

    Reads the specified input until the desired state is reached and then returns True.
    Function runs until the state is reached.
    """

    # Check if the type of the input is correct
    if(type(iEingang) == DigitalInputs & type(xZustand) == bool):

        # Changing iAusgang to the desired Integer
        if iEingang == DI1:
            iEingang = 1
        if iEingang == DI2:
            iEingang = 2
        if iEingang == DI3:
            iEingang = 3
        if iEingang == DI4:
            iEingang = 4
        if iEingang == DI5:
            iEingang = 5
        if iEingang == DI6:
            iEingang = 6
        if iEingang == DI7:
            iEingang = 7
        if iEingang == DI8:
            iEingang = 8
        eingangSchleife = True
        # Converts the given state into a number
        if xZustand:
            xZustand = 1
        else:
            xZustand = 0
        # Checks the input as long as it reaches the given state
        # Then ends the loop and returns True
        while eingangSchleife:
            if digitalRead(iEingang)==xZustand:
                eingangSchleife = False
                return True
    else:
	    raise TypeError("iEingang is not of type DigitalInputs")

def analogRead(iEingang: AnalogInputs):
    """
    iEingang: Index of the input to be read out

    Reads the input and returns the calibrated value in mV.
    """

    # Check if the type of the input is correct
    if(type(iEingang) == AnalogInputs):

        # Changing iAusgang to the desired Integer
        if iEingang == AI1:
            iEingang = 1
        elif iEingang == AI2:
            iEingang = 2

        # Selects the file that matches the input
        if iEingang == 1:
            fname="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage3_raw"
        if iEingang == 2:
            fname="/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage0_raw"
        # Opens the file and reads the value in it
        f=open(fname, "r")
        iSpannung=int(f.readline())
        f.close()
        # Calibrates the value and returns it
        return(Cal.calibrateIn(iSpannung, iEingang))
    else:
	    raise TypeError("iEingang is not of type AnalogInputs")