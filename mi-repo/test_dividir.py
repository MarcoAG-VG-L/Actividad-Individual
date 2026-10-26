import pytest

from dividir import dividir


def test_dividir_dos_numeros():
    assert dividir(10, 2) == 5


def test_dividir_positivo_y_negativo():
    assert dividir(-10, 2) == -5


def test_dividir_devuelve_resultado_decimal():
    assert dividir(5, 2) == 2.5


def test_dividir_cero():
    assert dividir(0, 5) == 0


def test_dividir_entre_cero_lanza_error():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
