import utils
import read_csv
import charts

def run():
  data = list(read_csv.read_csv('data.csv'))
  
  country = input('Type Country => ').title()
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country_data = result[0]
    print(country_data)
    labels, values = utils.get_population(country_data)
    charts.generate_bar_chart(country_data['Country'], labels, values)

  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  

if __name__ == '__main__':
  run()
