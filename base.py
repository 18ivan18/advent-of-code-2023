import json
import os
import sys

advent_of_code_base_url = 'https://adventofcode.com'
solutions_dir = 'solutions'


def today() -> int:
    days = [int(x) for x in os.listdir(solutions_dir)]
    days.append(0)
    return sorted(days)[-1]


# Opening JSON file
f = open('.env')

# returns JSON object as
# a dictionary
env = json.load(f)
session_cookie = env['session']
year = 2023
day = int(sys.argv[1]) if len(sys.argv) > 1 else today()
day_str = f"{day:02}"