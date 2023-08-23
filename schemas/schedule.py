from typing import Optional
from pydantic import BaseModel

class Schedule(BaseModel):
    id: Optional[int]
    name: str
    fatherLastname: str
    motherLastname: str
    birthDate: str
    cellPhone: int
    homePhone: int
    gender: str
    email: str
    dateQuery: str
    hoursConsultation: str
    OfficeName: str
    whoRecommends: str
    queryreason: str


