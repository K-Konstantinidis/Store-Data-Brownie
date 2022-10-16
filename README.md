# Store-Data-Brownie
## SimpleStorage.sol
A smart contract to:
- Store and retrieve a value.
- Store a person and their favourite number

## Deploy.py
A python script to: 
- Connect to a Blockchain `(Testnet, Mainnet)`
- Get an account safely:
  - From brownie if we want to test
  - A real one via the config & .env file
- Deploy our contract
- Retrieve the initial stored value
- Create a new transaction to update the stored value
- Retrieve the new stored value

## Read_value.py
- Retrieve the most recent deployed contract

## Test_simple_storage.py
-  Test if the deployment is correct
-  Test if updating the value works correctly

## Help with the project
To run the code there are some requirements. You must install: 

### pipx 
Install _pipx_ by running the following on the command line: `python -m pip install --user pipx` then `python3 -m pipx ensurepath`

For more information check: <a href="https://pypa.github.io/pipx/">Install pipx</a>

### Brownie
Install _Brownie_ by running the following on the command line: `pip install eth-brownie`

For more information check: <a href="https://pypi.org/project/eth-brownie/">Install Brownie</a>

This is the Lesson 5 of the <a href="https://www.youtube.com/c/Freecodecamp">freeCodeCamp.org</a> tutorial: https://www.youtube.com/watch?v=M576WGiDBdQ with more comments.
