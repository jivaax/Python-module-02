class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(valid: bool) -> None:
    print("Opening watering system")
    try:
        if valid:
            water_plant("Tomato")
            water_plant("Lettuce")
            water_plant("Carrots")
        else:
            water_plant("Tomato")
            water_plant("lettuce")
            water_plant("carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system(True)
    print("\nTesting invalid plants...")
    test_watering_system(False)
    print("\nCleanup always happens, even with errors!")
