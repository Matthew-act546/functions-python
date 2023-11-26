name = "matthew"

def greet(username):
    print("Welcome "+ username + "!")

greet(name)

def pet(pet_type, pet_name, age=None):
    print("I have a " + pet_type.title() + ".")
    print("My " + pet_type.title() + " name is " + pet_name.title() + ".")
    print()

pet(pet_type="dog", pet_name="pepper")
pet(pet_type="cat", pet_name="ginger")

#default parameters
def pet(pet_name, pet_type='dog'):
    print("I have a " + pet_type.title() + ".")
    print("My " + pet_type.title() + " name is " + pet_name.title() + ".")
    print()

pet(pet_name="pepper")
pet(pet_type="cat", pet_name="ginger")

def person(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

dev = person("Matthew David", "fernandez")
print("The developer name is ", dev)

def pers(n1, n2, middle_name=''):
    if middle_name:
        FN = n1 + " " + middle_name + " " + n2
    else:
        FN = n1 + " " + n2
    return FN.title()

name = pers("matthew", "fernandez", "cabance")
print(name)

#returning dictionary 
def build_person(f, l, age):
    human = {'first_name': f, 'last_name': l}
    if age:
        human['age'] = age

    return human

man = build_person("Matthew David", "Fernandez", age=16)
print(man)

#function in list
def welcome(names):
    for name in names:
        msg = "Welcome " + name + "!"
        print(msg)

welcomes = ["matthew", "David", "fernandez"]
welcome(welcomes)

def make_pizza(*toppings):    
    print("\nMaking a pizza with the following toppings:")    
    for topping in toppings:        
        print("- " + topping)        
        
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')

