def get_pagibig(gross):
    if gross < 1500:
        return gross * 0.01
    else:
        limit = gross * 0.02
        if limit < 100:
            return limit
        else:
            return 100

