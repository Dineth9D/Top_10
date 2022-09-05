from countryinfo import CountryInfo

count = input("Enter your country:")
country = CountryInfo(count)

print("Capital city is: ", country.capital())
print("Currencies is :", country.currencies())
print("Language is :", country.languages())
print("Borders are :", country.borders())
print("Others names :", country.alt_spellings())
