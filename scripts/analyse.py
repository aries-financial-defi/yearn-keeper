# this file analyse the vaults for yearn
import requests
from brownie import Contract, interface, web3

def main():
    r = requests.get("https://api.yearn.tools/vaults")
    for vault in r.json():
        strategy = Contract(vault['strategyAddress'])
        want = strategy.want()
        if vault['tokenAddress'] == want:
            print("{0: <50} token is same with want address".format(vault['tokenName']))
        else:
            print("{0: <50}  token is different with want address".format(vault['tokenName']))
            controller = Contract(vault['controllerAddress'])
            print("Controller address: {0:16} Convertor: {0:16}".format(vault['controllerAddress'], controller.converters(vault['tokenAddress'], want)))
            

