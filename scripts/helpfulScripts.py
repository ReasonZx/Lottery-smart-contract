from brownie import accounts, network, config, MockV3Aggregator, Contract, LinkToken

def getAccount():
    if network.show_active() == "development" or ("fork" in network.show_active()):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def getContractAddress(_contractName, _account=None):
    if network.show_active() == "development":
        mockAggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": _account})
        return mockAggregator.address
    else:
        return config["networks"][network.show_active()][_contractName]

def getContract(_contractType, _account=None):
    SCaddress = getContractAddress(_contractName, _account)
    if network.show_active() == "development":
        print("Functionality not available in development network. Use testnet or local fork.")
        exit()
    else:
        contract = Contract.from_abi(_contractType.name, SCaddress, _contractType.abi)
    
    return contract 



def fundSC (SCadress, account=None, token=None, ammount = 100000000000000000):      #0.1
    if(not account):
        account = getAccount()
    if(not token):
        token = getContract(LinkToken)

    tx = token.transfer(SCadress, ammount, {"from": account})
    tx.wait(1)
    
    print("Contracted funded!")
    return tx