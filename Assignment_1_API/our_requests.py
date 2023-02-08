import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API']['KEY']
