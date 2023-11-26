def add_person(first_name, last_name):
    full_name = first_name + " " + last_name
    
    return full_name.title()

while True:
    print("Add a person\nif you want to quit press 'q'.")
    f_name = input("Enter you're first name here: ")
    l_name = input("Enter you're last name here:")
    user = add_person(first_name=f_name, last_name=l_name)

    if f_name.lower() == 'q' or l_name.lower() == 'q':
        print("Ending the terminal thank you for adding a members!")
        break
    else:
        print(user)