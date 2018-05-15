# SAPEventsBot

Chatbots can play very important role in your organization. Operational tasks like adding an event to your calendar can and should be automated. This technology is being used my small and big companies to make scheduling an event easy and less time-consuming process. Time is the one thing that is holding individuals and companies from accomplishing more, so why not simplify the process and accomplish more in limited amount of time. SAP events assistant provides the ability to look up upcoming SAP events and add them to your calendar with necessary information just with a click. Users can interact with SAP events assistant on Slack and Facebook messenger.

SAP events assistant is built using recast.ai, currently acquired by SAP. SAP events assistant takes user’s input through text on one of the public messaging platform either slack or on messenger. Then it sends that that input to recast.ai’s Bot Connector tool. Bot Connector is a standardized messaging API, which supports text, images, buttons and other rich messaging features from different channels. Bot Connector breaks your input down into natural language processing and determines what the intent of your message is. Then Bot Connector figures out what the intent is, it makes calls to external data source, which in this case is SAP events page and shows all that events data into the chat box. Once it shows all the data in carrousels in the chatbot, it waits for the user to click on one of the events to add it to their calendar. Thereafter, Google API functionality comes into play and takes care of rest of the process and adds selected event to user’s calendar at specified date, time and location (if available). Event can be wither single event or recurring event. An event is represented by an event resource.

![chatbot](https://user-images.githubusercontent.com/24690198/40073667-7e64f16c-5845-11e8-8472-6ea826bd6951.png)

Demo Video: https://drive.google.com/open?id=1EykfqKUP3gqQeWYKKahJtSmk9YdXDWBo

# To chat with this bot:

    1. 
