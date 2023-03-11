import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model._base import _preprocess_data

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features) / 100]
    prediction = model.predict(final_features)

    output = round(prediction[0], 46)

    return render_template('index.html', prediction_text='Model perfomance is: {}'.format(output))


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=80)
    log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
