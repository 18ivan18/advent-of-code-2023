#!/usr/bin/env python3
import os
import sys
import requests
import shutil
import stat
from bs4 import BeautifulSoup
from base import solutions_dir, advent_of_code_base_url, year, day, day_str


if (not os.path.exists(solutions_dir)):
    os.mkdir(solutions_dir)

def get_day_url(day: int) -> str:
    return f"{advent_of_code_base_url}/{year}/day/{day}"

url = get_day_url(day)

response = requests.get(url)

if(not response or (len(sys.argv) > 1 and day_str in os.listdir(solutions_dir))):
    print('\033[1m' + "You're all up to date.")
    exit(0)

shutil.copytree('day_x_template', os.path.join(solutions_dir, day_str))
main_py_dir = os.path.join(solutions_dir, day_str, 'main.py')
os.chmod(main_py_dir, os.stat(main_py_dir).st_mode | stat.S_IEXEC)

soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
with open(os.path.join(solutions_dir, day_str, 'README.md'), 'w') as fd:
    fd.write(soup.find('main').get_text())

print('\033[1m' + f"Successfully created day {day}!\n{url}")
