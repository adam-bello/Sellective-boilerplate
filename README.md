# Sellective: An eCommerce Platform fro Collectables

Sellective is an online platform fro buying and selling collectible items. Oftentimes when buying collectibles, it can be hard to know if you should trust the seller to provide you with an authentic product. Sellective aims to solve this probelm by creating a platform where orders are verified by verified authenticators before they are finalized. Our platform allows sellers to post listings for their items, which anyone can browse. To build trust in these sellers, buyers and can leave reviews for both specific listings and the sellers. If the seller wishes, they can respond to these reviews to clear anything up. Our main feature relies on our authenticators, who are specialists who maek sure that orders and listings are authentic. They can leave notes on listings with their thoughts, as well as mark orders made by buyers as authentic before the order is finalized. It is through this process that we hope to provide a safer and more trusting online environment for buying and selling collectibles.

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




