def get_philhealth(basic_income):
    if basic_income <= 10000:
        return 300/2
    elif basic_income > 10000 and basic_income < 60000:
        return (basic_income * 0.04)/2
    else:
        return 1800/2
