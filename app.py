# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:00:00 2020

@author: Zeel
"""

from flask import Flask, render_template, request
import requests
import json
import plotly
import time
import plotly.graph_objs as go

app = Flask(__name__)


output=""
url=""
result=""

#HOME PAGE 
@app.route('/', methods = ['GET'])
def index():
    global result
    result=""
    result= result + 'Processing default request\n'
    return render_template('zoomindex.html', result=result)
   
#start function will be called while clicking on start button, multiple traces will be plotted    
class START:
  @app.route('/start', methods = ['POST','GET'])
   def start():
                global result
                result= result + 'Processing start request\n'
                response_start = requests.get("http://flaskosa.herokuapp.com/cmd/START")
                rs= response_start.content
                
                response = requests.get("http://flaskosa.herokuapp.com/cmd/TRACE")
                r= response.content
                data= json.loads(r)
        
                labels = []
                values = []    
                for i in range(len(data['xdata'])):
                    labels.append((0.000299792458)/data['xdata'][i])
                for j in range(len(data['ydata'])):
                    values.append(data['ydata'][j])
            
                xScale = labels
                yScale = values
         
            # Create a trace
                trace = go.Scatter(
                x = xScale,
                y = yScale)
         
                data = [trace]
                graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
                print(graphJSON)
                return render_template('zoomindex.html', stop_output=rs, graphJSON=graphJSON, result=result)

        
#single function will be called while clicking on single button 
class SINGLE:
    @app.route('/single', methods = ['POST','GET'])
    def single():
            global result
            result= result + 'Processing single request\n'
            response = requests.get("http://flaskosa.herokuapp.com/cmd/TRACE")
            r= response.content
            data= json.loads(r)
    
            labels = []
            values = []    
            for i in range(len(data['xdata'])):
                labels.append((0.000299792458)/data['xdata'][i])
            for j in range(len(data['ydata'])):
                values.append(data['ydata'][j])
        
            xScale = labels
            yScale = values
     
        # Create a trace
            trace = go.Scatter(
            x = xScale,
            y = yScale)
     
            data = [trace]
            graphJSON_single = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('zoomindex.html', graphJSON_single=graphJSON_single, result=result)        

#stop function will be called while clicking on stop button, and acquisition will be stopped         
class stop:
    @app.route('/stop', methods = ['POST'])
    def stop():
        global result
        result= result + 'Processing stop request\n'
       # response_start = requests.get("http://flaskosa.herokuapp.com/cmd/STOP")
        response = requests.get("http://flaskosa.herokuapp.com/cmd/STOP")
        stop_output="Machine state has stopped"
        return render_template("zoomindex.html",stop_output=stop_output, result=result)    
    
#Route for echo string
@app.route('/echo/<output>')
def get_query(output):   
    global result
    result= result + 'Processing echo request\n'
    return render_template("zoomindex.html",output=output,result=result) 

#Route for PING command
@app.route('/PING')
def ping():   
    global result
    result= result + 'Processing pong request\n'
    output="PONG"
    return render_template("zoomindex.html",output=output, result=result) 

#Route for IDN command
@app.route('/IDN')
def idn():   
    global result
    result= result + 'Processing IDN request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/IDN")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

#Route for Limits
@app.route('/LIM')
def lim():   
    global result
    result= result + 'Processing limit request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/LIM")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

#Route for knowing the machine state
@app.route('/state')
def state():   
    global result
    result= result + 'Returning machine state\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/STATE")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

#Route for trace
@app.route('/trace')
def trace():   
    global result
    result= result + 'Processing trace request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/TRACE")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 
 
#Route for different queries for user    
@app.route('/query', methods = ['POST'])
def query():
    # response_start = requests.get("http://flaskosa.herokuapp.com/cmd/STOP")
    q_response = request.form['query']
    if q_response[0:4].lower()=="echo":
        output=q_response[5:]
        global result
        result= result + 'Returning Echo string\n'
        return render_template("zoomindex.html",output=output, result=result) 
        
    elif(q_response.lower()=="ping"):
        output="PONG"
        result= result + 'Returning Ping results\n'
        return render_template("zoomindex.html",output=output, result=result) 
    
    elif(q_response.lower()=="state"):
        output="IDLE"
        result= result + 'Returning machine state\n'
        return render_template("zoomindex.html",output=output, result=result)
    
    elif(q_response.lower()=="lim"):
        response = requests.get("http://flaskosa.herokuapp.com/cmd/LIM")
        response= response.content
        result= result + 'Returning limits\n'
        return render_template("zoomindex.html",output=response, result=result)
    
    else:
    
        result= result + 'Error: Please check your query\n'
        output="Please check README file for correct commands"
        return render_template("zoomindex.html",output=output, result=result)
        
    
    
if __name__ == '__main__':
    app.run()
