import utils
import read_csv
import charts
import matplotlib.pyplot as plt
import pandas as pd


def run():
    df = pd.read_csv('data.csv')
    # df = df[df['Continent'] == 'South America']

    # countries = df['Country/Territory'].values
    # porcentages = df['World Popultaion Percentage'].values
 

    data = read_csv.read_csv('data.csv')
    countryName = input('Escribe tu pais => ')
    # result = utils.population_by_country(data, country)
    
    result = df[df['Country/Territory']  == countryName]
    # result = list(df.iloc[:1,5].values)
    if len(result) > 0:
        countrySel = result
        # labels, values = utils.get_population(country)
        labels = countrySel['Country/Territory'].values
        values = countrySel['World Population Percentage'].values
        charts.generate_bar_chat(countryName,labels, values)

    continent = input('Escribe tu continente => ')
    continentSel = df[df['Continent'] == continent]
    countriesLabels = continentSel['Country/Territory'].values
    porcentagesValues = continentSel['World Population Percentage'].values
    # labels, values = utils.get_population_continent(data, continent)
    # print(len(labels), len(values))
    if len(countriesLabels) > 0 and len(porcentagesValues) > 0 :
        fig, ax = plt.subplots()
        ax.pie(porcentagesValues, labels=countriesLabels)
        ax.axis('equal')
        # plt.show()
        plt.savefig('pie.png')
        plt.close()

if __name__ == '__main__':
    run()