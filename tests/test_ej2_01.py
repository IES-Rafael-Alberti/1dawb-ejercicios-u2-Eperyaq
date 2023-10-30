import pytest
from src. import pruebaNivel, comprobarNivel

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, False),
        (18, True),
        (100, True),
        (5, False),
        (17, False),
        (125, True)
    ]
)
def test_mayorEdad_params(input_n, expected):
    assert mayorEdad(input_n) == expected


