# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:58:55 2020

@author: Zeel
"""

from flask import Flask, render_template, request
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import plotly
import logging
import plotly.graph_objs as go
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

output=""
url=""
result=""


@app.route('/', methods = ['GET'])
def index():
    global result
    result= result + 'Processing default request\n'
    return render_template('zoomindex.html', result=result)
    

class START:
    @app.route('/start', methods = ['POST','GET'])
    def start():
            global result
            result= result + 'Processing start request\n'
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
            return render_template('zoomindex.html', graphJSON=graphJSON, result=result)
        
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
            graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('zoomindex.html', graphJSON=graphJSON, result=result)        
    
class stop:
    @app.route('/stop', methods = ['POST'])
    def stop():
        global result
        result= result + 'Processing stop request\n'
       # response_start = requests.get("http://flaskosa.herokuapp.com/cmd/STOP")
        response = requests.get("http://flaskosa.herokuapp.com/cmd/STOP")
        stop_output="Machine state has stopped"
        return render_template("zoomindex.html",stop_output=stop_output, result=result)    
    

@app.route('/echo/<output>')
def get_query(output):   
    global result
    result= result + 'Processing echo request\n'
    return render_template("zoomindex.html",output=output,result=result) 

@app.route('/PING')
def ping():   
    global result
    result= result + 'Processing pong request\n'
    output="PONG"
    return render_template("zoomindex.html",output=output, result=result) 

@app.route('/IDN')
def idn():   
    global result
    result= result + 'Processing IDN request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/IDN")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

@app.route('/LIM')
def lim():   
    global result
    result= result + 'Processing limit request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/LIM")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

@app.route('/state')
def state():   
    global result
    result= result + 'Returning machine state\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/STATE")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 

@app.route('/trace')
def trace():   
    global result
    result= result + 'Processing trace request\n'
    response = requests.get("http://flaskosa.herokuapp.com/cmd/TRACE")
    response= response.content
    return render_template("zoomindex.html",output=response, result=result) 
 
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
    
    else:
    
        result= result + 'Error: Please check your query\n'
        output="Please check README file for correct commands"
        return render_template("zoomindex.html",output=output, result=result)
        
    
    
    
    
     
             
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
