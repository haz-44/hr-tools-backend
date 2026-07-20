from pydantic import BaseModel, Field



class RsRequest(BaseModel):
    # البيانات الي المفروض استلمها من الكلاينت
    # الراتب الاجمالي + عدد سنوات الخدمة
    salary: float = Field(gt=0)
    years: float = Field(gt=0)



class RsResponse(BaseModel):
    # البيانات الي راح ارسلها للكلاينت بعد المعالجة
    # عبارة عن قيمة مبلغ الراتب التقاعدي
    rs_amount: float