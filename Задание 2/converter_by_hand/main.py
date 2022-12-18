# title Converter csv to json
# description By hand
# code


# data input / output
def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


# read_data_to_list
def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


# preparation
def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(titles, row):
    values = row.strip().split(',')

    l = list()
    [l.extend([k.strip(), v.strip()]) for k, v in \
     dict(zip(titles, values)).items()]

    # double braces expected
    data = """  {{
    "{}": {},
    "{}": "{}",
    "{}": {},
    "{}": {},
    "{}": {}
  }}""".format(*l)

    return data


def convert_csv_to_json(data):
    titles, data = prepare_data(data)

    content = [convert_row_to_pretty_json(titles, row) for row in data]
    content = ',\n'.join(content)
    content = ''.join(['[\n', content, '\n]'])

    return content


def main():
    data = read_data_to_list("input.csv")
    result = convert_csv_to_json(data)
    write_data("output.json", result)


if __name__ == "__main__":
    main()
