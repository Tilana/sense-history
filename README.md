## sense-history

The goal of *sense-history* is to better understand how the city we live in was shaped over time.

It is a wearable device that signals historic landmarks. So, while going through your daily life you can get sense on how your city looked years ago, discover the history of its buildings and experience the dimension historic changes.

On my daily route to work, how often would I have to cross the former Berlin wall?
Which trees were already standing at their position 100 years ago? Where did people during the Second World War find shelter during military attacks? 



*sense-history* is a Raspberry Pi project. After setting up the you can select a module for your city (or add your own). Connected with a GPS tracker and a vibration motor it will give a signal as soon as you are close to point of interest.



### Modules

In general any geospatial data can be transformed into a module.
A module takes care that the geospatial data is interpreted correctly and squared with the current GPS location. 

Right now, It's possible to signal a vibration in two different use cases:

​	(1) when the current location is close enough to a point of interest in the data 
​		 e.g. when we are standing in a 2 meter radius of a tree older than 100 years

​	(2) when a specific line is crossed or predetermined areas are entered or left
​		 e.g. when crossing the Berlin wall from the east to the west sector (or the other way around)



In this repo three modules are included:

- The Berlin Wall
- Trees in Berlin
- Trees in Zurich


Finding adequate geospatial data can be a time-consuming and tedious process. If you have ideas for modules, tips for sources or even processed data, please reach out to me under **e-mail** or create a pull request.

### Setup

sense-history is a raspberry project. 

#### Raspberry Pi

#### Vibration Motor

#### GPS Module




### Installation

To get *shapely* running install libgeos with:

``` sudo apt-get install libgeos-dev ```

For other dependencies run:

``` sudo pip install -r requirements.txt ```




Setup raspberry to run script on with power connection:
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

On your Pi, edit the file /etc/rc.local using the editor of your choice. You must edit it with root permissions:

```
sudo vim /etc/rc.local
```

