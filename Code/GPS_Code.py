PYTHON CODE FOR EXTRACTING GPS RAW DATA IN STATIC AND DYNAMIC MODE

import serial

port = "/dev/ttyAMA0"

def parseGPS(data):
    # print "raw:", data     #prints raw data
    if data[0:6] == "$GPRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            print("no satellite data available")
            return
        print("---Parsing GPRMC---")
        time = sdata[1][0:2] + ":"; + sdata[1][2:4] + ":" + sdata[1][4:6]     #Time
        lat = decode(sdata[3])     #Latitude
        dirLat = sdata[4]     #Latitude Direction N/S
        lon = decode(sdata[5])     #Longitute
        dirLon = sdata[6]     #Longitude Direction E/W
        speed = sdata[7]     #Speed in K
        trCourse = sdata[8]     #True Course
        date = sdata[9][0:2] + "/" + sdata[9][2:4] + &quot;/&quot; + sdata[9][4:6]     #Date
        magvar= sdata[10]     #Magnetic Varition
        print("time : %s, latitude : %s(%s), longitude : %s(%s), speed : %s, True Course : %s, Date : %s, Magnetic Variation: %S" %(time, lat, 
        dirLat, lon, dirLon, speed, trCourse, date, magvar))
    elif data[0:6] == "$GPGSV":
        gdata = data.split(",")
        sv = gdata[3]     #No.SVS
        prn = gdata[4]     #SV PRN
        snr= gdata[7]     #SNR
        print("Satellite visible: %s, PRN: %s, SNR: %s" %(sv,prn,snr))
        
def decode(coord):
    # Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + "deg" + min + "." + tail + "min";
    
print("Receiving GPS data")
ser = serial.Serial(port, baudrate=9600, timeout=0.5)
# serial=serial.Serial("dev/ttyAMA0", baudrate=9600, timeout=0.5)
while True:
    data = ser.readline()
    parseGPS(data)
