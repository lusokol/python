import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
Slice family from start to end

slice_me(family: list, start: int, end: int):
return list sliced
    """
    try:
        assert isinstance(family, list) or len(family), "Family is not a list."
        assert isinstance(start, int), "Start is not an int"
        assert isinstance(end, int), "End is not an int"
        assert all(isinstance(item, list) and (len(item) == len(family[0]))
                   for item in family), "Every items in\
 the list doesn't have the same lenght or aren't list."
        arr = np.array(family)
        subset = arr[start:end]
        print(f"My shape is : {arr.shape}")
        print(f"My new shape is : {subset.shape}")
        return subset.tolist()
    except AssertionError as error:
        print(f"AssertionError: {error}")
