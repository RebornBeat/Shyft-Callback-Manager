import requests
import json
import os

def get_api_key():
    key_file = 'api_key.json'
    if os.path.exists(key_file):
        with open(key_file, 'r') as f:
            data = json.load(f)
            return data.get('api_key')
    else:
        print("API key file not found.")
        new_key = input("Please enter your API key: ")
        with open(key_file, 'w') as f:
            json.dump({'api_key': new_key}, f)
        print(f"API key saved to {key_file}")
        return new_key

api_key = get_api_key()
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Available event types
event_types = {
    1: "MARKETPLACE_WITHDRAW",
    2: "NFT_BID",
    3: "NFT_BURN",
    4: "NFT_LIST_CANCEL",
    5: "NFT_LIST",
    6: "NFT_LIST_UPDATE",
    7: "NFT_MINT",
    8: "NFT_SALE",
    9: "COMPRESSED_NFT_SALE",
    10: "COMPRESSED_NFT_LIST",
    11: "COMPRESSED_NFT_LIST_CANCEL",
    12: "COMPRESSED_NFT_LIST_UPDATE",
    13: "COMPRESSED_NFT_BID",
    14: "COMPRESSED_NFT_BID_CANCEL",
    15: "COMPRESSED_NFT_TAKE_BID",
    16: "NFT_TRANSFER",
    17: "SOL_TRANSFER",
    18: "TOKEN_BURN",
    19: "TOKEN_CREATE",
    20: "TOKEN_MINT",
    21: "TOKEN_TRANSFER",
    22: "OFFER_LOAN",
    23: "CANCEL_LOAN",
    24: "REPAY_LOAN",
    25: "REPAY_ESCROW_LOAN",
    26: "TAKE_LOAN",
    27: "EXTEND_LOAN",
    28: "EXTEND_ESCROW_LOAN",
    29: "REQUEST_LOAN",
    30: "CANCEL_REQUEST_LOAN",
    31: "LIQUIDATE_LOAN",
    32: "BUY_NOW_PAY_LATER",
    33: "SWAP",
    34: "CREATE_POOL",
    35: "ADD_LIQUIDITY",
    36: "REMOVE_LIQUIDITY",
    37: "COLLECT_FEES",
    38: "COLLECT_REWARD",
    39: "CREATE_RAFFLE",
    40: "UPDATE_RAFFLE",
    41: "BUY_TICKETS",
    42: "REVEAL_WINNERS",
    43: "CLAIM_PRIZE",
    44: "CLOSE_RAFFLE",
    45: "CANCEL_RAFFLE",
    46: "CREATE_TREE",
    47: "COMPRESSED_NFT_MINT",
    48: "COMPRESSED_NFT_TRANSFER",
    49: "COMPRESSED_NFT_BURN",
    50: "CREATE_REALM",
    51: "DEPOSIT_GOVERNING_TOKENS",
    52: "WITHDRAW_GOVERNING_TOKENS",
    53: "SET_GOVERNANCE_DELEGATE",
    54: "CREATE_GOVERNANCE",
    55: "CREATE_PROGRAM_GOVERNANCE",
    56: "CREATE_PROPOSAL",
    57: "ADD_SIGNATORY",
    58: "REMOVE_SIGNATORY",
    59: "INSERT_TRANSACTION",
    60: "REMOVE_TRANSACTION",
    61: "CANCEL_PROPOSAL",
    62: "SIGN_OFF_PROPOSAL",
    63: "CAST_VOTE",
    64: "FINALIZE_VOTE",
    65: "RELINQUISH_VOTE",
    66: "EXECUTE_TRANSACTION",
    67: "CREATE_MINT_GOVERNANCE",
    68: "CREATE_TOKEN_GOVERNANCE",
    69: "SET_GOVERNANCE_CONFIG",
    70: "POST_MESSAGE",
}
    
def create_callback(address, events, callback_url):
    data = {
      "network": "mainnet-beta",
      "addresses": [address],
      "callback_url": callback_url,
      "events": events
    }

    json_data = json.dumps(data)
    url = "https://api.shyft.to/sol/v1/callback/create"

    response = requests.post(url, headers=headers, data=json_data)

    if response.ok:
        print("Callback created successfully!")
        print(response.json())
    else:
        print("Failed to create callback.")
        print("Error:", response.text)

def add_address(callback_id, address):
    data = {
        "id": callback_id,
        "addresses": [address]
    }

    response = requests.post(
        "https://api.shyft.to/sol/v1/callback/add-addresses",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Address added successfully!")
        print(response.json())
    else:
        print("Failed to add address.")
        print("Error:", response.text)

def remove_address(callback_id, address):
    data = {
        "id": callback_id,
        "addresses": [address]
    }

    response = requests.post(
        "https://api.shyft.to/sol/v1/callback/remove-addresses",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Address removed successfully!")
        print(response.json())
    else:
        print("Failed to remove address.")
        print("Error:", response.text)

def pause_callback(callback_id):
    data = {
        "id": callback_id
    }

    response = requests.post(
        "https://api.shyft.to/sol/v1/callback/pause",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Callback paused successfully!")
        print(response.json())
    else:
        print("Failed to pause callback.")
        print("Error:", response.text)

def resume_callback(callback_id):
    data = {
        "id": callback_id
    }

    response = requests.post(
        "https://api.shyft.to/sol/v1/callback/resume",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Callback resumed successfully!")
        print(response.json())
    else:
        print("Failed to resume callback.")
        print("Error:", response.text)

def remove_callback(callback_id):
    data = {
        "id": callback_id
    }

    response = requests.delete(
        "https://api.shyft.to/sol/v1/callback/remove",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Callback removed successfully!")
        print(response.json())
    else:
        print("Failed to remove callback.")
        print("Error:", response.text)

def update_callback(callback_id, addresses=None, events=None, callback_url=None, enable_raw=None, enable_events=None, encoding=None):
    data = {
        "id": callback_id
    }

    if addresses:
        data["addresses"] = addresses
    if events:
        data["events"] = events
    if callback_url:
        data["callback_url"] = callback_url
    if enable_raw is not None:
        data["enable_raw"] = enable_raw
    if enable_events is not None:
        data["enable_events"] = enable_events
    if encoding:
        data["encoding"] = encoding

    response = requests.post(
        "https://api.shyft.to/sol/v1/callback/update",
        headers=headers,
        data=json.dumps(data)
    )

    if response.ok:
        print("Callback updated successfully!")
        print(response.json())
    else:
        print("Failed to update callback.")
        print("Error:", response.text)

def list_callbacks(print_output=True):
    url = "https://api.shyft.to/sol/v1/callback/list"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        callbacks = response.json()
        if print_output:
            print("List of registered callbacks:")
            print(json.dumps(callbacks, indent=2))
        return callbacks['result']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []

def select_callback_id():
    callbacks = list_callbacks(print_output=False)
    if not callbacks:
        print("No callbacks available.")
        return None

    print("Available callback IDs:")
    for i, callback in enumerate(callbacks):
        print(f"{i + 1}. {callback['_id']}")

    while True:
        try:
            choice = int(input("Select the callback ID by number (or enter 0 to cancel): ")) - 1
            if choice == -1:
                return None
            if 0 <= choice < len(callbacks):
                return callbacks[choice]['_id']
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def select_events():
    print("Available events:")
    for number, event in event_types.items():
        print(f"{number}. {event}")
    
    selected_events = input("Enter the numbers of the events you want to register for, separated by commas: ")
    selected_numbers = [int(num.strip()) for num in selected_events.split(',')]
    
    events = [event_types[num] for num in selected_numbers if num in event_types]
    return events

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create a callback")
        print("2. Remove an address")
        print("3. Add an address")
        print("4. Pause a callback")
        print("5. Resume a callback")
        print("6. Remove a callback")
        print("7. Update a callback")
        print("8. List callbacks")
        print("9. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            address = input("Enter the address to register: ")
            events = select_events()
            callback_url = input("Enter the callback URL: ")
            create_callback(address, events, callback_url)
        elif choice == "2":
            callback_id = select_callback_id()
            if callback_id:
                address = input("Enter the address to remove: ")
                remove_address(callback_id, address)
        elif choice == "3":
            callback_id = select_callback_id()
            if callback_id:
                address = input("Enter the address to add: ")
                add_address(callback_id, address)
        elif choice == "4":
            callback_id = select_callback_id()
            if callback_id:
                pause_callback(callback_id)
        elif choice == "5":
            callback_id = select_callback_id()
            if callback_id:
                resume_callback(callback_id)
        elif choice == "6":
            callback_id = select_callback_id()
            if callback_id:
                remove_callback(callback_id)
        elif choice == "7":
            callback_id = select_callback_id()
            if callback_id:
                addresses = input("Enter addresses (comma-separated) or leave blank: ")
                events = select_events()
                callback_url = input("Enter new callback URL or leave blank: ")
                enable_raw = input("Enable raw data (yes/no) or leave blank: ")
                enable_events = input("Enable events (yes/no) or leave blank: ")
                encoding = input("Enter encoding format or leave blank: ")

                addresses_list = [address.strip() for address in addresses.split(',')] if addresses else None
                enable_raw_bool = True if enable_raw.lower() == 'yes' else False if enable_raw.lower() == 'no' else None
                enable_events_bool = True if enable_events.lower() == 'yes' else False if enable_events.lower() == 'no' else None

                update_callback(callback_id, addresses_list, events, callback_url or None, enable_raw_bool, enable_events_bool, encoding or None)
        elif choice == "8":
            list_callbacks()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
