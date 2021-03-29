import re
pattern = re.compile("-?[.0-9]*;-?[.0-9]*")
split_token = ";"

def exctract_data(file):
    x_data, y_data = [], []
    for line in file:
        is_data = pattern.match(line)
        if not is_data:
            continue
        x, y = line.split(split_token)
        x_data.append(float(x))
        y_data.append(float(y))
    return x_data, y_data