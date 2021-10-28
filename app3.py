from ntpath import join
from flask import Flask, flash, request, redirect, url_for, render_template
from flask.json import jsonify
import pandas as pd
import csv
from google.cloud import storage
import google.cloud.storage
import json
import os
import sys
import io 
from io import BytesIO
from datetime import date
app=Flask(__name__)
#Upload the file(csv) along with JSON structure
@app.route('/upload' , methods=["POST"])
def json():
    data=request.get_json()
    Org_ID=data['Org_ID']
    type=data['type']
    year=data['year']
    with open('Sales.csv','w',newline='') as f:
            thewriter=csv.writer(f)
            for k,v in data.items():
                thewriter.writerow([k,v])

    #Starting of GCP¶
    PATH=os.path.join(os.getcwd(),'resourcebusy-testing-9c296e198f25.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=PATH
    #Create a client object¶
    storage_client=storage.Client(PATH)
    #Pushing a file on GCP BUcket
    filename='Sales.csv'
    UPLOADFILE=os.path.join(os.getcwd(),filename)
    typ=date.today()
    g=typ.month
    month=["january","february","march","april","may","june","juily","august","september","october","november","december"]
    bucket=storage_client.get_bucket('resoucebusymanan_587')
    blob=bucket.blob(filename)
    blob.upload_from_filename(UPLOADFILE)
    storage_client=storage.Client.from_service_account_json("resourcebusy-testing-9c296e198f25.json")
    bucket=storage_client.get_bucket("resoucebusymanan_587")
    #Uploading the file(csv) in the required loaction in GCP bucket
    filename="%s/%s/%s/%s" % (data["Org_ID"],data["year"],month[g-1],"file-sales.csv")
    blob=bucket.blob(filename)
    with open('Sales.csv', 'rb') as f:
        blob.upload_from_file(f)
        print("upload complete")
    return jsonify({'Org_ID': Org_ID, 'type' : type, 'year' : year})



       
    


