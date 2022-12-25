from brownie import lottery, accounts, config, network
import scripts.helpfulScripts
from web3 import Web3


def test_get_entrance_fee():
    account = scripts.helpfulScripts.getAccount()
    lottery_contract = lottery.deploy(
        scripts.helpfulScripts.getPriceFeedAddress(account),
        {'from': account},
    )
    print(Web3.fromWei(lottery_contract.getEntraceFee(), "ether"))


def main():
    test_get_entrance_fee()