from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools
from flask import Flask, request, jsonify
import urllib.request, json
import dateutil.parser
import os


app = Flask(__name__)
port = 5000

#opening json file and loading the content inside through the data variable we just created
with urllib.request.urlopen("https://www.sap.com/bin/sapdx/solrsearch?json={%22pagePath%22%3A%22%2Fcontent%2Fsapdx%2Fwebsite%2Fnam%2Fusa%2Fen_us%2Fabout%2Fevents%2Ffinder%22%2C%22pageCount%22%3A20%2C%22page%22%3A1%2C%22searchText%22%3A%22%22%2C%22sortName%22%3A%22startDate%22%2C%22sortType%22%3A%22asc%22%2C%22componentPath%22%3A%22%2Fcontent%2Fsapdx%2Fwebsite%2Fnam%2Fusa%2Fen_us%2Fabout%2Fevents%2Ffinder%2Fjcr%3Acontent%2Fpar%2FfinderContainer%22%2C%22search%22%3A[]}&additionalProcess=false&showEmptyTags=false%22%3A%5B%7B%22tags%22%3A%5B%22region_and_country%3A130362398448344139069223%2F18398822489182182997166") as url:
    data = json.loads(url.read().decode())


try:
    import argparse
    #basically we instantiate an object "flags" to hold our arguements and call function parse_args
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

#------------------------------------------------------- Google Calendar stuff--------------------------------------------------------------------------------------

#storage object stores and retrieves credentials from the sotrage.json
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()


#checks for credentials from the file client_secrets.json
if not creds or creds.invalid:
    #creates flow object from client_secret.json file . This file has client ID and secret. client is imported
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    #creds object holds information about the token that authorize  access to user's data
    #run_flow function's flow arguement attempts to open athorization page in the browser
    #once user grants access it stores new credentials into the storage.json file through store object
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)

#applying necessary credential headers to all the http requests by using authroze() function of the credentials object that we created above.
#once the object has been authorized it is passed inside the build function
CAL = build('calendar', 'v3', http=creds.authorize(Http()))


def AddItToCal(event_num):
    event_title = data['results'][event_num]['title']
    event_Startdate = data['results'][event_num]['catchAll'][4]
    event_Enddate = data['results'][event_num]['catchAll'][6]
    event_City = data['results'][event_num]['eventCity']
    event = {}

    event.update({"summary": event_title})
    event.update({"location": event_City})

    event.update({"start": {
        "dateTime": event_Startdate
    }})
    event.update({"end": {
        "dateTime": event_Enddate
    }})

    event.update({"attendees": [{"email": "purav2908@gmail.com"}]})
    return event
#---------------------------------------------------------------------- all the code for showing content on recast.ai--------------------------------------------------------------------------

@app.route('/', methods=['POST'])
def index():

#lists to add data from the json file
    summary = []
    start = []
    end = []
    url = []
#for loop that iterates over the json data and adds them to the lists we created above
    for event_info in data['results']:
            summaries= event_info['title']
            summary.append(summaries)

            event_start = event_info['startDate']
            start.append(event_start)

            event_end = event_info['endDate']
            end.append(event_end)

            public_url = event_info['publicUrl']
            actual_url = 'https://www.sap.com' + public_url + '.html'
            url.append(actual_url)



    start_date = []
    end_date = []
    for s in start:
        new_s_date = dateutil.parser.parse(s).strftime('%m/%d/%Y  %H:%M:%S')
        start_date.append(new_s_date)

    for e in end:
        new_e_date = dateutil.parser.parse(e).strftime('%m/%d/%Y  %H:%M:%S')
        end_date.append(new_e_date)

    return jsonify(
        status=200,
        replies=[{
            'type': 'carousel',
            'content': [
                {
                    'title': '1.  %s \n ' % (''.join(summary[0])),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[0]), ''.join(end[0])),
                    'buttons': [
                        {
                            'title':  'Book this event',
                            'type': 'BUTTON_1_TYPE',
                            'value': 'Book event 1',
                        },
                        {
                            'type': 'web_url',
                            'value': url[0],
                            'title': 'SAP Events page'
                        },
                    ]
                },
                {
                    'title': '2. %s ' % ''.join(summary[1]),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[1]), ''.join(end[1])),
                    'buttons': [
                        {
                            'title': ' Book this event ',
                            'type': 'BUTTON_1_TYPE',
                            'value': ' Book event 2',
                        },
                        {
                            'type': 'web_url',
                            'value': url[1],
                            'title': 'SAP Events page'
                        },
                    ]
                },
                {
                    'title': '3.  %s ' % ''.join(summary[2]),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[2]), ''.join(end[2])),
                    'buttons': [
                        {
                            'title': ' Book this event ',
                            'type': 'BUTTON_1_TYPE',
                            'value': ' Book event 3',
                        },
                        {
                            'type': 'web_url',
                            'value': url[2],
                            'title': 'SAP Events page'
                        }
                    ]
                },
                {
                    'title': '4. %s ' % ''.join(summary[3]),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[3]), ''.join(end[3])),
                    'buttons': [
                        {
                            'title': ' Book this event ',
                            'type': 'BUTTON_1_TYPE',
                            'value': ' Book event 4',
                        },
                        {
                            'type': 'web_url',
                            'value': url[3],
                            'title': 'SAP Events page'
                        },
                    ]
                },
                {
                    'title': '5. %s ' % ''.join(summary[4]),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[4]), ''.join(end[4])),
                    'buttons': [
                        {
                            'title': ' Book this event ',
                            'type': 'BUTTON_1_TYPE',
                            'value': ' Book event 5',
                        },
                        {
                            'type': 'web_url',
                            'value': url[4],
                            'title': 'SAP Events page'
                        },
                    ]
                },
                {
                    'title': '6.  %s ' % ''.join(summary[5]),
                    'subtitle': ' Start :  %s  \n  End : %s' '\n ' % (''.join(start[5]), ''.join(end[5])),
                    'buttons': [
                        {
                            'title': ' Book this event ',
                            'type': 'BUTTON_5_TYPE',
                            'value': ' Book event 6',
                        },
                        {
                        'type': 'web_url',
                        'value': url[5],
                        'title': 'SAP Events page'
                        },

                    ]
                }
            ],
        }]
    )

#route request to get event numbers from the recast.ai
@app.route('/book-events', methods=['POST'])
def AddEvents():
    selected_event = json.loads(request.get_data())
    event_number = selected_event['nlp']['entities']['number'][0]['scalar']
    add_first_event = CAL.events().insert(calendarId='primary',
                                              sendNotifications=True, body=AddItToCal(event_number-1)).execute()
    return jsonify(status=200)

#this function prints out errors in the console
@app.route('/errors', methods=['POST'])
def errors():
    print(json.loads(request.get_data()))
    return jsonify(status=200)

#runs on the port
app.run(port=port)
