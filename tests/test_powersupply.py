import pytest


TEST_VOLTAGE = 1.00
TEST_CURRENT = 1.000


def check_bit(bits, n):
    return bits & (1 << n)


def check_output_bit(bits):
    return check_bit(bits, 6) != 0


class Test_PowerSupply(object):
    def test_check_initial_set_voltage_is_zero(self, ps):
        assert ps.get_set_voltage() == 0


    def test_check_initial_set_current_is_zero(self, ps):
        assert ps.get_set_current() == 0


    def test_check_power_supply_is_off(self, ps):
        status_bits = ord(ps.get_status())
        assert check_output_bit(status_bits) == False


    def test_set_voltage(self, ps):
        ps.set_voltage(TEST_VOLTAGE)
        assert ps.get_set_voltage() == TEST_VOLTAGE


    def test_set_current(self, ps):
        ps.set_current(TEST_CURRENT)
        assert ps.get_set_current() == TEST_CURRENT


    def test_turn_on(self, ps):
        ps.on()
        assert check_output_bit(ord(ps.get_status())) == True


    def test_get_voltage(self, ps):
        assert ps.get_voltage() == TEST_VOLTAGE
    

    def test_get_current(self, ps):
        assert ps.get_current() == 0


    def test_turn_off(self, ps):
        ps.off()
        assert check_output_bit(ord(ps.get_status())) == False


    def test_store_panel_setting(self, ps):
        assert ps.store_panel_setting(1) == (TEST_VOLTAGE, TEST_CURRENT)


    def test_recall_panel_setting(self, ps):
        assert ps.recall_panel_setting(1) == (TEST_VOLTAGE, TEST_CURRENT)
