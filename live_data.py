import requests
import json
from datetime import datetime
import numpy as np


def get_latest():
    ts = datetime.now().timestamp()
    ts = int(np.floor(ts/10))*10  # to nearest 10 seconds, as integer

    bounds = '-0.9,50.7,-0.8,50.8'  # these are for Bracklesham
    url = 'http://enaktingweb.ecs.soton.ac.uk/weather/latest.php?timestamp=' + str(ts) + '&coords=' + bounds
    response = requests.get(url)
    data = response.json()
    print(data)


if __name__ == '__main__':
    get_latest()
