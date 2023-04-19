--# GET /listing
--#select title, quantity, price, timeListed from Listings;

--# POST /listing
--INSERT INTO Listings (title, description, quantity, price, sellerId, productId)
--VALUES (1, 0, 0, 'I love pikachu cards', 1, 1);

--# GET /listing/{listingId}
--select description from Listings where listingID=1;
--select * from Listings join Products P on Listings.productId = P.productId where listingID=1;
--select * from ListingReviews where listingId=1;
--select * from ListingReviewResponses join ListingReviews on ListingReviewResponses.reviewID = ListingReviews.reviewId where ListingReviews.--listingId=1;
--select * from AuthenticatorListingNotes where listingId=1;

--# PUT /listing/{listingId}
--UPDATE Listings SET quantity=1, price=2.22, title='newTitle', description='new description' WHERE listingID=1;
--select * from Listings;

--# DELETE /listing/{listingId}
--DELETE FROM Listings where listingID=1;

--# GET /listing/{listingId}/review/{reviewId}
--select likes, dislikes, reviewComment from ListingReviews where listingId=1 and reviewId=1;

--# POST /listing/{listingId}/review/{reviewId}/response
--INSERT INTO ListingReviewResponses (responseComment, reviewID)
--VALUES ('This listing looks fake.', 2);

--# POST /seller/{sellerId}/review/{reviewId}/response
--INSERT INTO SellerReviewResponse (responseComment, reviewId)
--VALUES('I had the same experience', 2);

--# GET /seller/{id}/orders
--select * from Orders where sellerId=1;
--select title from Listings join Orders O on Listings.listingID = O.listingID where O.sellerId=1;

--# GET /orders/{id}
--select amountPaid, completed, dateShipped, quantity, t2.listingID, t2.name, t2.title, t2.description from
--(select * from Orders O where O.orderId=1) t1 join
--(select listingID, name, title, description from Listings L join Products P on L.productId=P.productId) t2 on t1.listingID=t2.listingID;


--# GET /authenticator/{authenticatorId}/orders
--select orderId, title, L.listingID, isAuthenticated from Orders
--   join Listings L on Orders.listingID = L.listingID where authenticatorID=1;

--# GET /authenticator/orders/{id}
--select amountPaid, completed, dateShipped, quantity, t2.listingID, t2.name, t2.title, t2.description from
--(select * from Orders O where O.orderId=1) t1 join
--(select listingID, name, title, description from Listings L join Products P on L.productId=P.productId) t2 on t1.listingID=t2.listingID;

--select B.buyerId, firstName, lastName, email, phone from Orders O join Buyers B on O.buyerId = B.buyerId where orderId=1;

--select S.sellerId, firstName, lastName, email, phone from Orders O join Sellers S on O.sellerId = S.sellerId where orderId=1;

--# GET /authenticator/listing/{listingId}/note
--select * from AuthenticatorListingNotes where listingId=1;

--# POST /authenticator/listing/{listingId}/note
--INSERT INTO AuthenticatorListingNotes (noteComment, listingId, authenticatorId)
--VALUES ('This is fake', 2, 2);

--# PUT /authenticator/listing/{listingId}/note
--UPDATE AuthenticatorListingNotes SET noteComment='new note' WHERE listingId=1;