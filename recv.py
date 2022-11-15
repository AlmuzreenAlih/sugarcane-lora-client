import base64
import serial
# SerialData = serial.Serial("/dev/ttyUSB0", 9600, timeout = 0.2)
SerialData = serial.Serial("com4", 115200, timeout = 0.2)
# SerialData.setDTR(False)
# time.sleep(1)
# SerialData.flushInput()
# SerialData.setDTR(True)
# time.sleep(2)
# SerialData.write(bytes("2", "utf-8"))
# reading = SerialData.readline().decode("utf-8")
# reading = SerialData.readline().decode("utf-8")
#	 if reading == 'A':
#		 pass

Start = 0
AccString = ""

iii = 0

while True:
    reading = SerialData.readline().decode("utf-8")
    reading = reading.replace('\r\n',"")
    
    try:            
        if Start == 0 and reading[0] == '=':
            print("start")
            Start = 1
        elif Start == 1 and reading[0] == '=':
            print("end", len(AccString))
            f = open("some.txt", "w+")
            f.write(AccString) 
            f.close()
            FinalString = base64.b64decode(AccString)
            f = open("Vvv.jpg", "wb+")
            f.write(FinalString) 
            f.close()
            Start = 0
        elif reading != '\r' and reading != '\n' and reading != '' and reading != '\r\n' and reading != 'Success':               
            iii = iii+1
            iiii = reading.find('==')
            if len(reading)!=250:
                print(iii,iiii, len(reading))
            
            if iiii != -1:
                AccString = AccString + reading[0:iiii+2]
                # print("Fuck")
            else:
                AccString = AccString + reading
                # print("Yeag")
        
    except:
        pass