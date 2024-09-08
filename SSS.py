def display_sss(gross):
    sss_contribution = 0
    if gross >= 1000 and gross <= 3249.99:
        sss_contribution = 135.00
    elif gross >= 3250 and gross <= 3749.99:
        sss_contribution = 157.50
    elif gross >= 3750 and gross <= 4249.99:
        sss_contribution = 180.00
    elif gross >= 4250 and gross <= 4749.99:
        sss_contribution = 202.50
    elif gross >= 4750 and gross <= 5249.99:
        sss_contribution = 225.00
    elif gross >= 5250 and gross <= 5749.99:
        sss_contribution = 247.50
    elif gross >= 5750 and gross <= 6499.99:
        sss_contribution = 270.00
    elif gross >= 6250 and gross <= 6749.99:
        sss_contribution = 292.50
    elif gross >= 6750 and gross <= 7249.99:
        sss_contribution = 315.00
    elif gross >= 7250 and gross <= 7749.99:
        sss_contribution = 337.50
    elif gross >= 7750 and gross <= 8249.99:
        sss_contribution = 360.00
    elif gross >= 8250 and gross <= 8749.99:
        sss_contribution = 382.50
    elif gross >= 8750 and gross <= 9249.99:
        sss_contribution = 405.00
    elif gross >= 9250 and gross <= 9749.99:
        sss_contribution = 422.50
    elif gross >= 9750 and gross <= 10249.99:
        sss_contribution = 450.00
    elif gross >= 10250 and gross <= 10749.99:
        sss_contribution = 472.50
    elif gross >= 10750 and gross <= 11249.99:
        sss_contribution = 495.00
    elif gross >= 11250 and gross <= 11749.99:
        sss_contribution = 517.50
    elif gross >= 11750 and gross <= 12249.99:
        sss_contribution = 540.00
    elif gross >= 12250 and gross <= 12749.99:
        sss_contribution = 562.50
    elif gross >= 12750 and gross <= 13249.99:
        sss_contribution = 585.00
    elif gross >= 13250 and gross <= 13749.99:
        sss_contribution = 607.50
    elif gross >= 13750 and gross <= 14249.99:
        sss_contribution = 630.00
    elif gross >= 14250 and gross <= 14749.99:
        sss_contribution = 652.50
    elif gross >= 14750 and gross <= 15249.99:
        sss_contribution = 675.00
    elif gross >= 15250 and gross <= 15749.99:
        sss_contribution = 697.50
    elif gross >= 15750 and gross <= 16249.99:
        sss_contribution = 720.00
    elif gross >= 16250 and gross <= 16749.99:
        sss_contribution = 742.50
    elif gross >= 16750 and gross <= 17249.99:
        sss_contribution = 765.00
    elif gross >= 17250 and gross <= 17749.99:
        sss_contribution = 787.50
    elif gross >= 17750 and gross <= 18249.99:
        sss_contribution = 810.00
    elif gross >= 18250 and gross <= 18749.99:
        sss_contribution = 832.50
    elif gross >= 18750 and gross <= 19249.99:
        sss_contribution = 855.00
    elif gross >= 19250 and gross <= 19749.99:
        sss_contribution = 877.50
    elif gross >= 19750 and gross <= 20249.99:
        sss_contribution = 900.00
    elif gross >= 20250 and gross <= 20749.99:
        sss_contribution = 900.00
    elif gross >= 20750 and gross <= 21249.99:
        sss_contribution = 900.00
    elif gross >= 21250 and gross <= 21749.99:
        sss_contribution = 900.00
    elif gross >= 22250 and gross <= 22749.99:
        sss_contribution = 900.00
    elif gross >= 22750 and gross <= 23249.99:
        sss_contribution = 900.00
    elif gross >= 23250 and gross <= 23749.99:
        sss_contribution = 900.00
    elif gross >= 23750 and gross <= 24249.99:
        sss_contribution = 900.00
    elif gross >= 24250 and gross <= 24749.99:
        sss_contribution = 900.00
    elif gross >= 24750 and gross <= 24749.99:
        sss_contribution = 900.00
    else:
        sss_contribution = 900.00
    return sss_contribution