from brownie import accounts, SimpleStorage, network, config
import os


def deploy_simple_storage():
    account = get_account()
    transaction_from = {"from": account}
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy(transaction_from)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, transaction_from)
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
