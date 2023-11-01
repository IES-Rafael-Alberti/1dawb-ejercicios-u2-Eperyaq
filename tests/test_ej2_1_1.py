import pytest
from src.ejercicio2_1_01 import edad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("20", True),
        ("8", False),
        ("14", False),
        ("40", True)
       
    ]
)
def test_edad_params(input_n1, expected):
    assert edad(input_n1) == expected