
from pydantic import BaseModel, field_validator,EmailStr
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
    
    # Field validator

    # required particular email
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.in']
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value

    # required name in capital
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    # validating the age
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            TypeError("Age should be between 1  to 100")
        
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
