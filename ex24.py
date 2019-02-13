#Ex24: More Pratice

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('With a starting point of: {}'.format(start_point))
print(f"We'd have {int(beans)} beans, {int(jars)} jars, and {int(crates)} crates.")

start_point /= 50

print('We can also do that this way:')
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
