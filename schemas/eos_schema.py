from pydantic import BaseModel, Field


class EosRequest(BaseModel):
    # البيانات الي المفروض استلمها من الكلاينت
    # الراتب الاجمالي + عدد سنوات الخدمة
    salary: float = Field(gt=0)
    service_years: float = Field(gt=0)
    contract_type: str = Field (examples=['limited', 'unlimited'])
    reason: str = Field(examples=['resignation', 'agreement', 'by_employer'])



class EosResponse(BaseModel):
    # البيانات الي راح ارسلها للكلاينت بعد المعالجة
    # قيمة مبلغ مكافئة نهاية الخدمة
    eos_amount: float