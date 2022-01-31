import psycopg2
import time
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import models
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

# connect to database created in postgres
while True:

    try:
        conn = psycopg2.connect(host='localhost', database="animal_store", user='postgres',
                                password='solstad', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        # sys.exit(10)
        # import time, this will make the while loop wait 2 secs before starting over.
        time.sleep(2)
