from flask import Blueprint, request, jsonify, make_response
import json
from src import db


authenticators = Blueprint('authenticators', __name__)

# get the orders for an authenticator
@authenticators.route('/<id>/orders')
def get_orders(id):
    cursor = db.get_db().cursor()
    query = '''
    SELECT orderId, amountPaid, completed, dateShipped, Orders.quantity, buyerId, Orders.sellerId, authenticatorId, Orders.listingId, isAuthenticated, title
    FROM Orders JOIN Listings ON Listings.listingID = Orders.listingID
    WHERE Orders.authenticatorId={0};
    '''.format(id)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the all of the specifics of an order
@authenticators.route('/order/<orderID>/details')
def get_order_details(orderID):
    cursor = db.get_db().cursor()
    query = '''
    select amountPaid, completed, dateShipped, quantity, isAuthenticated, t2.listingID, t2.name, t2.title, t2.description,
    Buyers.firstName as buyerfirst, Buyers.lastName as buyerlast, Buyers.email as buyeremail, Buyers.phone as buyerphone,
    Buyers.street as buyerstreet, Buyers.city as buyercity, Buyers.state as buyerstate, Buyers.zip as buyerzip,
    Sellers.firstName as sellerfirst, Sellers.lastName as sellerlast, Sellers.email as selleremail, Sellers.phone as sellerphone,
    Sellers.street as sellerstreet, Sellers.city as sellercity, Sellers.state as sellerstate, Sellers.zip as sellerzip from
    Orders O join
    (select listingID, name, title, description from Listings L join Products P on L.productId=P.productId) t2 on O.listingID=t2.listingID
    join Buyers on Buyers.buyerId = O.buyerID
    join Sellers on Sellers.sellerId = O.sellerID
    where O.orderId = {0}
    '''.format(orderID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# authenticate an order
@authenticators.route('/order/<orderID>', methods=['PUT'])
def authenticate_order(orderID):
    cursor = db.get_db().cursor()
    query = 'UPDATE Orders SET isAuthenticated = 1 WHERE orderId = {0};'.format(
        orderID)
    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# post an authenticator note
@authenticators.route('/listings/<listingID>/<authenticatorID>', methods=['POST'])
def post_note(listingID, authenticatorID):
    req_data = request.get_json()

    cursor = db.get_db().cursor()
    content = req_data['noteComment']

    query = 'INSERT INTO AuthenticatorListingNotes (noteComment, listingId, authenticatorId) VALUES ("'
    query += content + '", ' + listingID + ', ' + authenticatorID + ')'

    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# update an authenticator note
@authenticators.route('/notes/<noteID>', methods=['PUT'])
def update_note(noteID):
    req_data = request.get_json()

    cursor = db.get_db().cursor()
    content = req_data['noteComment']

    query = 'UPDATE AuthenticatorListingNotes SET noteComment="{0}" WHERE noteID = {1};'.format(
        content, noteID)

    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# delete an authenticator note
@authenticators.route('/notes/<noteID>', methods=['DELETE'])
def delete_note(noteID):
    cursor = db.get_db().cursor()

    query = 'DELETE FROM AuthenticatorListingNotes where noteID={0};'.format(
        noteID)

    cursor.execute(query)
    db.get_db().commit()
    return "Success"

# get all notes
@authenticators.route('/notes', methods=['GET'])
def get_AuthenticatorListingNotes():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM AuthenticatorListingNotes
    '''
    cursor.execute(query)
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers.
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
