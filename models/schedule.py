from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

schedules = Table("schedule", meta,
       Column("id", Integer, primary_key=True),
       Column("name", String(255)),
       Column("fatherLastname", String(255)),
       Column("motherLastname", String(255)),
       Column("birthDate", String(255)),
       Column("cellPhone", String(255)),
       Column("homePhone", String(255)),
       Column("gender", String(255)),
       Column("email", String(255)),
       Column("dateQuery", String(255)),
       Column("hoursConsultation", String(255)),
       Column("OfficeName", String(255)),
       Column("whoRecommends", String(255)),
       Column("queryreason", String(255)))

meta.create_all(engine)