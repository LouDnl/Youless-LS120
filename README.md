# WORK IN PROGRESS
This project is still in development.

# Youless-LS120

## Package
This package is for importing data from a YouLess LS120 datalogger that is connected to a smart electricity and gas meter.
The data is stored in an SQLite3 database and displayed on a dash webpage using pandas and plotly.
I created this package for stand-alone usage and not with a setup.py for installing.
While I oriented this on Dash it is ofcourse possible to use the data retrieved from the YouLess and the plotly figures created in any other webpage.

## Functions:
 - Dash text is available in Dutch and English (set in settings.py)
 - Realtime view with about 2 minutes history, updates every 5 seconds (not stored in database)
 - Live view per minute up to 10 hours history, updates every minute (not stored in database)
 - Import and process Energy (Electricity and Gas) data from Youless LS120 into SQLite3 database 
	- All data is stored as text and converted when read from the database
	- *Appends and overwrites data if needed*
 - Read data back from SQLite3 database
 - Convert read data to list based on wanted items
 - Convert list to Pandas DataFrame based on wanted items
 - Create dash based website with graphs

## requirements.txt
 - Contains all needed libraries/modules
 - Install them with: python -m pip install -r requirements.txt

## Usage:
 - Run either example files to get an idea of what is possible. \
 Otherwise see the description under the Package files
 - 

## Example files:
- liveview_allgraphs.py starts a flask webserver that displays all available graphs
	- updates the database on start and while active
	- plots live, daily, monthly and yearly Electricity and GAS usage
- test_view.py starts a flask webserver that displays the graphs set in that same file under the callback and multi_output function
	- this file is for testing purposes
	- webpage is hosted on ip that is set in settings.py and based on debug setting
- **The webpage is started on the local_ip or external_ip from settings.py**
	- if DASH_DEBUG in settings.py is set to True the webserver will be hosted on local_ip, \
	if set to False the webserver will be hosted on remote_ip

 ## Package files:
 - settings.py contains user changeable settings like IP, path and language
 - constants.py contains all constant variables etc for the package.
 - create_database.py creates youless.db if needed or appends tables if needed
 - import_data.py reads static data from Youless LS120 and writes it to the database
 - read_data.py reads data from the database and returns lists with data
 - plot_data.py converts lists with data and returns plotly figures 
 - read_live.py reads live data fro the Youless LS120 and returns lists with data
 - plot_live.py converts lists with live data and returns plotly figures
 - web_elements.py contains pre defined settings for both view files
 - __init__.py makes package modules available and starts the logger
 - logger_config.yaml contains the logger settings.\
 by default the logger level is set to DEBUG under root. Set this to WARNING to disable most logging.

## To Do:
 - **Add explanatory usage per package file**
 - Create interactive Dash website with:
	- Separate webpage from plot script
	- Automatic view of available data
	- Buttons that click to available data
	- Custom graphs based on available data. e.g. average electricity usage on wednesdays
 - Add quick tutorial to create a linux service that always runs
	- Examples available in docs/startupscript.txt (No explanation yet)
 - Add extra notations for more clarity
 - Convert read database data to Pandas DataFrame directly
 - ~~Remove commented out code~~
 - ~~Add quick tutorial on how to install requirements.txt~~
 - ~~Live usage view~~
 - ~~Combine reused code to importable class methods~~
 - ~~Add GAS usage~~
 - ~~Check if existing data in database matches retrieved data from Youless, if so then do nothing, else append~~
 - ~~Create automatic readout from LS120~~
 - ~~Make webpage available on linux server~~
 
 
## Some example views
![Realtime view](docs/liverealtime.png)\
![Live per minute](docs/liveminutes10hrs.png)\
![Day overview](docs/day.png)\
![Month overview](docs/month.png)\
![Year per day overview](docs/yeardays.png)\
![Year per month overview](docs/yearmonths.png)
