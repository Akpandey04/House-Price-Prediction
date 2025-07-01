import pandas as pd
import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Load data and model
data = pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bathroom'))
    sqft = float(request.form.get('total_sqft'))

    # Column names must exactly match what model expects
    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])

    prediction = pipe.predict(input_df)[0] * 1e5
    return str(np.round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
