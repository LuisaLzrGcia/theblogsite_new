print ("¿Cual es tu nombre?")
first_name = input ()
print ("¿Cual es tu puesto?")
job_name = input ()
print ("¿primer adjetivo?")
first_adjective = input ()
print ("¿segundo adjetivo?")
second_adjective = input()
print (" primer comida?")
first_food = input()
print ("segunda comida?")
second_food = input()
print ("se sienten?")
a_feeling = input()

message = (
    f"{first_name} started their first Generation course today. They are training as a {job_name}. "
    f"They found their cohort to be {first_adjective} and {second_adjective}. "
    f"Their favorite foods are {first_food} and {second_food}. They feel {a_feeling}."
)
print(message)
