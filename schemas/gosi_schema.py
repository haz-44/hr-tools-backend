from pydantic import BaseModel, Field


class GosiRequest(BaseModel):
    basic_salary: float = Field(gt=0) # gt = grater than
    employee_type: str = Field(examples=['saudi', 'non-saudi'])
    transportation_allowance: float


class GosiResponse(BaseModel):
    employee_type: str
    subscription_salary: float
    housing_allowance: float
    transportation_allowance: float
    employee_deduction: float
    employer_contribution: float
    net_after_gosi: float
    total_salary: float