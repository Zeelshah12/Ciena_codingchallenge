# Ciena_CodingChallenge

A single page web app in a Python framework(Flask) has been created to simulate the behaviour of its connection to virtual cloud OSA. For front end development, HTML/JavaScript is used. The web app has 3 basic controls- START, STOP AND SINGLE to retrieve an OSA trace and display the result on a graph as per the instructions given in the challenge.

The app is successfully deployed on heroku platform. You can visit the web page at : https://zeelosaflaskapp.herokuapp.com/


## Installation Guidelines

You need to install all the requirements specified in requirements.txt file with the help of "pip install command". You need Python3 for running this web app on your system. You can install requirements by using "pip install -r requirements.txt" command. Or, you can use the following commands seperately:-
* pip install flask
* pip install requests
* pip install plotly 

After installing all the necessary requirements, change the main function of app.py as app.run(port='5000'). This is for running the application on your localhost on port number 5000. Run app.py file from your editor and it will start a development server. You can redirect to http://127.0.0.1:5000/ or http://localhost:5000/. 

## Features

* START button will start the acquisition rate and you can see the multiple graphs rendered on the web page.
* STOP button will stop the acquisition rate and message "Machine state has stopped" will be displayed on the web page.
* SINGLE retrieves a single trace from the virtual OSA and graph will be displayed.
* Input field for query commands is present on the web page, the "GO" button will submit the query to the server and results will be displayed.
* User can send query via REST end point 
- https://zeelosaflaskapp.herokuapp.com/echo/STRING - Will return string
- https://zeelosaflaskapp.herokuapp.com/PING  - Will return PONG
- https://zeelosaflaskapp.herokuapp.com/IDN - Will return the results of IDN
- https://zeelosaflaskapp.herokuapp.com/LIM - Will return the limits 
- https://zeelosaflaskapp.herokuapp.com/state - Will return the machine state
- https://zeelosaflaskapp.herokuapp.com/trace - Will return the json data of trace
 
 * Query input box will take commands from the user like echo/string, ping, state, lim and all these commands will display the results on the web page. If any command is wrongly entered by user, then Error message will be shown to the user.
 
## Bonus Functionalities Achieved

* The user has the ability to zoom, pan the plot and read data values off the plot.
* Plot persistence is done(successive plots are shown on start command).
* A scrollable text area with communication log between instrument & user (useful for debugging hardware issues in the laboratory) is   running perfectly.
* App is successfully deployed on Heroku : https://zeelosaflaskapp.herokuapp.com/









