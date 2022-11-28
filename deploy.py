from flask import Flask, request,render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)
model=pickle.load(open("flight_rf.pkl","rb"))
@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("predict",methods=["GET","POST"])
@cross_origin()
def predict():
    if request.method()=="POST":
        date_dep=request.form["DEp_Time"]
        Journey_day=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").day)
        Journey_month=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").month)
        Dep_hour=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").hour)
        Dep_min=int(pd.to_dtaetime(date_dep,format="%Y-%m-%dT%H:%M").minute)
        datw_arr=request.form["Arrival_Time"]
        Arrival_hour=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").hour)
        Arrival_min=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").minute)
        dur_hour=abs(Arrival_hour-Dep_hour)
        dur_min=abs(Arrival_min-Dep_min)
        Total_stops=int(request.form["stops"])
        airline=request.form["airline"]
        if(airline=="Jet_Airways"):
            Jet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="IndiGo"):
            Jet_Airways=0
            IndiGo=1
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="Air_India"):
            Jet_Airways=0
            IndiGo=0
            Air_India=1
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0    
        elif (airline=="Multiple_Carriers"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=1
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="SpiceJet"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=1
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="Vistara"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=1
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0

        elif (airline=="GoAir"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=1
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="Multiple_Carriers_Premium_economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=1
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0    
        elif (airline=="Jet_Airways_Business"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=1
            Vistara_Premiuim_economy=0
            Truiet=0
        elif (airline=="Vistara_Premiuim_economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=1
            Truiet=0
        elif (airline=="Truiet"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=1
        else:
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_Carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_Carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premiuim_economy=0
            Truiet=0
        Source=request.form["Source"]
        if(Source=="Delhi"):
            s_Delhi=1
            s_Kolkate=0
            s_Mumbai=0
            s_Chennai=0
        elif(Source=="Kolkata"):
            s_Delhi=0
            s_Kolkate=1
            s_Mumbai=0
            s_Chennai=0
        elif(Source=="Mumbai"):
            s_Delhi=0
            s_Kolkate=0
            s_Mumbai=1
            s_Chennai=0
        elif(Source=="Chennai"):
            s_Delhi=0
            s_Kolkate=0
            s_Mumbai=0
            s_Chennai=1
        else:
            s_Delhi=0
            s_Kolkate=0
            s_Mumbai=0
            s_Chennai=0

        Source=request.form["Destination"]
        if(Source=="Cochin"):
            d_Cochin=1
            d_Delhi=0
            d_New_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0
        elif(Source=="Delhi"):
            d_Cochin=0
            d_Delhi=1
            d_New_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0 
        elif(Source=="New_Delhi"):
            d_Cochin=0
            d_Delhi=0
            d_New_Delhi=1
            d_Hyderabad=0
            d_Kolkata=0 
        elif(Source=="Hyderabad"):
            d_Cochin=0
            d_Delhi=0
            d_New_Delhi=0
            d_Hyderabad=1
            d_Kolkata=0 
        elif(Source=="Kolkata"):
            d_Cochin=0
            d_Delhi=0
            d_New_Delhi=0
            d_Hyderabad=0
            d_Kolkata=1
        else:
            d_Cochin=0
            d_Delhi=0
            d_New_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0