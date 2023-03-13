from brownie import lottery, network
from scripts import helpfulScripts, deployLottery, startLottery, enterLottery
from web3 import Web3
import time

def endLottery(_account, _lotterySC):
    tx = helpfulScripts.fundSC(_lotterySC.address, _account=_account)
    tx.wait(1)
    endingTx = _lotterySC.endLottery({"from" : _account})
    endingTx.wait(1)
    time.sleep(60)
    print("Lottery Winner is : " + _lotterySC.winner())



def main():
    account = helpfulScripts.getAccount()

    if ("fork" in network.show_active()) :
        lotterySC = deployLottery.deployLottery()
        startLottery.startLottery(account, lotterySC)
        enterLottery.enterLottery(lotterySC, account)
    else:  
        lotterySC = lottery[-1]

    endLottery(account, lotterySC)