import GetInput

def calculate_fuel_consumption(module: int) -> int:
    fuel = module//3 - 2
    if fuel > 0:
        return fuel + calculate_fuel_consumption(fuel)
    return 0


modules = GetInput.get_numberd_list("../Input/Day1.txt")

total_fuel = 0
for module in modules:
    total_fuel += calculate_fuel_consumption(module)
print(total_fuel)