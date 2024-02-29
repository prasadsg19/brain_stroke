from flask import Flask, request, jsonify, render_template
from utils import get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form['gender']
    age = float(request.form['age'])
    hypertension = request.form['hypertension']
    heart_disease = request.form['heart_disease']
    ever_married = request.form['ever_married']
    residence_type = request.form['residence_type']
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    work_type = request.form['work_type']
    smoking_status = request.form['smoking_status']

    prediction = get_prediction(gender, age, hypertension, heart_disease, ever_married,
                                residence_type, avg_glucose_level, bmi, work_type,
                                smoking_status)
    
    final={0:'NO' ,1:'Yes' }

    return jsonify({'prediction': final[prediction]})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9090,debug=False)
