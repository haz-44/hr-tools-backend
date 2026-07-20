from schemas.eos_schema import EosRequest, EosResponse

def calculate_eos(data: EosRequest):
    salary = data.salary
    years = data.service_years
    reason = data.reason

    first_five_years = min(years, 5)
    remain_years = max(years - 5, 0)
    reward = (salary * 0.5 * first_five_years + salary * remain_years)

    if reason == 'resignation':
        if years < 2:
            reward = 0
        elif years <= 5:
            reward = reward * 1/3
        elif years < 10:
            reward = reward * 2/3
       
    return EosResponse(eos_amount=reward)