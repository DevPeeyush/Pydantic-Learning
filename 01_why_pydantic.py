# Type validation problem:
# Without Pydantic, every function must repeat manual checks for types and
# constraints, which is easy to miss and produces inconsistent errors.
# Pydantic validates untrusted input against one model at the boundary,
# preventing invalid data from reaching application logic or the database.
import pydantic


def insert_patient_data(name, age):
    if type(name) == str and type(age) == int:
        if(age < 0):
            raise TypeError("Age cann't be negative")
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError("Incorrect data type")
    
    
def update_patient_data(name, age):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("updated")
    else:
        raise TypeError("Incorrect data type")
insert_patient_data("peeyush",32)


print("pydantic version", pydantic.__version__)