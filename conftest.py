import pytest
from tenma.powersupply import PowerSupply


@pytest.fixture(scope="module")
def ps():
    try:
        PS = PowerSupply("COM3")
        yield PS
        PS.close()
    except Exception as ex:
        raise pytest.exit(ex)
