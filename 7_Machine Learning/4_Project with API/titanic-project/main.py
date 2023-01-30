# imports
from flask import Flask, render_template, flash, request, jsonify, Markup
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64, os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# default values
DEFAULT_EMBARKED = 'Southampton'
DEFAULT_FARE = 33
DEFAULT_AGE = 30
DEFAULT_GENDER = 'Female'
DEFAULT_TITLE = 'Mrs.'
DEFAULT_CLASS = 'Second'
DEFAULT_CABIN = 'C'
DEFAULT_SIBSP = 0
DEFAULT_PARCH = 0
average_survival_rate = 0

# model
model = LogisticRegression()

app = Flask(__name__)

# on startup
@app.before_first_request
def startup():
    global average_survival_rate, model

    from numpy import genfromtxt
    titanic_array = genfromtxt('titanic2.csv', delimiter=',')

    average_survival_rate = (np.mean([ item[0] for item in titanic_array]) * 100)

    xtrain, xtest, ytrain, ytest = train_test_split([ item[1:] for item in titanic_array],
                                                    [ item[0] for item in titanic_array],
                                                    test_size=0.5,
                                                    random_state=100
                                                    )
    
    model.fit(xtrain, ytrain)


# routes
@app.route('/', methods=['POST','GET'])
def submit_new_profile():
    model_results = ''

    if request.method == 'POST':
        pass
    else:
        return render_template('index.html',
                model_results = '',
                model_plot = '',
                )
