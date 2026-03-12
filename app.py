from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
	# TODO: Return a welcome message

	return jsonify({"message": "Welcome to the product page API!"}), 200

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
	# TODO: Return all products or filter by ?category=

	category = request.args.get("category")
	if category:
		filtered = [item for item in products if item["category"] == category]
		return jsonify(filtered), 200
	# return jsonify({"message": "Products not found"}), 400
	return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
	# TODO: Return product by ID or 404

	for p in products:
		if p["id"] == id:
			return jsonify(p), 200
	return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
	app.run(debug=True)
