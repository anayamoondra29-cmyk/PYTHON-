country_code={"India":91,"Australia":61,"Nepal":977}

country_code["UAE"]=971

print(country_code)

countires=input("enter a country")

print(country_code.get(countires,'not avalible'))

print(country_code.pop("Nepal"))

print(country_code)

print(country_code.clear())

print(country_code)