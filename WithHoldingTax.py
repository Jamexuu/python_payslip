def display_with_holding_tax(sss, phil_health, pag_ibig, gross):
    sumation = sss + phil_health + pag_ibig
    subtracted = gross - sumation
    with_tax = 0

    if subtracted < 20833:
        with_tax = sumation
        return with_tax
    elif subtracted >= 20833 or subtracted <= 33333:
        with_tax = (subtracted - 20833) * 0.20
        return with_tax
    elif subtracted >= 33333 or subtracted <= 66667:
        with_tax = (subtracted - 33333) * 0.25 + 2500
        return with_tax
    elif subtracted >= 66667 or subtracted <= 166667:
        with_tax = (subtracted - 66667) * 0.30 + 10833.83
        return with_tax
    elif subtracted >= 166667 or subtracted <= 666667:
        with_tax = (subtracted - 166667) * 0.32 + 40833.33
        return with_tax
    elif subtracted >= 666667 or subtracted <= 999999999.99:
        with_tax = (subtracted - 666667) * 0.35 + 200833.33
        return with_tax


