from flask import Flask, render_template, request
import numpy as np
import pickle


# Load the model from the file

app = Flask(__name__)

with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        # Retrieve input data from the form
        v1 = float(request.form.get('v1'))
        v2 = float(request.form.get('v2'))
        v3 = float(request.form.get('v3'))
        amount = float(request.form.get('amount'))
        
        
        # Prepare the input data as a NumPy array
        input_data = np.array([[v1, v2, v3, amount]])
        print(input_data)
        
        # Make a prediction
        prediction = model.predict(input_data)
        prediction = "Fraud" if prediction[0] == 1 else "Not Fraud"
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
