# Py-html2png

Python module to take build a png image from an html file.
The module can be used client and server side. For server side, with no display the script will create a virtual display to make possible browser screenshot.


Use Case: 
I've created a Folium Map for my Telegram bot, but no ways to export it in png or jpeg format. Only possible trick was to take a screenshot of the html map, loaded into the browser. 


Required: 
- Python Modules: pyvirtualdisplay, selenium
- Firefox installed on computer and geckodriver in the same directory of the script

