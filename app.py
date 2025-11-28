from flask import Flask, request, jsonify
import joblib
import numpy as np
 
# Load model and scaler
model = joblib.load('pricing_model.pkl')
scaler = joblib.load('scaler.pkl')
 
app = Flask(__name__)   
@app.route('/')
def home():
    return jsonify({"message": "Bosch Pricing Optimization API is running!"})
 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        unit_price = float(data['unit_price'])
        comp1 = float(data['comp_1'])
        comp2 = float(data['comp_2'])
        comp3 = float(data['comp_3'])
        month = int(data.get('month', 6))  
        # Prepare features
        sample = np.array([[unit_price,
                            unit_price - comp1,
                            unit_price - comp2,
                            unit_price - comp3,
                            month]])
        sample_scaled = scaler.transform(sample)
        predicted_qty = model.predict(sample_scaled)[0]
        revenue = unit_price * predicted_qty
 
        return jsonify({
            "predicted_quantity": round(predicted_qty, 2),
            "estimated_revenue": round(revenue, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)