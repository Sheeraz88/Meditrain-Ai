from flask import Flask, render_template, request, jsonify
from Meditrain import getSeverityDict, getDescription, getprecautionDict, sec_predict, tree_to_code,precautionDictionary
from Meditrain import clf,cols
app = Flask(__name__)


getSeverityDict()
getDescription()
getprecautionDict()

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint to analyze symptoms and provide predictions."""
    data = request.json
    symptoms = data.get('symptoms', [])
    days = data.get('days', 1)
    
    if not symptoms:
        return jsonify({'error': 'No symptoms provided.'}), 400
    
    prediction = sec_predict(symptoms)
    response = {
        'prediction': prediction.tolist(),  # Convert numpy array to list
        'message': f"Based on your symptoms, you may have {prediction[0]}."
    }
    return jsonify(response)

@app.route('/get_response', methods=['POST'])
def get_response():
    """Endpoint to get precautions for a specific condition."""
    data = request.json
    disease = data.get('user_input')
    
    if not disease:
        return jsonify({'error': 'No disease specified.'}), 400
    
    precautions = precautionDictionary.get(disease, [])
    response = {
        'disease': disease,
        'precautions': precautions
    }
    return jsonify(response)

@app.route('/tree-analysis', methods=['POST'])
def tree_analysis():
    """Endpoint for detailed decision tree analysis."""
    data = request.json
    symptoms = data.get('symptoms', [])
    
    if not symptoms:
        return jsonify({'error': 'No symptoms provided for analysis.'}), 400
    
   
    analysis = tree_to_code(clf, cols)  
    return jsonify({'analysis': analysis})

if __name__ == '__main__':
    app.run(debug=True)
