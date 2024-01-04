from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import api.controller.manufacturer # noqa
import api.controller.household # noqa
import api.controller.appliance # noqa
import api.controller.power_generator # noqa