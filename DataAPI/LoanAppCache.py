from flask import Flask, request, jsonify
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize dictionary cache
cache = {}

@app.route('/test', methods=['GET'])
def test():
    return "LoanAppCache.py successfully launched and services working"

@app.route('/keys', methods=['GET'])
def keys():
    keys_list = list(cache.keys())
    return jsonify(keys_list), 200

# Endpoint to store data in our dictionary cache
@app.route('/store', methods=['POST'])
def store():
    months = request.args.get('months')
    amount = request.args.get('amount')
    apr = request.args.get('apr')
    key = f"{months}_{amount}_{apr}"
    json_data = request.json
    cache_data = json.dumps(json_data)
    cache.update({key: cache_data})
    return jsonify({'message': 'Data stored successfully'}), 200

# Endpoint to retrieve data from memcached
@app.route('/retrieve', methods=['GET'])
def retrieve():
    print("LoanAppCache::retrieve")
    months = request.args.get('months')
    amount = request.args.get('amount')
    apr = request.args.get('apr')
    key = f"{months}_{amount}_{apr}"
    data = cache.get(key)
    if data:
        return jsonify(json.loads(data)), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
