import base64
import time
import threading
import eel

class MyTimer:
    def __init__(self):
        self.StartTime = 0
        self.TargetTime = 0
        self.Force = 0
    
    def start(self, TargetTime):
        self.Force = 0
        self.StartTime = time.time()
        self.TargetTime = TargetTime
        
    def justFinished(self):
        # print(self.Force,time.time()-self.StartTime, self.TargetTime)
        if self.Force == 1:
            return False
        if (time.time()-self.StartTime > self.TargetTime):
            self.Force = 1
            return True
        else:
            return False
    def elapsed(self):
        return time.time()-self.StartTime
    
    def stop(self):
        self.Force = 1

Timer1 = MyTimer()
Timer1.justFinished()

eel.init('GUI')
import warnings
import serial
import serial.tools.list_ports

SerialData = serial.Serial("com7", 115200, timeout = 0.2)

SerialData.setDTR(False)
time.sleep(1)
SerialData.flushInput()
SerialData.setDTR(True)
time.sleep(2)
# SerialData.write(bytes("2", "utf-8"))
# reading = SerialData.readline().decode("utf-8")
# reading = SerialData.readline().decode("utf-8")
#	 if reading == 'A':
#		 pass

Start = 0
AccString = ["s"]

iii = 0
PacketsSuccess = 0
from os import listdir
from os.path import isfile, join
FName = "Default"
PacketsTotal = 1
def ShowPackets():
    global PacketsSuccess,Classification,Percentage,FName
    eel.JS_Show_Progress("STATUS: Packet " + str(PacketsSuccess) + " out of " + str(PacketsTotal) +" packets" +" received! (" + str(round((PacketsSuccess/(PacketsTotal))*100,2)) + "%)")
    # eel.JS_Show_Class(FName.split("_")[1],FName.split("_")[2])
def MainLoop():
    global Start,AccString,iii, PacketsSuccess, FName,PacketsTotal
    reading = SerialData.readline().decode("utf-8")
    reading = reading.replace('\r\n',"")
    if Timer1.justFinished():
        Start = 0
        eel.JS_Show_Timeout()
        eel.JS_Show_Progress("STATUS: READY TO RECEIVE A FILE")    
        
    try:           
        print(str(time.time())) 
        if reading != "":
            print(reading)

        if reading[0] == '=':
            Start = 1
            EndFoundAt = reading.find('$$')
            EndFoundAt2 = reading.find('^^')
            SerialData.write(bytes(reading[0:EndFoundAt2+3], "utf-8"))
            FName = reading[1:EndFoundAt]
            print("start: ", FName, reading[EndFoundAt+2:EndFoundAt2])
            PacketsTotal = int(reading[EndFoundAt+2:EndFoundAt2])
            PacketsSuccess = 0
            Timer1.start(30)
            AccString = ["s"]
        elif reading[0] == '#':
            EndFoundAt = reading.find('$$')
            EndFoundAt2 = reading.find('^^')
            FName = reading[1:EndFoundAt]
            print("start: ", FName, reading[EndFoundAt+2:EndFoundAt2])
            f = open("GUI/images/"+FName, "wb+")
            f.write(b' ') 
            f.close()
            mypath = "GUI/images"
            onlyfiles = ["images/"+f for f in listdir(mypath) if isfile(join(mypath, f))]
            eel.JS_Delete_Elements()
            eel.JS_Send_Paths(onlyfiles)
            eel.JS_Show_Success(1)
            eel.JS_Show_Progress("STATUS: READY TO RECEIVE A FILE")  
            print("done")
            
            
        elif Start == 1 and reading[0] == '+':
            print("end", len(AccString))
            SerialData.write(bytes("AA", "utf-8"))
            
            if len(AccString) > 50:
                AccStr = ""
                for i in AccString:
                    if i != "s":
                        AccStr = AccStr + i[1:-1]
                print("encoding",AccStr[0],AccStr[1],AccStr[-1],AccStr[-2],AccStr[-3],len(AccStr),type(AccStr))
                FinalString = base64.b64decode(AccStr[0:-2])

                f = open("GUI/images/"+FName, "wb+")
                f.write(FinalString) 
                f.close()
            else:
                f = open("GUI/images/"+FName, "wb+")
                f.write(b' ') 
                f.close()
            print("saved")
            Start = 0
            mypath = "GUI/images"
            onlyfiles = ["images/"+f for f in listdir(mypath) if isfile(join(mypath, f))]
            eel.JS_Delete_Elements()
            eel.JS_Send_Paths(onlyfiles)
            eel.JS_Show_Success(2)
            eel.JS_Show_Progress("STATUS: READY TO RECEIVE A FILE")  
            Timer1.stop()
            AccString = ["s"]
              
        elif Start == 1 and reading != '\r' and reading != '\n' and reading != '' and reading != '\r\n' and reading != 'Success':               
            # print(reading, reading[0], reading[-1])
            Timer1.start(30)
            iii = iii+1
            FooterFoundAt = reading.find('##')
            if len(reading)!=250:
                pass
                # print(iii,FooterFoundAt, len(reading))
            
            if (reading[0] == reading[-1]) or (reading[0] == reading[FooterFoundAt+2]):
                # print("Equal")
                if FooterFoundAt != -1:
                    print("Found")
                    if reading[0] == AccString[-1][0]:
                        # print(iii,reading,"Renaming last")
                        AccString[-1] = reading[0:FooterFoundAt+2]
                    else:
                        AccString.append(reading[0:FooterFoundAt+3])
                        PacketsSuccess = PacketsSuccess + 1
                        ShowPackets()
                    print(repr(reading[0:FooterFoundAt+3]))
                    SerialData.write(bytes(reading[0:FooterFoundAt+3], "utf-8"))
                else:
                    # print("Not Found", AccString[-1][0])
                    if reading[0] == AccString[-1][0]:
                        # print(iii,reading,"Renaming last")
                        AccString[-1] = reading
                    else:
                        # print(iii,reading,"Good")
                        AccString.append(reading)
                        PacketsSuccess = PacketsSuccess + 1
                        ShowPackets()
                    SerialData.write(bytes(reading, "utf-8"))
            else:
                SerialData.write(bytes("h", "utf-8"))    
    except:
        pass
    
    t1 = threading.Timer(0.1,MainLoop,[]).start()

mypath = "GUI/images"
onlyfiles = ["images/"+f for f in listdir(mypath) if isfile(join(mypath, f))]
eel.JS_Delete_Elements()
eel.JS_Send_Paths(onlyfiles)
eel.JS_Show_Progress("STATUS: READY TO RECEIVE A FILE")     
MainLoop()
eel.start('index.html', mode='chrome', cmdline_args=['--start-maximized'])
