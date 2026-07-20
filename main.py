from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.gosi_schema import GosiRequest, GosiResponse
from schemas.eos_schema import EosRequest, EosResponse
from schemas.rs_schema import RsRequest, RsResponse
from services.gosi_service import calculate_gosi
from services.eos_service import calculate_eos
from services.rs_service import calculate_rs



app = FastAPI(
    title="HR Tools API",
    description="API for Saudi HR calculators",
    version="1.0.0",
)


# السماح لواجهة React بالاتصال مع FastAPI
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "HR Tools API is running",
        "available_tools": [
            "/hr-tools/gosi",
            "/hr-tools/eos",
            "/hr-tools/rs",
        ],
    }


@app.post("/hr-tools/gosi", response_model=GosiResponse)
def gosi_calculator(data: GosiRequest):
    return calculate_gosi(data)


@app.post("/hr-tools/eos", response_model=EosResponse)
def eos_calculator(data: EosRequest):
    return calculate_eos(data)

@app.post("/hr-tools/rs", response_model=RsResponse)
def rs_calculator(data: RsRequest):
    return calculate_rs(data)