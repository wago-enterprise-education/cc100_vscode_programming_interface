# Created by Konrad Holsmoelle, Mattis Schrade
# konrad.holsmoelle@wago.com
# mattis.schrade@wago.com

# Output calibration from: https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py
def readCalibriationData():
    """
    Reads out the data of the calibrationdata from the CC100
    """
    global calib_data
    filename="/etc/calib"
    try:
        file = open(name = filename, mode = "r")
    except:
        print("Fehler! Pfad nicht vorhanden.")
    calib_data = file.readlines()[1:]    
    file.close()

def getCalibrationData(value):
    """
    Returns the calibrationdata for the required row of the table
    """
    return calib_data[value].rstrip().split(' ', 4)

def calcCalibrate(val_uncal, calib):
    """
    Calcutes the value of the voltage for the required output
    """
    x1=int(calib[0])
    y1=int(calib[1])
    x2=int(calib[2])
    y2=int(calib[3])

    val_cal=(y2-y1)*int(val_uncal-x1)
    val_cal=val_cal/(x2-x1)
    val_cal=val_cal+y1

    return int(val_cal)

def calibrateOut(iVoltage, iOutput):
    """
    iVoltage: Voltage to be applied to the input
    iOutput: Output which should be switched

    Returns the value which is to be written with the specified voltage
    """
    
    readCalibriationData()
    # Takes a different set of calibration data depending on the output
    if iOutput == 1:
        cal_ao = getCalibrationData(4)
    elif iOutput == 2:
        cal_ao = getCalibrationData(5)
    # Calculates and returns the value
    return calcCalibrate(iVoltage, cal_ao)

def calibrateIn(iValue, iInput):
    """
    iValue: Value given for the file from the output
    iInput: Input at which the value was read
    """
    readCalibriationData()
    if iInput == 1:
        cal_ai = getCalibrationData(2)
    if iInput == 2:
        cal_ai = getCalibrationData(3)
    #Returns the calculated value 
    return calcCalibrate(iValue, cal_ai)