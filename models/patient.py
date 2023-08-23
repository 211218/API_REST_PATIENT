from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

patients = Table("patients", meta,
        Column("id", Integer, primary_key=True),
        Column("name", String(255)),
        Column("fatherLastName", String(255)),
        Column("motherLastName", String(255)),
        Column("birthDate", String(255)),
        Column("cellPhone", String(255)),
        Column("homePhone", String(255)),
        Column("address", String(255)),
        Column("gender", String(255)),
        Column("email", String(255)),
        Column("civilStatus", String(255)),
        Column("occupation", String(255)),
        Column("grades", String(255)))

meta.create_all(engine)