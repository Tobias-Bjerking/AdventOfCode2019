def get_numberd_list(path: str) -> list:
    input = open(path).read()
    values = list(map(int, input.splitlines()))
    return values

def get_list(path: str) -> list:
    input = open(path).read()
    values = list(input.splitlines())
    return values