from fastapi import FastAPI

app = FastAPI()


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    # Verificamos si es divisible por algún número hasta su raíz cuadrada
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.get("/")
def home():
    return {"mensaje": "Hola! Usa /primo/TU_NUMERO para probar"}

@app.get("/primo/{numero}")
def verificar_primo(numero: int):
    # Llamamos a la función que creamos arriba
    resultado = es_primo(numero)
    
    # Devolvemos un JSON con la respuesta
    return {
        "numero": numero,
        "es_primo": resultado
    }