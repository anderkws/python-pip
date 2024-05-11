import utils
import read_csv
import charts
import matplotlib.pyplot as plt

def run():
    data = read_csv.read_csv('data.csv')
    country = input('Type your country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chat(country['Country/Territory'],labels, values)

    continent = input('Type your continent => ')
    labels, values = utils.get_population_continent(data, continent)
    # print(len(labels), len(values))
    if len(labels) > 0 and len(values) > 0 :
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels)
        ax.axis('equal')
        # plt.show()
        plt.savefig('pie.png')
        plt.close()

if __name__ == '__main__':
    run()