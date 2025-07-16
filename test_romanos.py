from funciones_romanos import de_arabigo_a_romano, descomponer, de_romano_a_arabigo, get_order
import pytest


@pytest.mark.parametrize(
    "arabic, expected_roman",
    [
        (1976, "MCMLXXVI"),
        (2984, "MMCMLXXXIV"),
        (1000, "M"),
        (900, "CM"),
        (70, "LXX"),
        (6, "VI")

    ]
)
def test_arabic_to_roman(arabic, expected_roman):
    assert de_arabigo_a_romano(arabic) == expected_roman
"""
def test_1976():
    assert de_arabigo_a_romano(1976) == "MCMLXXVI"
    assert de_arabigo_a_romano(2984) == "MMCMLXXXIV"

def test_miles():
    assert de_arabigo_a_romano(1000) == "M"

def test_centenas():
    assert de_arabigo_a_romano(900) == "CM"

def test_decenas():
    assert de_arabigo_a_romano(70) == "LXX"


def test_unidades():
    assert de_arabigo_a_romano(6) == "VI"
"""
def test_descomponer_numeros():
    assert descomponer(1976) == [1000, 900, 70, 6]
    assert descomponer(2984) == [2000, 900, 80, 4]


"""
Tests para romano a arabigo

Existen tres reglas basicas
- regla de traducir cada simbolo a su valor
- regla del orden: Los símbolos se suman y ordenan de mayor a menor
- regla de las repeticiones: los simbolos I, X, C, M pueden repetirse un maximo de 3 veces
- reglas de las restas: 
  - los simbolos I, X, C, M pueden restar si van delante de uno mayor
    los pares:
     - V, X para I
     - L, C para X
     - D, M para C
  - Solo puede haber una resta por grupo, (no se puede escribir IVIV)

"""

def test_orden_decreciente_romanos_70():
    assert de_romano_a_arabigo("LXX") == 70
    assert de_romano_a_arabigo("MDCLXVI") == 1666

    # Nos falta el test de raise ValueError cuando esten desordenados
    # Nos falta el test de raise ValueError si hay un simbolo incorrecto, como W

def test_orden_creciente_error():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("VC")



def test_restas_permitidas():
    assert de_romano_a_arabigo("IV") == 4
    assert de_romano_a_arabigo("XL") == 40
    assert de_romano_a_arabigo("MCDXLIX") == 1449

def test_simbolos_no_permitidos():
    with pytest.raises(ValueError) as la_variable_que_quiera_Eze:
        de_romano_a_arabigo("XW")

    assert "Simbolo no permitido" in str(la_variable_que_quiera_Eze.value)

# Comprobar que solo se pueden repetir los simbolos I, X, C, M hasta un maximo de 3 veces

def test_repeticiones_max_3():
    with pytest.raises(ValueError) as excinfo:
        de_romano_a_arabigo("MMMMCCCCXXXXIIII")

    with pytest.raises(ValueError) as excinfo:
        de_romano_a_arabigo("IIII")

    with pytest.raises(ValueError) as excinfo:
        de_romano_a_arabigo("MMMM")

    with pytest.raises(ValueError) as excinfo:
        de_romano_a_arabigo("CCCC")

    with pytest.raises(ValueError) as excinfo:
        de_romano_a_arabigo("XXXX")


def test_max_3_diferentes():
    assert de_romano_a_arabigo("MMMIII") == 3003

def test_VLD_no_repeticiones():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("DD")

    with pytest.raises(ValueError):
        de_romano_a_arabigo("MMMLL")

    with pytest.raises(ValueError):
        de_romano_a_arabigo("IVV")



# test de restas repetidas o encadenadas
def test_repetidas():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IVIX")

def test_restas_desordenadas():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IXCM")

def test_restas_encadenadas_deben_fallar():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IXC")

def test_no_se_resta_si_ya_hay_valor_del_mismo_1orden():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("CCM")

def test_no_se_resta_si_ya_hay_del_msimo_orden_sin_repe():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("LXC")


# Tests para saber orden de numero
@pytest.mark.parametrize(
    "numero, orden",
    [
        (1, 1),
        (10, 10),
        (110, 10),
        (112, 1),
        (2000, 1000),
        (2300, 100)
    ]
)
def test_orden(numero, orden):
    assert get_order(numero) == orden