# Help for testing: https://docs.pytest.org/en/6.2.x/contents.html
from brownie import accounts, SimpleStorage

# See if the initial value is correct when we deploy the contract
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 0
    # Assert
    assert starting_value == expected_value


# See if updating a value works correctly
def test_update():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected_value = 15
    simple_storage.store(expected_value, {"from": account})
    # Assert
    assert expected_value == simple_storage.retrieve()
