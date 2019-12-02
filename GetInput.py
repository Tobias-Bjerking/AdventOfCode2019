def get_numbered_list(path: str) -> list:
    file_input = open(path).read()
    values = list(map(int, file_input.splitlines()))
    return values


def get_list(path: str) -> list:
    file_input = open(path).read()
    values = list(file_input.splitlines())
    return values


def get_numbered_line(path: str) -> list:
    values = get_list(path)
    return list(map(int, values[0].split(",")))
