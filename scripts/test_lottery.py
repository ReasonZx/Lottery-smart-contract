from brownie import lottery, network
from scripts import helpfulScripts, deployLottery
from web3 import Web3


def testGetEntranceFee():
    if ("fork" in network.show_active()) :
        lotterySC = scripts.deployLottery.deployLottery()
    else:  
        lotterySC = lottery[-1]

    print(Web3.fromWei(lotterySC.getEntraceFee(), "ether"))


def main():
    testGetEntranceFee()