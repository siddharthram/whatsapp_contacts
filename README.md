###A quick and dirty script to parse whatsapp DOM to extract contact info

this script expects the whatsapp data and extracts contact info out of it. It will likely break as WhatsApp changes its DOM

##Usage

First, get the info you need out of the DOM. Log into Whatsapp, and click on the group you want to extract contact info out of. 

Open the Web Inspector. In Chromium based browsers, this will be under view->Develop. on the mac you can access it via <cmd><opt><i>

Open the 'Group Info'. It will list all the participants. Scroll down to the end and click on 'more' till all the partipants are shown in the scroll view

Then, in the inspector, move over the elements till you see the group members highlighted. Right click, select 'Outer HTML'. Save it in a file.


Download wa.py, and have python installed. Run it like this

_>python wa.py <your filename>_


