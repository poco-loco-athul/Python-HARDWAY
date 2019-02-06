#ex14 Prompting and Passing

from sys import argv

script, usr = argv
prompt ='> '

print(f"Hi {usr}, what is your favorite color?")
col = input(prompt)

print(f"""
Alright, {usr}. Your favorite color is {col}
and you have just used script {script}. Nice
""")
