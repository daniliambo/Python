# title Salary Project
# description Salary Project
# code

import requests
import json
import datetime


def read(path):
    with open(path, 'r') as f:
        content = json.loads(f.read())
    return content


def write(path, content):
    with open(path, 'w') as f:
        json_string = json.dumps(content)
        f.write(json_string)


def generate_url(year, month):
    url = """https://isdayoff.ru/api/getdata?year={}&month={}&delimeter= """.format(year, month)
    return url


def get_request(year, month):
    url = generate_url(year, month)
    response = requests.request('GET', url=url)
    content = response.content.decode('utf-8')
    return content


def count_days(content):
    days = map(int, content.split(' '))

    c = 0
    for d in days:
        if d == 0:
            c += 1

    return c


def calc_monthly_salary(salary, n):
    return round(salary / n / 8, 2)


def convert_month_to_number(month):
    return datetime.datetime.strptime(month.upper(), "%B").month


def main():
    # init paths
    read_path = 'input.json'
    write_path = 'output.json'

    # load the content
    json_content = read(read_path)

    year, month, salary = json_content['year'], convert_month_to_number(json_content['month']), \
                          json_content['salary']

    content = get_request(year, month)
    n = count_days(content)

    daily_salary = calc_monthly_salary(salary, n)
    json_content['hour_income'] = daily_salary

    write(write_path, json_content)


if __name__ == '__main__':
    main()
