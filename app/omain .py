import utils
import read_csv
import mcharts

data =[
    {
    'Country' : 'Colombia',
    'Population' : 500
    },
    {
        'Country' : 'Bolivia',
        'Population' : 300
    }
]

def run():

    keys, values = utils.get_population()
    print(keys, values)
    country = input('Type your country => ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()