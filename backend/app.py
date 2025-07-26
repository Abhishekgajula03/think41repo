import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load datasets
products = pd.read_csv('data/products.csv')
orders = pd.read_csv('data/orders.csv')
inventory = pd.read_csv('data/inventory_items.csv')

@app.route('/query', methods=['POST'])
def handle_query():
    question = request.json['question']
    
    if "top 5 most sold products" in question:
        top_products = orders['product_id'].value_counts().head(5)
        return jsonify(top_products.to_dict())
    
    elif "status of order ID" in question:
        order_id = int(question.split()[-1])
        status = orders.loc[orders['order_id'] == order_id, 'status'].values[0]
        return jsonify({"status": status})
    
    elif "how many left in stock" in question:
        product_name = question.split('"')[1]  # Extract "Classic T-Shirt"
        stock = inventory[(inventory['product_name'] == product_name) & (inventory['sold_at'].isna())].shape[0]
        return jsonify({"stock": stock})
    
    else:
        return jsonify({"error": "Question not recognized"})

if __name__ == '__main__':
    app.run(debug=True)
