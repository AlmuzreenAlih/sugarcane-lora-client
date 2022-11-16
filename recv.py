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
AccString = ["s"]

iii = 0

while True:
    reading = SerialData.readline().decode("utf-8")
    reading = reading.replace('\r\n',"")
    
    try:            
        if Start == 0 and reading[0] == '=':
            print("start")
            Start = 1
            SerialData.write(bytes("AA", "utf-8"))
        elif Start == 1 and reading[0] == '=':
            # print("end", len(AccString))
            # f = open("some.txt", "w+")
            # f.write(AccString) 
            # f.close()
            AccStr = ""
            for i in AccString:
                if i != "s":
                    AccStr = AccStr + i
            
            FinalString = base64.b64decode(AccStr)
            f = open("Vvv.jpg", "wb+")
            f.write(FinalString) 
            f.close()
            Start = 0
            SerialData.write(bytes("AA", "utf-8"))
        elif reading != '\r' and reading != '\n' and reading != '' and reading != '\r\n' and reading != 'Success':               
            print(reading, reading[0], reading[-1])
            iii = iii+1
            FooterFoundAt = reading.find('==')
            if len(reading)!=250:
                print(iii,FooterFoundAt, len(reading))
            
            if (reading[0] == reading[-1]):
                print("Equal")
                if FooterFoundAt != -1:
                    print("Found")
                    if reading[0] == AccString[-1][0]:
                        print(iii,reading,"Renaming last")
                        AccString[-1] = reading[0:FooterFoundAt+2]
                    else:
                        AccString.append(reading[0:FooterFoundAt+2])
                    SerialData.write(bytes(reading[0:FooterFoundAt+2], "utf-8"))
                else:
                    print("Not Found", AccString[-1][0])
                    if reading[0] == AccString[-1][0]:
                        print(iii,reading,"Renaming last")
                        AccString[-1] = reading
                    else:
                        print(iii,reading,"Good")
                        AccString.append(reading)
                    print("Haha")    
                    SerialData.write(bytes(reading, "utf-8"))
            else:
                SerialData.write(bytes("h", "utf-8"))
                
        
    except:
        pass