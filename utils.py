def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def calorie_estimator(goal, weight):
    if goal == "Fat Loss":
        return weight * 22
    elif goal == "Muscle Gain":
        return weight * 30
    else:
        return weight * 26