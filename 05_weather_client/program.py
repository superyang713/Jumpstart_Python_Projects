import requests
import bs4
from collections import namedtuple


WeatherReport = namedtuple('WeatherReport',
                           'location temperature unit')


def main():
    print_header()
    zipcode = input('What zipcode do you want the weather for (94541)? ')
    report = get_weather_from_html(zipcode)
    print('The temperature in {} is {} {}'
          .format(report.location, report.temperature, report.unit))


def print_header():
    print('-' * 40)
    print('          Weather App')
    print('-' * 40)


def get_page(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    r = requests.get(url)
    return bs4.BeautifulSoup(r.text, 'html.parser')


def get_weather_from_html(zipcode):
    bs = get_page(zipcode)
    location = bs.find('h1').text.strip()
    temperature = bs.find(class_='wu-value wu-value-to').text.strip()
    unit = bs.find(class_='wu-label').text.strip()
    report = WeatherReport(location=location, temperature=temperature,
                           unit=unit)
    return report


if __name__ == '__main__':
    main()
