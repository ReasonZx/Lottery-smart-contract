from brownie import lottery, network
from scripts import helpfulScripts, deployLottery



def startLottery(_account, _lotterySC):
    startTx = _lotterySC.startLottery({'from': _account})
    startTx.wait(1)
    print("Lottery started!")


def main():
    account = helpfulScripts.getAccount()

    if ("fork" in network.show_active()) :
        lotterySC = deployLottery.deployLottery()
    else:  
        lotterySC = lottery[-1]

    startLottery(account, lotterySC)