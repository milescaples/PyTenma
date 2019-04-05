import time
import serial
from decimal import Decimal


class PowerSupply():
    def __init__(self, comport):
        self.ser = serial.Serial(comport, 9600)

        if not self.getIdentification().startswith("TENMA"):
            self.ser.close()
            raise Exception("Device on " + comport + " not compatible")

        self.setVoltage(0)
        self.set_voltage = self.checkSetVoltage()
        self.setCurrent(0)
        self.set_current = self.checkSetCurrent()
        self.setOutput(False)

    def close(self):
        self.ser.close()

    def com(self, command):
        self.ser.write(command.encode('utf-8'))
        time.sleep(0.1)
        if command.endswith('?'):
            reply = self.ser.read(self.ser.inWaiting())
            return reply

    def getIdentification(self):
        return self.com('*IDN?').decode('utf-8')

    def status(self):
        return self.com('STATUS?')

    def setVoltage(self, voltage):
        return self.com('VSET1:{:.2f}'.format(voltage))

    def checkSetVoltage(self):
        return Decimal(self.com('VSET1?').decode('utf-8'))

    def getVoltage(self):
        return Decimal(self.com('VOUT1?').decode('utf-8'))

    def setCurrent(self, current):
        return self.com('ISET1:{:.3f}'.format(current))

    def checkSetCurrent(self):
        return Decimal(self.com('ISET1?').decode('utf-8'))

    def getCurrent(self):
        return Decimal(self.com('IOUT1?').decode('utf-8'))

    def setOutput(self, boolean):
        return self.com('OUT' + ('1' if boolean else '0'))

    def setOvercurrentProtection(self, boolean):
        return self.com('OCP' + ('1' if boolean else '0'))

    def setOvervoltageProtection(self, boolean):
        return self.com('OVP' + ('1' if boolean else '0'))

    def recallPanelSetting(self, integer):
        return self.com('RCL{:d}'.format(integer))

    def storePanelSetting(self, integer):
        return self.com('SAV{:d}'.format(integer))
