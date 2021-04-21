import pytest
from tenma.powersupply import PowerSupply


def pytest_addoption(parser):
    parser.addoption('--port', help='serial port of the power supply')


@pytest.fixture(scope="session")
def ps(request):
    try:
        port = request.config.getoption('--port')
        PS = PowerSupply(port)
        yield PS
        PS.close()
    except Exception as ex:
        raise pytest.exit(ex)
