import time
import serial


class PowerSupply():
    def __init__(self, comport):
        self.ser = serial.Serial(comport, 9600)
        assert self.get_identification() is not None
        self.set_output(0.0, 0.0)
        self.off()


    def close(self):
        self.ser.close()


    def execute(self, command):
        self.ser.write(command.encode('utf-8'))
        time.sleep(0.1)
        if command.endswith('?'):
            response = self.ser.read(self.ser.inWaiting())
            return response


    def get_identification(self):
        return self.execute('*IDN?').decode('utf-8')


    def get_status(self):
        return self.execute('STATUS?')


    def set_voltage(self, voltage):
        self.execute('VSET1:{:.2f}'.format(voltage))


    def get_set_voltage(self):
        return float(self.execute('VSET1?').decode('utf-8'))


    def get_voltage(self):
        return float(self.execute('VOUT1?').decode('utf-8'))


    def set_current(self, current):
        self.execute('ISET1:{:.3f}'.format(current))


    def get_set_current(self):
        return float(self.execute('ISET1?').decode('utf-8').strip('K'))


    def get_current(self):
        return float(self.execute('IOUT1?').decode('utf-8'))


    def set_output(self, voltage, current):
        self.set_voltage(voltage)
        self.set_current(current)


    def on(self):
        self.execute('OUT1')


    def off(self):
        self.execute('OUT0')

    
    def set_overcurrent_protection(self, boolean):
        self.execute('OCP' + ('1' if boolean else '0'))


    def set_overvoltage_protection(self, boolean):
        self.execute('OVP' + ('1' if boolean else '0'))


    def store_panel_setting(self, integer):
        if integer in range(1,5):
            self.execute('SAV{:d}'.format(integer))
            return self.get_set_voltage(), self.get_set_current()
        else:
            raise Exception("integer out of bounds")


    def recall_panel_setting(self, integer):
        if integer in range(1,5):
            self.execute('RCL{:d}'.format(integer))
            return self.get_set_voltage(), self.get_set_current()
        else:
            raise Exception("integer out of bounds")
        