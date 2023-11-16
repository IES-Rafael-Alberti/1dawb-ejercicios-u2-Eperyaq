import pytest
from src.ejercicios2_1_9 import precios

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (2, "Puedes entrar gratis!"),
        (6, "Debes pagar 5€"),
        (42, "Tienes que pagar 10€")
       
    ]
)
def test_precios_params(input_n1, expected):
    assert precios(input_n1) == expected