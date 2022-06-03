import json
import re
import sys
import time
from datetime import date
from datetime import datetime


def main():
    query = sys.argv[1]

    if query == 'now':
        timestamp = int(time.mktime(datetime.now().timetuple()))
    elif query == 'today':
        timestamp = int(time.mktime(date.today().timetuple()))
    elif re.match('^\d\d\d\d-\d+-\d+ \d+:\d+:\d+$', query):
        timestamp = int(time.mktime(datetime.strptime(query, '%Y-%m-%d %H:%M:%S').timetuple()))
    elif re.match('^\d\d\d\d-\d+-\d+$', query):
        timestamp = int(time.mktime(datetime.strptime(query, '%Y-%m-%d').timetuple()))
    elif re.match('^\d\d\d\d-\d+$', query):
        timestamp = int(time.mktime(datetime.strptime(query+'-01', '%Y-%m-%d').timetuple()))
    elif re.match('^\d+$', query):
        timestamp = int(query)
    else:
        return

    timestamp_str = str(timestamp)
    time_str = datetime.strftime(datetime.fromtimestamp(timestamp), '%Y-%m-%d %H:%M:%S')
    date_str = datetime.strftime(datetime.fromtimestamp(timestamp), '%Y-%m-%d')

    items = [
        {'title': timestamp_str, 'subtitle': 'seconds_since_epoch', 'arg': timestamp_str},
        {'title': time_str, 'subtitle': 'date and time in ' + str(time.tzname[0]), 'arg': time_str},
        {'title': date_str, 'subtitle': 'just date in ' + str(time.tzname[0]), 'arg': date_str}
    ]

    print(json.dumps({'items': items}))


if __name__ == '__main__':
    main()
