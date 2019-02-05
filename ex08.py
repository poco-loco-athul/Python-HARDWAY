#ex08 Printing, Printing

formatter = "{} {} {}"

print(formatter.format(1,2,3))
print(formatter.format(formatter, formatter, formatter))
print(formatter.format(formatter.format("It's",  "not", "complicated."),"Is", "it?"))
