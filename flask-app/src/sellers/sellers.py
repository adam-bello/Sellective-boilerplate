from flask import Blueprint, request, jsonify, make_response
import json
from src import db


sellers = Blueprint('sellers', __name__)

# add a listing to the db
@sellers.route('/listings', methods=['POST'])
def post_listing():
    req_data = request.get_json()
    #title, description, quantity, price, sellerId, productId
    cursor = db.get_db().cursor()
    title = req_data['title']
    desc = req_data['description']
    quantity = req_data['quantity']
    price = req_data['price']
    sellerid = req_data['sellerId']
    productid = req_data['productId']
    query = 'INSERT INTO Listings (title, description, quantity, price, sellerId, productId) VALUES ("'
    query += title + '", "' + desc + '", ' + quantity + ', ' + price + ', ' + sellerid + ', ' + productid + ')'

    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# update a listing in the db
@sellers.route('/listings/<listingID>', methods=['PUT'])
def update_listing(listingID):
    req_data = request.get_json()
    cursor = db.get_db().cursor()

    title = req_data['title']
    desc = req_data['description']
    quantity = req_data['quantity']
    price = req_data['price']

    query = 'UPDATE Listings SET quantity={0}, price={1}, title="{2}", description="{3}" WHERE listingID = {4};'.format(quantity, price, title, desc, listingID)
    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# delete a listing in the db
@sellers.route('/listings/<listingID>', methods=['DELETE'])
def delete_listing(listingID):
    cursor = db.get_db().cursor()
    query = 'DELETE FROM Listings where listingID={0};'.format(listingID)
    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# create a response to a listing review
@sellers.route('/reviews/<reviewID>', methods=['POST'])
def post_listing_response(reviewID):
    req_data = request.get_json()
    cursor = db.get_db().cursor()
    response = req_data['responseComment']
    query = 'INSERT INTO ListingReviewResponses (responseComment, reviewID) VALUES ("'
    query += response + '", ' + reviewID + ')'
    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# create a response to a seller review
@sellers.route('/sellerreviews/<reviewID>', methods=['POST'])
def post_seller_response(reviewID):
    req_data = request.get_json()
    cursor = db.get_db().cursor()
    response = req_data['responseComment']
    query = 'INSERT INTO SellerReviewResponses (responseComment, reviewID) VALUES ("'
    query += response + '", ' + reviewID + ')'
    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# get the orders for a seller
@sellers.route('/<id>/orders')
def get_orders(id):
    cursor = db.get_db().cursor()
    query = '''
    SELECT orderId, amountPaid, completed, dateShipped, Orders.quantity, buyerId, Orders.sellerId, authenticatorId, Orders.listingId, isAuthenticated, title
    FROM Orders JOIN Listings ON Listings.listingID = Orders.listingID
    WHERE Orders.sellerId={0};
    '''.format(id)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)