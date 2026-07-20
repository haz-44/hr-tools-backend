from schemas.rs_schema import RsRequest, RsResponse


def calculate_rs(data: RsRequest) -> RsResponse:
    
    salary = data.salary
    years = data.years

    rs_amount = salary * years / 40

    return RsResponse(rs_amount=rs_amount)