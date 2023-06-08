from steam.client import SteamClient
from steam.enums import EResult
from steam.webapi import WebAPI
from binance.client import Client
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the variables
steam_username = os.getenv('STEAM_USERNAME')
steam_password = os.getenv('STEAM_PASSWORD')
crypto_api_key = os.getenv('CRYPTO_API_KEY')
crypto_api_secret = os.getenv('CRYPTO_API_SECRET')

# Initialize the Steam Web API
api = WebAPI(key=os.getenv('STEAM_API_KEY'))

# Create a SteamClient instance
client = SteamClient()

# Log into your Steam account
login_result = client.login(username=steam_username, password=steam_password)
if login_result != EResult.OK:
    print(f"Failed to log in: {EResult(login_result).name}")
    exit()

# Initialize the Binance client
binance_client = Client(crypto_api_key, crypto_api_secret)

# Function to calculate the amount of Bitcoin equivalent to a TF2 key with a 30% discount
def calculate_amount(offer):
    tf2_key_price = 2.30  # in USD
    bitcoin_price = 26724.94  # in USD
    bitcoin_amount = (tf2_key_price * 0.7) / bitcoin_price
    total_amount = offer * bitcoin_amount
    return total_amount

# Function to execute the crypto transaction
def execute_crypto_transaction(offer):
    amount_to_sell = calculate_amount(offer)
    order = binance_client.order_market_sell(
        symbol='BTCUSDT',
        quantity=amount_to_sell,
    )
    if order['status'] == 'FILLED':
        return True
    else:
        return False

# Check if it's tf2 key
def is_tf2_key(item):
    TF2_KEY_IDS = {5021, 5057} 
    return item['assetid'] in TF2_KEY_IDS

# Check if the offer is valid
def is_valid_offer(offer):
    return all(is_tf2_key(item) for item in offer['items_to_receive'])

# Accept trade offer
def accept_trade_offer(trade_offer_id):
    response = api.call('IEconService.AcceptTradeOffer', tradeofferid=trade_offer_id)
    if response.get('response', {}).get('result') == 'accepted':
        return True
    else:
        return False

# Function to handle incoming messages
@client.on("chat_message")
def on_message(user, text):
    command = text.strip().lower()
    if command == "!commands":
        user.send("Commands: !commands, !deposit, !withdraw, !rate, !fee, !prices, !balance, !buy, !sell, !stock")
    elif command.startswith("!deposit"):
        user.send("Deposit handling not implemented yet.")
    elif command.startswith("!withdraw"):
        user.send("Withdraw handling not implemented yet.")
    elif command == "!rate":
        user.send("Rate handling not implemented yet.")
    elif command == "!fee":
        user.send("Fee handling not implemented yet.")
    elif command == "!prices":
        user.send("Prices handling not implemented yet.")
    elif command == "!balance":
        user.send("Balance handling not implemented yet.")
    elif command.startswith("!buy"):
        user.send("Buy handling not implemented yet.")
    elif command.startswith("!sell"):
        user.send("Sell handling not implemented yet.")
    elif command == "!stock":
        user.send("Stock handling not implemented yet.")


# Function to get trade offers
def get_trade_offers():
    response = api.call('IEconService.GetTradeOffers', get_received_offers=1)
    return response['response']['trade_offers_received']

# Main loop
while True:
    # Check for trade offers
    trade_offers = get_trade_offers()

    for offer in trade_offers:
        # If a valid trade offer is found, accept it
        if is_valid_offer(offer):
            # Count the number of keys in the offer
            key_count = len(offer['items_to_receive'])

            # Accept the offer
            if accept_trade_offer(offer['tradeofferid']):
                # If the offer is successfully accepted, execute the corresponding cryptocurrency transaction
                execute_crypto_transaction(key_count)