def get_median(numbers: list) -> float:
    if len(numbers) == 0:
        return 0.0
    else:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            mid = n // 2
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            mid = n // 2
            return sorted_numbers[mid]
