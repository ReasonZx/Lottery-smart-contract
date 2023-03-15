# Lottery-smart-contract

(might not work anymore as Goerli testnet is getting deprecated)
Smart Contract example deployed @ 0xe0CD0AfFc52Ed7bD8128aee29041595701020476 on Goerli Testnet


# Deploy
## Local Network
To deploy on a local network (needs Mocks), run:
```
brownie run scripts/deploy.py --network development
```

## Testnet
To deploy on a testnet, get your keys for that testnet and the project id from infura.io.

For example Goerli testnet:
```
$export PUBLIC_KEY="your_public_key"
$export PRIVATE_KEY="your_private_key"
$export WEB3_INFURA_PROJECT_ID="your_infura_project_id"
```
```
$brownie run scripts/deployLottery.py --network goerli
$brownie run scripts/startLottery.py --network goerli
$brownie run scripts/enterLottery.py --network goerli
$brownie run scripts/endLottery.py --network goerli
```

## Mainnet-fork
To have locally a mainnet-fork go to alchemy.com and create a new app (creates a fork). Then run the following command to add that fork to your local enviroment with brownie:
```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/********* accounts=10 mnemonic=******* port=8545
```
