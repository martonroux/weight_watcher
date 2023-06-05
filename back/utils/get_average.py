def get_average(numbers: list) -> float:
    if len(numbers) == 0:
        return 0.0
    else:
        return sum(numbers) / len(numbers)
