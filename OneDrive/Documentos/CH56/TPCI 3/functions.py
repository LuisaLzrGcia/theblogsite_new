# Say hello!
def print_hello_world():
    print("Hello world - from a function!")

print_hello_world() # Llamada de la function

# Function to return the phrase "Hello <name>"
def hello_name(name):
    response = "Hello " + name
    return response

print(hello_name("Gisella"))
print(hello_name("Jaqui"))

# Function to add two numbers 
def add(num1, num2):
    response = num1 + num2
    return response

print(add(15, 5))
print(add(-5, 5))