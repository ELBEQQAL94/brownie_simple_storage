from brownie import accounts, SimpleStorage


def deploy_simple_storage(transaction_from):
    simple_storage = SimpleStorage.deploy(transaction_from)
    return simple_storage


def test_deploy():
    account = accounts[0]
    transaction_from = {"from": account}
    simple_storage = deploy_simple_storage(transaction_from)
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected


def testing_update_storage():
    account = accounts[0]
    transaction_from = {"from": account}
    simple_storage = deploy_simple_storage(transaction_from)
    expected = 15
    simple_storage.store(expected, transaction_from)
    assert simple_storage.retrieve() == expected
