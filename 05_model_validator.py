
from pydantic import BaseModel, model_validator,EmailStr
from typing import List, Dict,Optional


# Pydantic schema
class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
            
# Model Validator
    @model_validator(mode='after')
    def valid_emergence_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise TypeError("Patient older than 60 must have emergency contact")
        return model


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print("updated")


patient_info = {
    'name': 'Peeyush Verma',
    'email' : 'abc@icici.in',
    'age': 65,
    'weight': 88.63,
    'married': False,
    # 'allergies': ['dust', 'smoke', 'peanuts'],
    'contact_details': {
        'Phone no.': '9876585265',
        'emergency' : '9664155228'
    }
}

# ** Unpacks the dictionary and validates its data against the model.
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
