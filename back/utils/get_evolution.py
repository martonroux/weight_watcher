def get_evolution(numbers: list) -> float:                                # FUNCTION TO CALCULATE EVOLUTION OF LIST
    if len(numbers) == 0:
        return 0.0

    evolution = [0]

    for i in range(1, len(numbers)):
        current_evolution = (numbers[i] - numbers[i - 1]) / numbers[i - 1]
        evolution.append(current_evolution)

    return evolution                    # PROBABLY INCORRECT
