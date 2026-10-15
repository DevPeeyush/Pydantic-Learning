
from pydantic import BaseModel, computed_field,EmailStr
from typing import List, Dict,Optional


# Pydantic schema
class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight: float
    height : float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
        
    # computing BMi using height and weight
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
                
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print("BMI : ",patient.calculate_bmi)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print("BMI : ",patient.calculate_bmi)
    print("updated")


patient_info = {
    'name': 'Peeyush Verma',
    'email' : 'abc@icici.in',
    'age': 22,
    'weight': 88.63,
    'height' : 1.75,
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
