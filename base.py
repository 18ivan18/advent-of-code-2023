from collections import defaultdict
import json
import os
import sys

advent_of_code_base_url = 'https://adventofcode.com'
solutions_dir = 'solutions'


def today() -> int:
    days = [int(x) for x in os.listdir(solutions_dir)]
    days.append(0)
    return sorted(days)[-1]


env = json.load(open('.env' if os.path.exists('.env') else '.env.sample'))
session_cookie = env['session']
year = env['year']
day = int(sys.argv[1]) if len(sys.argv) > 1 else today()
day_str = f"{day:02}"
