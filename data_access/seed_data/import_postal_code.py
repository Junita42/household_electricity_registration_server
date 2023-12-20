# import_data.py
import csv
from sqlalchemy.orm import sessionmaker
from data_access.models.valid_postal import Valid_Postal # Import the models
from sqlalchemy import create_engine
from data_access.models.base_model import Base

# Replace with your database URI
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/cs6400_su23_team002')

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def import_postal_codes(csv_filepath):
    with Session() as session:
        with open(csv_filepath, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                postal_code_entry = Valid_Postal(
                    postal_code=row[0],
                    city=row[1],
                    state=row[2],
                    latitude=row[3],
                    longitude=row[4]
                )
                session.add(postal_code_entry)
            session.commit()

if __name__ == "__main__":
    import_postal_codes('/Users/junita/Documents/projects/electricity_fastapi/data/postal_codes.csv')


