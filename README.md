# Generating real-time windspeed forecasts
Describes how this app works

### Useful links
**How To Set Up Flask with MongoDB and Docker:**
https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker

**MongoDB in a container:**
https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c

**MongoDB intro:**
https://realpython.com/introduction-to-mongodb-and-python/


## Docker commands
List docker container status: `sudo docker-compose ps`
Launch containers: `sudo docker-compose up`
Launch without logs: `sudo docker-compose up -d`
Rebuild image after changes: `sudo docker-compose build --no-cache data_loader`
Remove all docker containers: `sudo docker image prune -a`

### Getting json from ecs Soton
http://enaktingweb.ecs.soton.ac.uk/weather/latest.php?timestamp=1590329750&coords=-1.7,50.1,-0.1,51.8
'http://enaktingweb.ecs.soton.ac.uk/weather/latest.php?timestamp=' + timestamp + '&coords=' + getBounds().toBBoxString()
timestamp: "1590329750"
"-1.7,50.1,-0.1,51.8"
