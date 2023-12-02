from fastapi import FastAPI
from database import connect
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CheckEmailRequestBody(BaseModel):
    email: str

# endpoint to check email existance
@app.post("/emails")
async def check_email(body: CheckEmailRequestBody):
    print(body.email)
    # check email in db
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM Household WHERE email = %s"
    cursor.execute(query, (body.email,))
    email_exists = cursor.fetchone() is not None

    # Close the connection
    cursor.close()
    conn.close()

    return {"email": body.email, "is_exist": email_exists}
