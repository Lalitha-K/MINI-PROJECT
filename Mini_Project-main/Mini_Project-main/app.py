from flask import Flask,render_template,request
import joblib

app=Flask(__name__)
model=joblib.load("final_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/houseprice',methods=['POST'])
def feature():
    if request.method=='POST':
        li=[]

        Suburb=int(request.form['suburb'])
        Rooms=int(request.form['rooms'])
        Type=int(request.form['type'])
        Sale_Year=int(request.form['saleyear'])
        Distance=float(request.form['distance'])
        Bedroom=float(request.form['bedroom'])
        Bathroom=float(request.form['bathroom'])
        Car=float(request.form['car'])
        LandSize=float(request.form['landsize'])
        BuildingArea = float(request.form['buildingarea'])
        Year=float(request.form['year'])
        CouncilArea=int(request.form['council'])
        Regionname=int(request.form['region'])

        li=[Suburb,Rooms,Type,Sale_Year,Distance,Bedroom,Bathroom,Car,LandSize,BuildingArea,Year,CouncilArea,Regionname]

        Price=str(model.predict([li]))
    return render_template("houseprice.html",house_price=Price)





if __name__=='__main__':
    app.run(debug=True)

