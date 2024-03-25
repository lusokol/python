def give_bmi(height: list[int | float], weight: list[int | float]):
    """
Calculate BMI values based on given heights and weights.

give_bmi(height: list[int | float], weight: list[int | float]):
return list[int | float]
    """
    try:
        assert (weight and height and None not in weight and
                None not in height), "Height and Weight can't be empty."
        if (len(height) != len(weight)):
            raise AssertionError("Height and weight doesn't have the same\
 number of value")
        assert all(isinstance(h, (int, float)) for h in height), "Height\
 doesn't contain only int or float."
        assert all(isinstance(w, (int, float)) for w in weight), "Weight\
 doesn't contain only int or float."
        bmi_lst = [w / (h * h) for w, h in zip(weight, height)]
        return bmi_lst
    except AssertionError as error:
        print(f"AssertionError: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Determine whether BMI values are above a given limit.

apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
return list[bool]
    """
    try:
        assert bmi and None not in bmi, "BMI list emty."
        assert all(isinstance(b, (int, float)) for b in bmi), "BMI list\
 doesn't contain only int or float."
        assert isinstance(limit, int), "Limit (second argument)\
 have to be an int"
        limit_applied = [b > limit for b in bmi]
        return limit_applied
    except AssertionError as error:
        print(f"AssertionError: {error}")
