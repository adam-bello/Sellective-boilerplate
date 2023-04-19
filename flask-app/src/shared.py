from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the
# blueprint object, not the app object.
shared = Blueprint('shared', __name__)

# get all listings


@shared.route('/listings')
def get_listings():
    cursor = db.get_db().cursor()
    query = '''
        SELECT listingId, title, description, quantity, price, timeListed
        FROM Listings
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

# get the details of a listing


@shared.route('/listings/<listingID>')
def get_listing_details(listingID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT description, name
        FROM Listings JOIN Products ON Listings.productId = Products.productId
        WHERE listingId = {0}
    '''.format(listingID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the reviews for a listing


@shared.route('/listings/<listingID>/reviews')
def get_reviews(listingID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT reviewId, likes, dislikes, reviewComment, timePosted
        FROM ListingReviews
        WHERE listingId = {0}
    '''.format(listingID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the responses for a listing review


@shared.route('/listingreviews/<reviewID>/responses')
def get_review_responses(reviewID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT timePosted, responseComment
        FROM ListingReviewResponses
        WHERE reviewId = {0}
    '''.format(reviewID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the authenticator notes for a review


@shared.route('/listings/<listingID>/notes')
def get_listing_notes(listingID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT timePosted, noteComment
        FROM AuthenticatorListingNotes
        WHERE listingId = {0}
    '''.format(listingID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the reviews for a seller


@shared.route('/sellers/<sellerID>/reviews')
def get_seller_reviews(sellerID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT reviewId, likes, dislikes, reviewComment, timePosted
        FROM SellerReviews
        WHERE SellerId = {0}
    '''.format(sellerID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the responses for a seller review


@shared.route('/sellerreviews/<reviewID>/responses')
def get_sellerreview_responses(reviewID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT timePosted, responseComment
        FROM SellerReviewResponses
        WHERE reviewId = {0}
    '''.format(reviewID)
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get all products


@shared.route('/products')
def get_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT DISTINCT name AS label, productId AS value
        FROM Products
        ORDER BY productId
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

# get all sellers


@shared.route('/sellers')
def get_sellers():
    cursor = db.get_db().cursor()
    query = '''
        SELECT DISTINCT sellerId AS label, sellerId AS value
        FROM Sellers
        ORDER BY sellerId
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
