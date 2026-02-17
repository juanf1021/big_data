def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- LAS PRUEBAS ---
def test_primo_con_7():
    assert es_primo(7) == True

def test_primo_con_10():
    assert es_primo(10) == False

def test_primo_con_1():
    assert es_primo(1) == False