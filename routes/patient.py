from fastapi import APIRouter
from config.db import conn
from models.patient import patients
from schemas.patient import Patient
from fastapi.responses import JSONResponse

patient = APIRouter()

@patient.get('/patients/list', tags=["patients"], response_model=list[Patient], description="Get all patients")
def get_all_patients():
    patients_rows = conn.execute(patients.select()).fetchall()
    patients_dicts = [row._asdict() for row in patients_rows]
    return JSONResponse(content=patients_dicts)


@patient.post('/create_patient', tags=["patients"], response_model=Patient)
def create_patient(patient: Patient):
    try:
        new_patient = {
            "name": patient.name,
            "fatherLastName": patient.fatherLastName,
            "motherLastName": patient.motherLastName,
            "birthDate": patient.birthDate,
            "cellPhone": patient.cellPhone,
            "homePhone": patient.homePhone,
            "address": patient.address,
            "gender": patient.gender,
            "email": patient.email,
            "civilStatus": patient.civilStatus,
            "occupation": patient.occupation,
            "grades": patient.grades
        }
        result = conn.execute(patients.insert().values(new_patient))
        conn.commit()  # Commit the changes
        created_patient_id = result.lastrowid
        created_patient = {**new_patient, "id": created_patient_id}
        return created_patient
    
    except Exception as e:
        print("Error:", e)
        raise

@patient.delete('/patients/delete/{id}', tags=["patients"], description="Delete patient by id")
def delete_patient(id: int):
    try:
        conn.execute(patients.delete().where(patients.c.id == id))
        conn.commit()
        return {"message": "Patient deleted"}
    except Exception as e:
        print("Error:", e)
        raise


@patient.put('/patients/update/{id}', tags=["patients"], response_model=Patient, description="Update patient by id")
def update_patient(id: int, patient: Patient):
    try:
        conn.execute(
            patients.update()
            .values(
                name=patient.name,
                fatherLastName=patient.fatherLastName,
                motherLastName=patient.motherLastName,
                birthDate=patient.birthDate,
                cellPhone=patient.cellPhone,
                homePhone=patient.homePhone,
                address=patient.address,
                gender=patient.gender,
                email=patient.email,
                civilStatus=patient.civilStatus,
                occupation=patient.occupation,
                grades=patient.grades
            )
            .where(patients.c.id == id)
        )
        conn.commit()
        return patient
    except Exception as e:
        print("Error:", e)
        raise