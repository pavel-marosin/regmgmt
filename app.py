
import os

import eventbrite, requests
from eventbrite import Eventbrite
from flask import Flask, render_template, request, current_app as app
import pusher


#hardcode constants for now put into .env file asap.


EVENTBRITE_EVENT_ID =   os.environ['EVENTBRITE_EVENT_ID']
EVENTBRITE_OAUTH_TOKEN= os.environ['EVENTBRITE_OAUTH_TOKEN']
PUSHER_APP_ID = os.environ['PUSHER_APP_ID']
PUSHER_KEY = os.environ['PUSHER_KEY']
PUSHER_SECRET = os.environ['PUSHER_SECRET']

# instantiate the eventbrite api client

class MyEventbrite(Eventbrite):
    # def get_event_attendees(self, event_id, status=None,
    #                         changed_since=None, page=1):
    #     """
    #     should paginated response with a key of attendees, containing a
    #     list of attendee.
    #
    #     GET /events/:id/attendees/
    #     """
    #     data = {}
    #     if status:  # TODO - check the types of valid status
    #         data['status'] = status
    #     if changed_since:
    #         data['changed_since'] = changed_since
    #     data['page'] = page
    #     return self.get("/events/{0}/attendees/".format(event_id), data=data)


    def get_page(self, pn):  # pn is page number
        pn = str(pn)
        response = requests.get(
            "https://www.eventbriteapi.com/v3/events/" + EVENTBRITE_EVENT_ID + "/attendees/?page=" + pn + "&token=" + EVENTBRITE_OAUTH_TOKEN,
            verify=True,
        )
        return response.json()

    def get_all_event_attendees(self, event_id, status=None,
                                changed_since=None):
        """
        Returns a full list of attendees.
        TODO: figure out how to use the 'continuation' field properly
        """
        page = 1
        attendees = []
        while True:
            r = self.get_page(page)
            attendees.extend(r['attendees'])
            if r['pagination']['page_count'] <= page:
                break
            page += 1
        return attendees


eventbrite = eventbrite.Eventbrite(EVENTBRITE_OAUTH_TOKEN)

test = MyEventbrite(eventbrite)

# Instantiate the pusher object. Uused to push actions to the browser when they occur.
p = pusher.Pusher(app_id=PUSHER_APP_ID, key=PUSHER_KEY, secret=PUSHER_SECRET)

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
     #Initial view
    # Get the event details
    event = eventbrite.get_event(EVENTBRITE_EVENT_ID)

    # Get the attendee list
    attendees = eventbrite.get_event_attendees(EVENTBRITE_EVENT_ID)
    attendees2 = test.get_all_event_attendees(EVENTBRITE_EVENT_ID)

    # Reverse so latest to sign up is at the top
    attendees['attendees'].reverse()
    #attendees2['attendees'].reverse()

    # Render our HTML.
    return render_template(
        'index.html',
        settings={'PUSHER_KEY': PUSHER_KEY},
        event=event,
        attendees=attendees2
    )

@app.route('/webhook', methods=['POST'])
def webhook():


    # Use the API client to convert from a webhook to an API object.
    api_object = eventbrite.webhook_to_object(request)

    # Use pusher to add content to to the HTML page.
    p.trigger(u'webhooks', u'Attendee', api_object)
    return ""




def reboot(self):
    def decorator(f):
        import re
        import commands
        s = commands.getoutput('lsof -i :5000')
        try:
            p_id = re.findall('.*?Python\s+[0-9]{4,7}', s)[0].split(' ')[-1]
        except IndexError:
            p_id = None
        p_id = int(p_id) if p_id else None
        if p_id:
            commands.getoutput('kill -9 {}'.format(p_id))
        return f
    return decorator



if __name__ == '__main__':
        app.run()






####################################################################################################v







# from flask import Flask, request, abort
# from eventbrite import Eventbrite
# import requests, json
#
#
# app = Flask(__name__)
#
#
# eventbrite = Eventbrite('xyz123')
# user = eventbrite.get_user()
# print user['name']
#
#
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
# 	jData = request.json
# 	# print jData
# 	# for key in jData:
# 	# 	print key + " : " + jData[key]
#
# 	# api_object = eventbrite.webhook_to_object(request)
#     #
# 	# print(api_object.type)
#     #
# 	# if api_object.type == 'User':
# 	# 	print('user event occured')
#     #
# 	# if api_object.type == 'Event':
# 	# 	print('event request occured')
#
# 	return ''
#
#
# @app.route('/responsedetail', methods=['GET'])
# def responsedetails(api_url):
# 	response = requests.get(api_url)
# 	jData = json.loads(response.content)
# 	for key in jData:
# 		 print key + " : " + jData[key]
#
#
#
# if __name__ == '__main__':
#     app.run()
