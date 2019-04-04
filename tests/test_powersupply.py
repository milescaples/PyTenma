import pytest


class Test_PowerSupply(object):
    def test_initial_set_voltage(self, ps):
        voltage = ps.checkSetVoltage()
        assert voltage == 0

    def test_initial_set_current(self, ps):
        current = ps.checkSetCurrent()
        assert current == 0
