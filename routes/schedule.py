from fastapi import APIRouter
from config.db import conn
from models.schedule import schedules
from schemas.schedule import Schedule
from fastapi.responses import JSONResponse

schedule = APIRouter()

@schedule.get('/schedule/list', tags=["schedule"], response_model=list[Schedule], description="Get all schedule")
def get_all_schedule():
    schedule_rows = conn.execute(schedules.select()).fetchall()
    schedules_dicts = [row._asdict() for row in schedule_rows]
    return JSONResponse(content=schedules_dicts)


@schedule.post('/schedule/create', tags=["schedule"], response_model=Schedule)
def create_schedule(schedule: Schedule):
    try:
        new_schedule = {
            "name": schedule.name,
            "fatherLastname": schedule.fatherLastname,
            "motherLastname": schedule.motherLastname,
            "birthDate": schedule.birthDate,
            "cellPhone": schedule.cellPhone,
            "homePhone": schedule.homePhone,
            "gender": schedule.gender,
            "email": schedule.email,
            "dateQuery": schedule.dateQuery,
            "hoursConsultation": schedule.hoursConsultation,
            "OfficeName": schedule.OfficeName,
            "whoRecommends": schedule.whoRecommends,
            "queryreason": schedule.queryreason
        }
        result = conn.execute(schedules.insert().values(new_schedule))
        conn.commit()  # Commit the changes
        created_schedule_id = result.lastrowid
        created_schedule = {**new_schedule, "id": created_schedule_id}
        return created_schedule
    
    except Exception as e:
        print("Error:", e)
        raise


@schedule.delete('/schedule/delete/{id}', tags=["schedule"], description="Delete schedule by id")
def delete_schedule(id: int):
    try:
        conn.execute(schedules.delete().where(schedules.c.id == id))
        conn.commit()
        return {"message": "Schedule deleted"}
    except Exception as e:
        print("Error:", e)
        raise


@schedule.put('/schedule/update/{id}', tags=["schedule"], response_model=Schedule, description="Update schedule by id")
def update_schedule(id: int, schedule: Schedule):
    try:
        conn.execute(
            schedules.update()
            .values(
                name=schedule.name,
                fatherLastname=schedule.fatherLastname,
                motherLastname=schedule.motherLastname,
                birthDate=schedule.birthDate,
                cellPhone=schedule.cellPhone,
                homePhone=schedule.homePhone,
                gender=schedule.gender,
                email=schedule.email,
                dateQuery=schedule.dateQuery,
                hoursConsultation=schedule.hoursConsultation,
                OfficeName=schedule.OfficeName,
                whoRecommends=schedule.whoRecommends,
                queryreason=schedule.queryreason
            )
            .where(schedules.c.id == id)
        )
        conn.commit()
        return schedule
    except Exception as e:
        print("Error:", e)
        raise