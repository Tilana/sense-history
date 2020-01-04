## sense-history

### Run

Run Module:
``` ./run start ```

Run lint and tests:
``` ./run test ```

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


Add commands to execute the python program, preferably using absolute referencing of the file location (complete file path are preferred).
Be sure to leave the line exit 0 at the end, then save the file and exit. In nano, to exit, type Ctrl-x, and then Y.
