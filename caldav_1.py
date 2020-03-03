
# coding: utf-8

# In[31]:

from datetime import datetime
import caldav
from caldav.elements import dav, cdav

# Caldav url
# url = "https://caldav.yandex.ru"
#url = 'https://caldav.yandex.ru/calendars/madhape@yandex.ru/events-default'
url = 'http://localhost:5232'

vcal = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VEVENT
UID:1234567890
DTSTAMP:20191228T180000Z
DTSTART:20191228T180000Z
DTEND:20191228T180000Z
SUMMARY:Запись к Тимуру на 21 час
END:VEVENT
END:VCALENDAR
"""

#client=caldav.DAVClient(url, username='madhape@yandex.ru', password='vtlbfyf12', ssl_verify_cert=False)  

client=caldav.DAVClient(url, username='any', password='any')


# In[33]:

principal = client.principal()


# In[34]:

calendars = principal.calendars()


# In[35]:

if len(calendars) > 0:
    calendar = calendars[0]
    print ("Using calendar", calendar)

    print ("Renaming")
    calendar.set_properties([dav.DisplayName("Test calendar"),])
    print (calendar.get_properties([dav.DisplayName(),]))

    event = calendar.add_event(vcal)
    print ("Event", event, "created")

    print ("Ищу события в 2019 году")
    results = calendar.date_search(
        datetime(2019, 12, 1), datetime(2020,1, 1))

    for event in results:
        print ("Found", event)

