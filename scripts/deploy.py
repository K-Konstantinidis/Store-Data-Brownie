# accounts: to use an account with the help of brownie
# config: To use our wallet from the .yaml file
# SimpleStorage: Import our contract
# network: Check if the network is a developing one or not
from brownie import accounts, config, SimpleStorage, network

# Deploy a contract and then update the stored value
def deploy_simple_storage():
    # Get an account
    account = get_account()
    # Deploy contract to a chain
    simple_storage = SimpleStorage.deploy({"from": account})
    # Retrieve the initial value from the contract
    stored_value = simple_storage.retrieve()
    print(f"Initial Stored Value: {stored_value}")
    # Update contract value
    transaction = simple_storage.store(10, {"from": account})
    transaction.wait(1)  # Wait 1 block
    # Retrieve the new value
    updated_stored_value = simple_storage.retrieve()
    print(f"Updated Stored Value: {updated_stored_value}")


# Check if the account is a developing one or not
# In this project I connect to my infura.io project. (Use WEB3_INFURA_PROJECT_ID in the .env)
def get_account():
    if network.show_active() == "development":
        return accounts[0]  # Use the account that brownie makes
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # Get key from .yaml, return the address


def main():
    deploy_simple_storage()
