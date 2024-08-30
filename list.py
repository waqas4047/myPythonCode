countries=["pakitan","india","afghanistan","saudi","malesia","nepal","bangladash","katmandu"]
print(countries)
print(countries[4])
# this will find the index of afghanistan
print(countries.index("afghanistan"))
# i want to print the countries name from afghanistan upto end we can do that like
print(countries[2:])
# now iwant to print form india to malesia
print(countries[1:5])
countries.sort()
print(countries)

# now i want to sort it in reverse order
countries.sort(reverse=True)
print(countries)

# to change element in the list

countries[1]="america"
print(countries)

# we can also give index in minus like
print(countries[-2])

# to find items in the list

print(len(countries))

# we can also specify a list like below
new=list(("hello","newhere",2,True))
print(type(new))
print(new)