import sys
from argparse import ArgumentParser
import requests
import json

def get_holidays():
    country_code = ("A2")
    year = ("2010")
    url = "https://date.nager.at/Api/v1/Get/COUNTRYCODE/YEAR" + url
    data = requests.get(url, year=year, country_code=country_code).json()
    return data['country_code', 'year']

def parse_args(parser):
    parser = ArgumentParser()
    parser.add_argument("file", url="https://date.nager.at/Api/v1/Get/COUNTRYCODE/YEAR")
    return parser.parse_args(parser)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
    get_holidays = ("A2", "2010")


