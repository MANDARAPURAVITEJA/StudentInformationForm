from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
import os
import pymysql
import SQL_Operations as sql_obj

app = Flask(__name__)

# @app.route('/',methods=['GET'])  # route to display the home page
# @cross_origin()
# def homePage():
#     return render_template("home.html")

@app.route('/',methods=['POST','GET']) #
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            FIRST_NAME = request.form['FIRST_NAME']
            LAST_NAME = request.form['LAST_NAME']
            GENDER = request.form['GENDER']
            DOB = request.form['DOB']
            EMAIL = request.form['EMAIL']
            PHONE_NUMBER = request.form['PHONE_NUMBER']
            ADDRESS = request.form['ADDRESS']

            COURSE_HTML, COURSE_PYTHON, COURSE_JAVA = "", "", ""
            if request.form.get("COURSE_HTML")!=None:
                COURSE_HTML = "HTML"
            if request.form.get("COURSE_PYTHON")!=None:
                COURSE_PYTHON = "Python"
            if request.form.get("COURSE_JAVA")!=None:
                COURSE_JAVA = "Java"
                
            COURSE = str([COURSE_HTML,COURSE_PYTHON,COURSE_JAVA])
            ENROLLEMENT_YEAR = request.form['ENROLLEMENT_YEAR']
            IS_INTERNATIONAL = request.form['IS_INTERNATIONAL']

            student_info = sql_obj.Insert_Data(first_name=FIRST_NAME,
                                              last_name=LAST_NAME,
                                              gender=GENDER,
                                              dob=DOB,
                                              email=EMAIL,
                                              phone_number=PHONE_NUMBER,
                                              address=ADDRESS,
                                              course=COURSE,
                                              enrollement_year=ENROLLEMENT_YEAR,
                                              is_International=IS_INTERNATIONAL
                                        )
            context = "Student details Submitted Successfully"
            return render_template('index.html', context="Student details Submitted Successfully")

        except Exception as e:
            print('The Exception message is: ',e)
            context="Some issue with the code, details not saved. Contact IT Support"
            return render_template('index.html',context=context)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
