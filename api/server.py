from fastapi import FastAPI

app = FastAPI(debug=True)

import api.controller.manufacturer # noqa
import api.controller.househould # noqa
