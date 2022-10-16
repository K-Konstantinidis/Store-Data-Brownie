from brownie import SimpleStorage, accounts, config


# Retrieve the value of the most recent deployed contract
def read_contract():
    simple_storage = SimpleStorage[-1]  # -1 returns the most recent contract deployment
    # ABI -> ABI is saved in the build->contracts folder (name.json file) after compiling the .sol contract
    # Address -> Address is saved in the build->deployments folder (name.json file) after deploying the contract in a network
    print(simple_storage.retrieve())


def main():
    read_contract()
