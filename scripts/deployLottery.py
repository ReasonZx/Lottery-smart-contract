from brownie import lottery, config, network
from scripts import helpfulScripts
from web3 import Web3


def deployLottery():
    account = helpfulScripts.getAccount()
    
    lottery_contract = lottery.deploy(
        helpfulScripts.getContractAddress("eth_usd_price_feed", account),
        helpfulScripts.getContractAddress("vrfCoordinator", account),
        helpfulScripts.getContractAddress("link", account),
        helpfulScripts.getContractAddress("fee", account),
        helpfulScripts.getContractAddress("keyHash", account),
        {'from': account},
    )
    return lottery_contract


def main():
    deployLottery()