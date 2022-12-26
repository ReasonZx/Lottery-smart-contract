from brownie import lottery
from scripts import helpfulScripts
from web3 import Web3


def deployLottery():
    account = helpfulScripts.getAccount()
    
    lottery_contract = lottery.deploy(
        helpfulScripts.getContractAddress(account, "eth_usd_price_feed"),
        helpfulScripts.getContractAddress(account, "vrfCoordinator"),
        helpfulScripts.getContractAddress(account, "linkToken"),
        helpfulScripts.getContractAddress(account, "keyHash"),
        helpfulScripts.getContractAddress(account, "fee"),
        {'from': account},
    )
    return lottery_contract


def main():
    deployLottery()