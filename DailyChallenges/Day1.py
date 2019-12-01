import GetInput

def calculate_module_fuel_consumption(module: int) -> int:
    fuel = module//3 - 2
    if fuel > 0:
        return fuel + calculate_module_fuel_consumption(fuel)
    return 0

def calculate_total_fuel_consumption(modules: list) -> int:
    total_fuel = 0
    for module in modules:
        total_fuel += calculate_module_fuel_consumption(module)
    return total_fuel

modules = GetInput.get_numberd_list("../Input/Day1.txt")
print(calculate_total_fuel_consumption(modules))