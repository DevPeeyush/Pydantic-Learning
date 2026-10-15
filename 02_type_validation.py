
from pydantic import BaseModel
from typing import List, Dict,Optional


# Pydantic schema
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


# Type validation
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")


patient_info = {
    'name': 'Peeyush',
    'age': 22,
    'weight': 88.63,
    'married': False,
    # 'allergies': ['dust', 'smoke', 'peanuts'],
    'contact_details': {
        'Phone no.': '98765',
        'email': 'abc@gmail.com'
    }
}

# ** Unpacks the dictionary and validates its data against the model.
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
