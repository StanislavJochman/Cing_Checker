import time
import webbrowser
import serial


ports = ['/dev/ttyUSB','COM']
error = 0
config = open("Cing_Checker.config","r")
config.readline()
port = config.readline().split("=")
port = port[1]
port = port.strip()

def BoardNotFound():
	print("Board is not available. Make sure your board is on (the green LED is on) and connected to the computer.")
	exit()

if(port == "AUTO"):
	for x in range(len(ports)):
		for y in range(255):
			try:
				ser = serial.Serial(ports[x]+str(y), 9600)
				print("Opening port: {}. Please wait.".format())
				break
			except:
				error += 1
			if(error > len(ports)*256):
				BoardNotFound()
else:
	ser = serial.Serial(port, 9600)


def ReadSerial():
	try:
		serial = str(ser.readline())
		serial_string = ""
		for x in range(2,len(serial)-5):
			serial_string += serial[x]
		return serial_string
	except:
		BoardNotFound()


def update_values():
    values = []
    value = ReadSerial()    
    if(value == "------"):
        for x in range(20):
            value = ReadSerial()
            if(value !="-127.00"):
                values.append(value)
            else:
                values.append("Fail")
        print(values)
        return(values)
    else:
        return []

def update(self):
    starttime = time.time()
    values = update_values()
    print(values)
    if(len(values)==20):
        self.value1.setText(values[0])
        self.value2.setText(values[1])
        self.value3.setText(values[2])
        self.value4.setText(values[3])
        self.value5.setText(values[4])
        self.value6.setText(values[5])
        self.value7.setText(values[6])
        self.value8.setText(values[7])
        self.value9.setText(values[8])
        self.value10.setText(values[9])
        self.value11.setText(values[10])
        self.value12.setText(values[11])
        self.value13.setText(values[12])
        self.value14.setText(values[13])
        self.value15.setText(values[14])
        self.value16.setText(values[15])
        self.value17.setText(values[16])
        self.value18.setText(values[17])
        self.value19.setText(values[18])
        self.value20.setText(values[19])
    #print("FPS: {}".format(round(1/(time.time()-starttime),1)))
    

def about_open():
    webbrowser.open('https://robotcing.sk/about_us.html')
def site_open():
    webbrowser.open('https://robotcing.sk/')
def troubleshooting_open():
    webbrowser.open('https://robotcing.sk/about_us.html')
def config_open():
    webbrowser.open('Cing_Checker.config')
    

"""
#custom imports
################################
import ReadCingSensors
################################

        #Custom code
        ################################
        #self.actionAbout.triggered.connect(lambda: self.clicked("COM2"))
        self.actionAbout.triggered.connect(lambda: ReadCingSensors.about_open())
        self.actionWebsite.triggered.connect(lambda: ReadCingSensors.site_open())
        self.actionTroubleshooting.triggered.connect(lambda: ReadCingSensors.troubleshooting_open())
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionConnect.triggered.connect(lambda: ReadCingSensors.connect())
        QtCore.QTimer.singleShot(90, self.updateData)
        ################################
    #Custom code
    ################################
    def updateData(self):
        ReadCingSensors.update(self)
        QtCore.QTimer.singleShot(90, self.updateData)
    ################################
"""