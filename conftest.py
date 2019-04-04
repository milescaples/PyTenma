import pytest
from tenma.powersupply import PowerSupply

@pytest.fixture(scope="module")
def ps():
    PS = PowerSupply("COM3")
    response = PS.getIdentification()
    if not response.startswith("TENMA"):
        raise pytest.exit('Incorrect device setup')
    yield PS
    PS.close()