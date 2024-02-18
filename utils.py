import pickle
import json
import numpy as np
import config
import warnings
warnings.filterwarnings("ignore", category=UserWarning)



def get_prediction(gender, age, hypertension, heart_disease, ever_married,
       residence_type, avg_glucose_level, bmi, work_type,
       smoking_status):
    
    
    with open("artifacts\stroke_rfmodel.pkl", 'rb') as f:
        model=pickle.load(f)

    # with open(config.std_scale ,'rb') as f:
    #     std_scale=pickle.load(f)

    with open(config.model_encode , 'r') as f:
        d=json.load(f)

    gender=d['gender'][gender]
    ever_married=d['ever_married'][ever_married]
    residence_type=d['residence_type'][residence_type]
    work_type=np.where(model.feature_names_in_ =='work_type_'+work_type)[0][0]
    smoking_status=np.where(model.feature_names_in_ == 'smoking_status_'+smoking_status)[0][0]


    test_array=np.zeros((1,model.n_features_in_))
    test_array[0,0]=gender
    test_array[0,1]=age
    test_array[0,2]=hypertension
    test_array[0,3]=heart_disease
    test_array[0,4]=ever_married
    test_array[0,5]=residence_type
    test_array[0,6]=avg_glucose_level
    test_array[0,7]=bmi
    test_array[0,work_type]=1
    test_array[0,smoking_status]=1

    # scale_array=std_scale.fit_transform(test_array)

    result=model.predict(test_array)[0]

    return result