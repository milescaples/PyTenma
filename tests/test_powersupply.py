import pytest


def check_bit(bits, n):
    return bits & (1 << n)

def check_output_bit(bits):
    return check_bit(bits, 6) != 0

class Test_PowerSupply(object):
    def test_check_power_supply_is_off(self, ps):
        status_bits = ord(ps.status())
        assert check_output_bit(status_bits) == False

    def test_check_initial_set_voltage_is_zero(self, ps):
        voltage = ps.checkSetVoltage()
        assert voltage == 0

    def test_check_initial_set_current_is_zero(self, ps):
        current = ps.checkSetCurrent()
        assert current == 0

    def test_set_and_check_voltage(self, ps):
        ps.setVoltage(1.00)
        voltage = ps.checkSetVoltage()
        assert voltage == 1.00
    
    def test_set_and_check_current(self, ps):
        ps.setCurrent(1.000)
        current = ps.checkSetCurrent()
        assert current == 1.000
    
    def test_turn_on(self, ps):
        ps.setOutput(True)
        assert check_output_bit(ord(ps.status())) == True
    
    def test_turn_off(self, ps):
        ps.setOutput(False)
        assert check_output_bit(ord(ps.status())) == False