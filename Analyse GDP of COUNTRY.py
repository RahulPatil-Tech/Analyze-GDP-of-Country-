import numpy as np
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
gdp_per_capita = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

max_gdp_per_capita = gdp_per_capita.argmax()
contry_with_max_gdp_per_capita = countries[max_gdp_per_capita]
contry_with_max_gdp_per_capita

min_gdp_per_capita = gdp_per_capita.argmin()
contry_with_min_gdp_per_capita = countries[min_gdp_per_capita]

for country in countries:
    print('ecaluatiing country ()',format(country))
for i in range(len(countries)):
    country = countries[1]
    country_gdp_per_capita = gdp_per_capita[1] 
    print('country {} per capita gdp is {}'.format(country,country_gdp_per_capita))
print(gdp_per_capita.max())
print(gdp_per_capita.min())
print(gdp_per_capita.mean())
print(gdp_per_capita.std())
print(gdp_per_capita.sum())

