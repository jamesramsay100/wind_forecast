import requests
import json
from datetime import datetime
import numpy as np
import time
import pymongo


def get_latest():

    while True:
        ts = datetime.now().timestamp()
        ts = int(np.floor(ts/10))*10 - 10  # to nearest 10 seconds, take off 10 secs to avoid url not being ready

        bounds = '-0.9,50.7,-0.8,50.8'  # these are for Bracklesham
        url = 'http://enaktingweb.ecs.soton.ac.uk/weather/latest.php?timestamp=' + str(ts) + '&coords=' + bounds
        response = requests.get(url)
        try:
            data = response.json()['data'][0]
            print(data, flush=True)
            mycol.insert_one(data)
            print('Inserted data', flush=True)
        except:
            print('Data not ready on that attempt', flush=True)

        time.sleep(30)


if __name__ == '__main__':
    # set up database
    client = pymongo.MongoClient("mongodb://mongodb:27017")  # second 'mongodb' refers to container name
    mydb = client['wind_data_db']  # the database
    mycol = mydb["brackelsham"]  # collection is the same as table

    get_latest()
