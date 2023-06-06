def get_evolution(numbers: list) -> float:                                # FUNCTION TO CALCULATE EVOLUTION OF LIST
    if len(numbers) == 0:
        return 0.0

    evolution = ((numbers[len(numbers) - 1] - numbers[0]) / numbers[0]) * 100

    return evolution
