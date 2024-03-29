def get_numbered_list(path: str) -> list:
    file_input = open(path).read()
    values = list(map(int, file_input.splitlines()))
    return values


def get_list(path: str) -> list:
    file_input = open(path).read()
    values = list(file_input.splitlines())
    return values


def get_map(path: str, split: str = ",") -> dict:
    values = get_list(path)
    dictionary = {}
    for string in values:
        m, v = string.split(split)
        if m not in dictionary.keys():
            dictionary[m] = [v]
        else:
            dictionary[m].append(v)
    return dictionary


def get_numbered_line(path: str, split: str = ",") -> list:
    values = get_list(path)
    return list(map(int, values[0].split(split)))


def get_line(path: str, split: str = ",") -> list:
    values = get_list(path)
    return list(values[0].split(split)), list(values[1].split(split))
