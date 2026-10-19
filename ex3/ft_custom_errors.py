class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(tomato_life: bool) -> None:
    if not tomato_life:
        raise PlantError("The tomato plant is wilting!")


def check_water(water: float) -> None:
    if water < 0.5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("\nTesting PlantError...")
    try:
        check_plant(False)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water(0.3)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant(False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(0.3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    test_custom_errors()

    print("\nAll custom error types work correctly!")
