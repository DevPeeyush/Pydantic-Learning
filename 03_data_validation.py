
from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import List, Dict,Optional,Annotated


# Pydantic schema
# Data validation
class Patient(BaseModel):
    # name: str = Field(max_digits=50)
    # add meta deta
    name : Annotated[str, Field(max_length=50, title='Name of the paitient',description='Give the name of patient in min. 50 words')]
    email : EmailStr
    linkedin_url : AnyUrl
    age: int
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print(patient.linkedin_url)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print("updated")


patient_info = {
    'name': 'Peeyush',
    'email' : 'peeyush@gmail.com',
    'linkedin_url' : 'https://linkedin.com/peeyushverma1',
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
