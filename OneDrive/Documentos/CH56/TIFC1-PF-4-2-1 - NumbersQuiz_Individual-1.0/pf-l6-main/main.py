import json
import requests


def trivia_fetch(num):
  
    
    
    
    datos_curiosos = {
        "number": num,
        "es_par": num % 2 == 0,
        "cuadrado": num * num,
        "doble": num * 2,
        "mitad": num / 2,
        "digitos": len(str(abs(num))),
        "es_positivo": num > 0,
        "es_primo": es_primo(num)
    }
    
   
    try:
        
        url_trivia = f"http://numbersapi.com/{num}?json"
        response = requests.get(url_trivia, timeout=5)
        
        if response.status_code == 200:
            trivia_web = json.loads(response.content)
            
            datos_curiosos["texto_curioso"] = trivia_web.get("text", "Sin dato disponible")
            datos_curiosos["tipo_trivia"] = trivia_web.get("type", "general")
            datos_curiosos["encontrado"] = trivia_web.get("found", False)
        
        
        url_math = f"http://numbersapi.com/{num}/math?json"
        response_math = requests.get(url_math, timeout=5)
        
        if response_math.status_code == 200:
            math_web = json.loads(response_math.content)
            datos_curiosos["dato_matematico"] = math_web.get("text", "Sin dato matemático")
            
    except Exception as e:
        
        datos_curiosos["texto_curioso"] = f"¡El número {num} es especial porque tiene exactamente {len(str(abs(num)))} dígitos!"
        datos_curiosos["tipo_trivia"] = "local"
        datos_curiosos["encontrado"] = True
        datos_curiosos["dato_matematico"] = f"Matemáticamente, {num} elevado al cuadrado es {num * num}"
    
    return datos_curiosos

def es_primo(n):
    
    
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def hacer_pregunta(pregunta, respuesta_correcta):
    
    print(f"\n{pregunta}")
    respuesta_usuario = input("Tu respuesta: ").strip()
    
    if respuesta_usuario.lower() == respuesta_correcta.lower():
        print("¡CORRECTO!")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta era: {respuesta_correcta}")
        return False

def mostrar_trivia_numero(numero):
    
    print(f"\n¡DATOS SÚPER CURIOSOS SOBRE EL {numero}!")
    print("=" * 50)
    
    trivia = trivia_fetch(numero)  
    
    
    print(f" DATOS BÁSICOS:")
    print(f"   • Es {'par' if trivia['es_par'] else 'impar'}")
    print(f"   • Tiene {trivia['digitos']} dígito(s)")
    print(f"   • Es {'positivo' if trivia['es_positivo'] else 'negativo o cero'}")
    print(f"   • Es {'un número primo' if trivia['es_primo'] else 'NO es primo'}")
    print(f"   • Su cuadrado es: {trivia['cuadrado']}")
    
    
    print(f"\n DATO CURIOSO DE INTERNET:")
    print(f"   • {trivia['texto_curioso']}")
    
    if 'dato_matematico' in trivia:
        print(f"\n DATO MATEMÁTICO ESPECIAL:")
        print(f"   • {trivia['dato_matematico']}")
    
    print("=" * 50)


def main():
    """
    Aquí va toda la diversión de tu quiz
    """
    print(" ¡BIENVENIDO AL QUIZ SÚPER DIVERTIDO!")
    print("=" * 40)
    
    
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola {nombre}! Vamos a jugar ")
    
    puntos = 0
    
    
    print("\n--- RONDA 1: MATEMÁTICAS ---")
    if hacer_pregunta("¿Cuánto es 127 + 314?", "441"):
        puntos += 1
    
    
    print("\n--- RONDA 2: CULTURA GENERAL ---")
    if hacer_pregunta("¿Cuál es la capital de Brasil?", "Brasília"):
        puntos += 1
    
    
    print("\n--- RONDA 3: TU NÚMERO FAVORITO ---")
    try:
        numero_favorito = int(input("Dime tu número favorito: "))
        mostrar_trivia_numero(numero_favorito)
        
        
        trivia_num = trivia_fetch(numero_favorito)
        if trivia_num["es_par"]:
            respuesta = "par"
        else:
            respuesta = "impar"
        
        if hacer_pregunta(f"¿El número {numero_favorito} es par o impar?", respuesta):
            puntos += 1
            
    except ValueError:
        print(" Eso no era un número válido")
    
    
    print("\n" + "="*40)
    print(f"¡QUIZ TERMINADO, {nombre}!")
    print(f" Tu puntuación: {puntos}/3")
    
    if puntos == 3:
        print(" ¡PERFECTO! Eres un genio!")
    elif puntos == 2:
        print(" ¡Muy bien! Casi perfecto!")
    elif puntos == 1:
        print("¡No está mal! Puedes mejorar!")
    else:
        print("¡Inténtalo de nuevo! La práctica hace al maestro!")


if __name__ == "__main__":
    main()