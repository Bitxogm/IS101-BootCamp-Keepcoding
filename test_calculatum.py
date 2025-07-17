from calculatum.presentacion import input_romano, input_operaciones, continuar_o_salir
from calculatum.datos import OPERATION, rn
from calculatum.logica import calcular
import pytest

@pytest.mark.parametrize(
    "lista_entradas, result",
    [
        (["I"], rn(1)),
        (["doce", "-1", "XII"], rn(12)),
        (["12"], rn(12)),
    ]
)
def test_input_romanos(monkeypatch, lista_entradas, result):
    entradas = iter(lista_entradas)
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    assert input_romano("") == result


@pytest.mark.parametrize(
    "lista_entradas, result",
    [
        (["+"], OPERATION.ADD),
        (["-"], OPERATION.SUB),
        (["x"], OPERATION.MUL),
        (["/"], OPERATION.DIV),
        (["*", "x"], OPERATION.MUL)

    ]
)
def test_input_operaciones(monkeypatch, lista_entradas, result):
    entradas = iter(lista_entradas)
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    assert input_operaciones("") == result

@pytest.mark.parametrize(
    "num1, num2, resultado, operacion",
    [
        (rn(1), rn(32), rn(33), OPERATION.ADD),
        (rn(41), rn(32), rn(9), OPERATION.SUB),
        (rn(1), rn(32), rn(32), OPERATION.MUL),
        (rn(32), rn(32), rn(1), OPERATION.DIV),
    ]
)
def test_calculos(num1, num2, resultado, operacion):
    assert calcular(num1, num2, operacion) == resultado


@pytest.mark.parametrize(
    "respuesta, result",
    [
        ("S", True),
        ("s", True),
        ("N", False),
        ("n", False),
        ("12", False)
    ]
)
def test_continue(monkeypatch, respuesta, result):
    monkeypatch.setattr("builtins.input", lambda _: respuesta)
    assert continuar_o_salir("") == result