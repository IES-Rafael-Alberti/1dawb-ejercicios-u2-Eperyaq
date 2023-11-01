import pytest
from src.ejercicios2_1_8 import pruebaNivel

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("0.0", "Inaceptable"),
        ("0.4", "Aceptable"),
        ("0.6", "Meritorio")
       
    ]
)
def test_pruebaNivel_params(input_n1, expected):
    assert pruebaNivel(input_n1) == expected