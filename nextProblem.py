import webbrowser
import glob
import re


last_problem_file = sorted(glob.glob("problem*.py"))[-1]

last_problem = int(re.search("[0-9]+", last_problem_file).group(0))
print(last_problem)

link = "https://projecteuler.net/problem=" + str(last_problem+1)

webbrowser.open(link)
