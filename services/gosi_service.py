from schemas.gosi_schema import GosiRequest, GosiResponse


def calculate_gosi(data: GosiRequest) -> GosiResponse:

    employee_nationality = data.employee_type.lower()

    if employee_nationality == "saudi":
        housing_allowance = data.basic_salary * 3 / 12

        employee_rate = 0.0975
        employer_rate = 0.1175

    elif employee_nationality == "non-saudi":
        housing_allowance = data.basic_salary * 2 / 12
        employee_rate = 0
        employer_rate = 0.02

    else:
        raise ValueError("Invalid employee nationality")
    
    subscription_salary = min(data.basic_salary + housing_allowance, 45000) # Cap the subscription salary at 45,000
    transportation_allowance = data.transportation_allowance
    employee_deduction = subscription_salary * employee_rate
    employer_contribution = subscription_salary * employer_rate
    total_salary = data.basic_salary + housing_allowance + transportation_allowance
    net_after_gosi = total_salary - employee_deduction

    return GosiResponse(
        employee_type=employee_nationality,
        subscription_salary=round(subscription_salary, 2),
        housing_allowance=round(housing_allowance, 2),
        transportation_allowance=round(transportation_allowance, 2),
        employee_deduction=round(employee_deduction, 2),
        employer_contribution=round(employer_contribution, 2),
        net_after_gosi=round(net_after_gosi, 2),
        total_salary=round(total_salary, 2),
    )