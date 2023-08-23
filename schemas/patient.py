from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    id: Optional[int]
    name: str
    fatherLastName: str
    motherLastName: str
    birthDate: str
    cellPhone: int
    homePhone: str
    address: str
    gender: str
    email: str
    civilStatus: str
    occupation: str
    grades: str
