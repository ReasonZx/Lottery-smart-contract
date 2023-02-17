from brownie import lottery, network
from scripts import helpfulScripts, deployLottery, startLottery
from web3 import Web3



def enterLottery(_lotterySC, _account):
    value = _lotterySC.getEntraceFee() + 100000000
    enterTx = _lotterySC.enter({"from":_account, "value": value})
    enterTx.wait(1)
    print("Entered Lottery!")



def main():
    account = helpfulScripts.getAccount()

    if ("fork" in network.show_active()) :
        lotterySC = deployLottery.deployLottery()
        startLottery.startLottery(account, lotterySC)
    else:  
        lotterySC = lottery[-1]

    enterLottery(lotterySC, account)