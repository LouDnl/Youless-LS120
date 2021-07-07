"""
Basic configuration holder objects.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys, os, datetime, time, locale
import warnings

class Runtime:
    DEBUG = False # enable/disable debug messages and enable/disable Dash-Flask debug mode
    LOG = True # enable/disable log messages
    DASHDEBUG = True # enable/disable local serving of dash webservices
    # SERVE = False # enable/disable local serving of dash webservices

    @staticmethod
    def td(request):
        # dt
        dt = datetime.datetime.today()

        if (request == 'dt'):
            return dt
        elif (request == 'current_date'):
            return ("{:4d}-{:02d}-{:02d}".format(dt.year,dt.month,dt.day))
        elif (request == 'current_time'):
            return ("{:02d}:{:02d}:{:02d}".format(dt.hour,dt.minute,dt.second))
        elif (request == 'today'):
            return ("{:4d},{:02d},{:02d}".format(dt.year,dt.month,dt.day))
        elif (request == 'yesterday'):
            return ("{:4d},{:02d},{:02d}".format(dt.year,dt.month,dt.day-1))
        elif (request == 'seconds'):
            return dt.second
        elif (request == 'day_now'):
            return dt.day
        elif (request == 'day_yesterday'):
            return dt.day-1
        elif (request == 'month_now'):
            return dt.month
        elif (request == 'last_month'):
            return dt.month-1
        elif (request == 'year_now'):
            return dt.year #% 100 # last two digits
        elif (request == 'last_year'):
            return dt.year-1 # last year
        elif (request == 'date_live'):
            return dt.strftime("%A %d %B %Y")
        elif (request == 'time_live'):
            return dt.strftime("%H:%M")
        elif (request == 'secs_live'):
            return dt.strftime("%H:%M:%S")        
        else:
            pass



class Vars:
    ## Static variables
    local_ip = '127.0.0.1'
    external_ip = '192.168.0.5'
    port = '80'
    path = "./" # static path, assumes db is in same folder as script
    dbname = "youless.db"
    # cssname = "plotly.css"

    ## Unused variables
    months = (range(1,13,1)) # url months
    weeks = (range(1,54,1))  # url weeks
    days = (range(1,32,1))   # url days
    hours = (range(1,25,1))  # url hours
    years = (range(2020, 2031, 1)) # years
    # lowMonths = (4,6,9,11)
    # highMonths = (1,3,5,7,8,10,12)
    # excMonth = 2
    livedict = {'timelst': [], 'wattlst': []} # dictionary for storing live data

    ## Configuration dictionary
    __conf = {
        "valuenaming": ('kWh', 'm3', 'watt', 'ltr'), # Tuple with fixed value naming 0, 1, 2, 3
        "energytypes": {
            "list": ("E", "G", "W"), # 0, 1, 2
            "E": "Electricity in watts or kilowatts (per hour)",
            "G": "Gas usage in liters or cubic meters",
            "W": "Water usage in liters or cubic meters"
        },
        "dbtables": { # Database table naming
            "E": ('yeardays_e', 'dayhours_e'),#, 'dayminutes_e'), # tuple 0, 1, 3
            "G": ('yeardays_g', 'dayhours_g')#, 'dayminutes_g'), # tuple 0, 1, 3
            # "S": ('yeardays_s', 'dayhours_s'), # tuple 0, 1
        },
        "queries": { # All used SQL queries
            "yeardays_e":
            """
                CREATE TABLE yeardays_e (

                    date TEXT NOT NULL PRIMARY KEY,
                    year TEXT NOT NULL,
                    month TEXT NOT NULL,
                    monthname TEXT NOT NULL,
                    kwh TEXT NOT NULL
                );
            """,
            "dayhours_e":
            """
                CREATE TABLE dayhours_e (
                    date TEXT NOT NULL PRIMARY KEY,
                    year TEXT NOT NULL,
                    week TEXT NOT NULL,
                    month TEXT NOT NULL,
                    monthname TEXT NOT NULL,
                    day TEXT NOT NULL,
                    yearday TEXT NOT NULL,
                    watt TEXT NOT NULL
                );
            """,
            "dayminutes_e":
            """
                "NON EXISTANT"
            """,
            "yeardays_g":
            """
                CREATE TABLE yeardays_g (

                    date TEXT NOT NULL PRIMARY KEY,
                    year TEXT NOT NULL,
                    month TEXT NOT NULL,
                    monthname TEXT NOT NULL,
                    m3 TEXT NOT NULL
                );
            """,
            "dayhours_g":
            """
                CREATE TABLE dayhours_g (
                    date TEXT NOT NULL PRIMARY KEY,
                    year TEXT NOT NULL,
                    week TEXT NOT NULL,
                    month TEXT NOT NULL,
                    monthname TEXT NOT NULL,
                    day TEXT NOT NULL,
                    yearday TEXT NOT NULL,
                    ltr TEXT NOT NULL
                );
            """,
            "dayminutes_g":
            """
                "NON EXISTANT"
            """,
            "i_dayhours":
            """
                INSERT OR REPLACE INTO %s (date,year,week,month,monthname,day,yearday,%s)
                VALUES(?,?,?,?,?,?,?,?)
            """,
            "i_yeardays":
            """
                INSERT OR REPLACE INTO %s (date,year,month,monthname,%s)
                VALUES(?,?,?,?,?)
            """,
            "s_table":
            """
                SELECT * FROM %s WHERE date=?
            """,
            "table_exist": # query credits: https://stackoverflow.com/posts/8827554/revisions
            """
                SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?
            """,
            "s_dayhours":
            """
                SELECT * FROM %s WHERE year = %s AND month = %s AND day = %s
            """,
            "s_dayhours2":
            """
                SELECT * FROM %s WHERE year = %s AND month = %s AND day IN (%s, %s)
            """,
            "s_yeardays":
            """
                SELECT * FROM %s WHERE year = %s AND month = %s
            """,
            "so_yeardays":
            """
                SELECT * FROM %s WHERE year = %s ORDER BY date
            """
        }
    }

    ## Youless webpage links, naming and css settings
    __web = {
        "LANG": "NL", # NL or EN only for now
        "LOCALE": "nl_NL.utf8", # Need to set this to nl_NL er en_US aswell
        # "LANG": "EN", # NL or EN only for now
        # "LOCALE": "en_US.utf8", # Need to set this to nl_NL er en_US aswell        
        "ENCODING": "utf-8",
        "HEADERS": { "Accept-Language": "en-US, en;q=0.5"},
        "URL": "http://192.168.0.40", # base url
        "ELE": "/V?", # url for electricity
        "GAS": "/W?", # url for gas
        "S0": "/Z?", # url for S0 bus
        "STATS": "/a?", # url for live statistics
        "JSON": "f=j&", # json link
        "M": "m=", # url represented in months (number) 1 to 12 and goes back 1 year, kWh for E and m3 for G
        "W": "d=", # url represented per day, history goes back 70 days, Watt for E and ltr for G
        "D": "h=", # url represented in 20 parts of half an hour (10 hours total) with usage per minute, counting back from the current moment (last entry of page 1). Watt for E
        "H": "w=",  # url represented in 30 parts of 8 hours (10 days total) per part in 47 representations (10 minutes), counting back from the current moment -10mins (last entry of page 1). Watt for E and ltr for G
        "maxDayPage": 70, # max for d=
        "minDayPage": 1, # min for d=
        "maxMonthPage": 12, # max for m=
        "minMonthPage": 1, # min for m=
        "maxMinutePage": 20, # max for h=
        "minMinutePage": 1, # min for h=
        "maxTenMinPage": 30, # max for w=
        "minTenMinPage": 1, # min for w=
        "maxHour": 24, # max hour in a day -1
        "minHour": 0, # min hour in a day
        "maxMinute": 29, # max minutes per part for h=
        "minMinute": 0, # min minutes per part for h=
        "minTen": 0, # min entry for w=
        "maxTen": 47, # max entry for w=
        "css": {
            "page_css": {'position': 'fixed', 'top': '0', 'left': '0', 'right': '0', 'bottom': '0', 'overflow': 'auto', 'width': '100%', 'height': '100%'},
            "row_title": {'text-align':'center', 'font-size': 'x-large', 'border': 'none', 'border-collapse': 'collapse', 'margin': '0px', 'padding': '0px'},
            "subrow_title": {'text-align':'center', 'font-size': 'large', 'border': 'none', 'border-collapse': 'collapse', 'margin': '0px', 'padding': '0px'},
            "table_css": {'margin': '0px', 'padding': '0px'},
            "column_css": {'border': 'none', 'border-collapse': 'collapse', 'margin': '0px', 'padding': '0px'}
        }
    }

    ## Languages. Tuple within a dictionary item. 0 == NL, 1 == EN
    __langDict = {
        "livegraphtitle": 
        (
            "Live verbruik: {} watt, {} {}uur<br>Meterstand: {} {}",
            "Live usage: {} watt, {} {} hours<br>Meter: {} {}",
        ),
        "liveminutegraphtitle": 
        (
            "Live verbruik per minuut: {} watt, {} {} uur",
            "Live usage per minute: {} watt, {} {} hour",
        ),
        "tenminutegraphtitle": 
        (
            "Verbruik per tien minuten:",
            "Usage per ten minutes:",
        ),
        "customhourtitle": (
            "%s %d t/m %d %d %s per uur, totaal verbruik: %g %s",
            "%s %d - %d %d %s per hour, total usage: %g %s",
        ),
        "dayhourtitle": 
        (
            "%s %d %d %s per uur, totaal verbruik: %g %s",
            "%s %d %d %s per hour, total usage: %g %s",
        ),
        "yearmonthtitle": 
        (
            "%s %d %s per dag, totaal verbruik: %g %s",
            "%s %d %s per day, total usage: %g %s",
        ),
        "yeardaytitle": 
        (
            "jaar %d %s per dag, totaal verbruik: %g %s",
            "year %d %s per day, total usage: %g %s",
        ),
        "yeartitle": 
        (
            "jaar %d %s per maand, totaal verbruik: %g %s",
            "year %d %s per month, total usage: %g %s",
        ),
        "ELE": 
        (
            "Elektriciteit verbruik",
            "Electricity usage",
        ),
        "GAS": 
        (
            "Gas verbruik",
            "Gas usage",
        ),
        "LIVE": 
        (
            "Live Informatie Elektriciteit",
            "Live Electricity Information",
        ),
        "TOYE": 
        (
            "Vandaag en gisteren",
            "Today and yesterday",
        ),
        "CMLM": 
        (
            "Deze maand en vorige maand",
            "This month and last month",
        ),
        "TYLYM": 
        (
            "Dit jaar en vorig jaar in maanden",
            "This year and last year in months",
        ),
        "TYLYD": 
        (
            "Dit jaar en vorig jaar in dagen",
            "This year and last year in days",
        ),
        "TOD": ("Vandaag", "Today"),
        "YDY": ("Gisteren", "Yesterday"),
        "TMO": ("Deze maand", "This month"),
        "LMO": ("Vorige maand", "Last month"),
        "TYE": ("Dit jaar", "This year"),
        "LYE": ("Vorig jaar", "Last year"),
        "D": ("Dag","Day",),
        "DT": ("Datum","Date",),
        "M": ("maand","month"),
        "T": ("Tijd","Time"),
        "U": ("Uur","Hour"),
        "KH": ("kiloWatt uur","kiloWatt hour"),
        "KWH": ("kWh","kWh"),
        "W": ("Watt","Watts"),
        "WH": ("Watt uur","Watts hour"),
        "KM": ("Kubieke Meter","Cubic meters"),
        "M3": ("m3","m3"),
        "L": ("Liter","Liter"),
    }
 
    @staticmethod
    def youlessLocale():
        """
            returns the locale setting
        """
        locale.setlocale(locale.LC_ALL, Vars.web("LOCALE"))
    
    @staticmethod
    def lang(text):
        """
            returns item from language dictionary
            usage:
            Vars.lang("keyname") returns the contents of the key
            return value is either english or dutch based on the setting in the __web dictionary under LANG.
        """
        if Vars.__web["LANG"] == "NL":
            return Vars.__langDict[text][0]
        elif Vars.__web["LANG"] == "EN":
            return Vars.__langDict[text][1]   

    @staticmethod
    def conf(name): # return items from config dictionary
        """
            returns item from the conf dictionary
            usage:
            Vars.conf("keyname") returns contents of the key
            For nested dictionaries use as followed:
            Vars.conf("keyname")["2nd_keyname"]["etc"]
        """
        return Vars.__conf[name]

    @staticmethod
    def web(name, *args): 
        """
            returns item from web dictionary, add second argument to return dictionary from key
            can be used either as Vars.web("keyname") and return its contents
            or as Vars.web("keyname", "secondkeyname") and returns the dictionary within the dictionary
            This will also work: Vars.web("keyname")["second_keyname"]["etc"]        
        """        
        if (args == ()):
            return Vars.__web[name]
        else:
            return Vars.__web[name].get(args[0]) # only the first extra argument will be processed, others will be ignored

# debug messages method
def dbg(s):
    """
        Usage:
        dbg(lambda: "TEXT")
        dbg(lambda: "TEXT and %s" % variable)
    """
    if Runtime.DEBUG:
        print("DEBUG: ", s())
        # print(s())

# log messages method
def log(s):
    """
        Usage:
        log(lambda: "TEXT")
        log(lambda: "TEXT and %s" % variable)
    """
    if Runtime.LOG:
        print(s())

# type defining
# def datatype(t):
#     types = {
#         "E": "Electricity",
#         "G": "Gas",
#         "W": "Water"
#     }
#     for k, v in types.items():
#         if t in v:
#             return(v)

def main():
    log(lambda: "I do not run on my own...")

if __name__ == '__main__':
        main()    