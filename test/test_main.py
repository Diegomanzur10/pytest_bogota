from code.main import suma, resta, multiplicacion, division
import pytest

@pytest.mark.parametrize(
        (
            "a",
            "b",
            "valor_esperado"
        ),
        [
            (
                3,
                4,
                7
            ),
            (
                4,
                4,
                8
            )
        ],
        ids=[
            "test1",
            "test2"
        ]
)
def test_suma(a, b, valor_esperado):
    assert suma(a, b) == valor_esperado

@pytest.mark.xfail(reason = "funcion a depricar")
def test_division():
    assert division(4,0) == 1
