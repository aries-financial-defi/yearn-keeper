# yearn keeper

a keeper bot for yearn v1 strategies which is a tad too smart

## requirements

- python 3.7+
- `pip install eth-brownie`
- `geth --http --graphql`
- being assigned a strategist role

## environments

* update `~/.bash_profile`
```
export ETHERSCAN_TOKEN=
export WEB3_INFURA_PROJECT_ID=
export ETH_RPC_URL=
export REGISTRY_ADDRESS=
export KEEPER3CRV_ADDRESS=
export UNISWAP_ADDRESS=
```

* load `$ source ~/.bash_profile`

## start

* mainnet
```BASH
$ brownie run scripts/keeper.py --network mainnet
```

# load strategist account
```BASH
$ brownie account:
$ Enter the password to unlock this account:
```

## supported strategies

- `StrategyCurve3CrvVoterProxy` uses a combination of the following
    - 24h min interval
    - 1000 3Crv min gross earnings
    - cover gas costs with strategist reward
