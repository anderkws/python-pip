def get_population(country_dic):
    population_dict = {
        '2022' : int(country_dic['2022 Population']),
        '2020' : int(country_dic['2020 Population']),
        '2015' : int(country_dic['2015 Population']),
        '2010' : int(country_dic['2010 Population']),
        '2000' : int(country_dic['2000 Population']),
        '1990' : int(country_dic['1990 Population']),
        '1980' : int(country_dic['1980 Population']),
        '1970' : int(country_dic['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def get_population_continent(data, continent):
    percentages_list = list(filter(lambda item:item['Continent'] == continent, data))
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in percentages_list}

    labels = percentages_dict.keys()
    values = percentages_dict.values()
    return labels, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result           


# def population_by_continent(data, continent):
#     result = list(filter(lambda item: item['World Population Percentage'] == continent, data))
#     return result           

