from flask import Flask, render_template, request, url_for
import pytorch 

app=Flask(__name__)
model=torch.load('diabetes.pt')
print('model is loaded')

@app.route('/', mrthod='GET')
def index():
    return render_template('index.html')

@app.route('/predic', method=['POST', 'GET'])
def predict():
    if request.method=='POST':
        Pregnancies=float(request.form['Pregnancies'])
        Glucose=float(request.form['Glucose'])
        BloodPressure=float(request.form['BloodPressure'])
        SkinThickness=float(request.form['SkinThickness'])
        Insulin=float(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
        Age=float(request.form['Age'])
        
        lst=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        pred=model.predict(lst)
        output=pred
        if output == 0:
            return "Don't worry, You don't have Diabetes"
        else:
            return "Sorry! You have Diabetes"
    # render_template('index.html', output=output)

if __name__=='__main__':
    app.run(debug=True)