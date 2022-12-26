from brownie import lottery, network
from scripts import helpfulScripts, deployLottery, startLottery
from web3 import Web3










def main():
    account = helpfulScripts.getAccount()

    if ("fork" in network.show_active()) :
        lotterySC = deployLottery.deployLottery()
    else:  
        lotterySC = lottery[-1]

    startLottery.startLottery(account, lotterySC)