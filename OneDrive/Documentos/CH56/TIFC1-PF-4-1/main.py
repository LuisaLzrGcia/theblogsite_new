import json
import requests

# PASO 1: La función mágica que el sistema necesita
def trivia_fetch(num):
    """
    Esta función es OBLIGATORIA - el sistema la va a probar
    Recibe un número y devuelve datos curiosos sobre él
    """
    # Empezamos con datos básicos que siempre funcionan
    datos_curiosos = {
        "numero": num,
        "es_par": num % 2 == 0,
        "cuadrado": num * num,
        "doble": num * 2,
        "mitad": num / 2,
        "digitos": len(str(abs(num))),
        "es_positivo": num > 0,
        "es_primo": es_primo(num)
    }
    
    # Intentamos obtener datos curiosos de internet usando JSON
    try:
        # Obtenemos datos curiosos generales en formato JSON
        url_trivia = f"http://numbersapi.com/{num}?json"
        response = requests.get(url_trivia, timeout=5)
        
        if response.status_code == 200:
            trivia_web = json.loads(response.content)
            # Agregamos los datos de la web a nuestro diccionario
            datos_curiosos["texto_curioso"] = trivia_web.get("text", "Sin dato disponible")
            datos_curiosos["tipo_trivia"] = trivia_web.get("type", "general")
            datos_curiosos["encontrado"] = trivia_web.get("found", False)
        
        # También intentamos obtener datos matemáticos
        url_math = f"http://numbersapi.com/{num}/math?json"
        response_math = requests.get(url_math, timeout=5)
        
        if response_math.status_code == 200:
            math_web = json.loads(response_math.content)
            datos_curiosos["dato_matematico"] = math_web.get("text", "Sin dato matemático")
            
    except Exception as e:
        # Si no hay internet o falla, ponemos datos locales
        datos_curiosos["texto_curioso"] = f"¡El número {num} es especial porque tiene exactamente {len(str(abs(num)))} dígitos!"
        datos_curiosos["tipo_trivia"] = "local"
        datos_curiosos["encontrado"] = True
        datos_curiosos["dato_matematico"] = f"Matemáticamente, {num} elevado al cuadrado es {num * num}"
    
    return datos_curiosos

def es_primo(n):
    """
    Función auxiliar para verificar si un número es primo
    """
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

# PASO 2: Funciones para tu quiz (opcionales pero útiles)
def hacer_pregunta(pregunta, respuesta_correcta):
    """
    Función para hacer una pregunta y verificar la respuesta
    """
    print(f"\n🤔 {pregunta}")
    respuesta_usuario = input("Tu respuesta: ").strip()
    
    if respuesta_usuario.lower() == respuesta_correcta.lower():
        print("🎉 ¡CORRECTO!")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta era: {respuesta_correcta}")
        return False

def mostrar_trivia_numero(numero):
    """
    Función para mostrar datos curiosos de un número de forma bonita
    """
    print(f"\n🔢 ¡DATOS SÚPER CURIOSOS SOBRE EL {numero}!")
    print("=" * 50)
    
    trivia = trivia_fetch(numero)  # Usamos nuestra función mágica mejorada
    
    # Mostramos datos básicos
    print(f"📊 DATOS BÁSICOS:")
    print(f"   • Es {'par' if trivia['es_par'] else 'impar'}")
    print(f"   • Tiene {trivia['digitos']} dígito(s)")
    print(f"   • Es {'positivo' if trivia['es_positivo'] else 'negativo o cero'}")
    print(f"   • Es {'un número primo' if trivia['es_primo'] else 'NO es primo'}")
    print(f"   • Su cuadrado es: {trivia['cuadrado']}")
    
    # Mostramos datos curiosos de internet
    print(f"\n🌐 DATO CURIOSO DE INTERNET:")
    print(f"   • {trivia['texto_curioso']}")
    
    if 'dato_matematico' in trivia:
        print(f"\n🧮 DATO MATEMÁTICO ESPECIAL:")
        print(f"   • {trivia['dato_matematico']}")
    
    print("=" * 50)

# PASO 3: La función principal donde va todo tu quiz
def main():
    """
    Aquí va toda la diversión de tu quiz
    """
    print("🎮 ¡BIENVENIDO AL QUIZ SÚPER DIVERTIDO!")
    print("=" * 40)
    
    # Pedimos el nombre del jugador
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola {nombre}! Vamos a jugar 🎉")
    
    puntos = 0
    
    # PREGUNTA 1: Sobre números
    print("\n--- RONDA 1: MATEMÁTICAS ---")
    if hacer_pregunta("¿Cuánto es 5 + 3?", "8"):
        puntos += 1
    
    # PREGUNTA 2: Trivia general
    print("\n--- RONDA 2: CULTURA GENERAL ---")
    if hacer_pregunta("¿Cuál es la capital de México?", "Ciudad de México"):
        puntos += 1
    
    # PREGUNTA 3: Pedimos un número y mostramos trivia
    print("\n--- RONDA 3: TU NÚMERO FAVORITO ---")
    try:
        numero_favorito = int(input("Dime tu número favorito: "))
        mostrar_trivia_numero(numero_favorito)
        
        # Pregunta basada en su número
        trivia_num = trivia_fetch(numero_favorito)
        if trivia_num["es_par"]:
            respuesta = "par"
        else:
            respuesta = "impar"
        
        if hacer_pregunta(f"¿El número {numero_favorito} es par o impar?", respuesta):
            puntos += 1
            
    except ValueError:
        print("¡Ey! Eso no era un número válido, pero sigamos...")
    
    # RESULTADOS FINALES
    print("\n" + "="*40)
    print(f"🏆 ¡QUIZ TERMINADO, {nombre}!")
    print(f"🌟 Tu puntuación: {puntos}/3")
    
    if puntos == 3:
        print("🎉 ¡PERFECTO! Eres un genio!")
    elif puntos == 2:
        print("😊 ¡Muy bien! Casi perfecto!")
    elif puntos == 1:
        print("👍 ¡No está mal! Puedes mejorar!")
    else:
        print("💪 ¡Inténtalo de nuevo! La práctica hace al maestro!")

# PASO 4: El código mágico que hace que todo funcione
if __name__ == "__main__":
    main()