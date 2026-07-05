from flask import Flask, request,render_template
app=Flask(__name__)
import joblib

model=joblib.load('salary_model.pkl')
@app.route('/',methods=['GET','POST'])
def home():
    ans=None
    if(request.method=='POST'):
        experience=float(request.form['experience'])
        salary=model.predict([[experience]])[0]
        ans=round(salary,2)

    return render_template('index.html', ans=ans)




if __name__=="__main__":
    app.run(debug=True,port=5001)