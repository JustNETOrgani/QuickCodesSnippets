gasUsed = 21000
TnxCost = 0.000399
fiatCost = 1.00

# If new cost given, compute new TnxCost.
newGasUsed = 67215


def oneTimeCompute():
    if newGasUsed < gasUsed:
        newEthTnxCost = (gasUsed/newGasUsed)*TnxCost
    else:
        newEthTnxCost = (newGasUsed/gasUsed)*TnxCost
    return newEthTnxCost

def multiCompute(newEthTnxCost):
    if newEthTnxCost < TnxCost:
        newFiatCost = (TnxCost/newEthTnxCost)*fiatCost
    else:
        newFiatCost = (newEthTnxCost/TnxCost)*fiatCost
    return newFiatCost

def main():
    newEthTnxCost = oneTimeCompute()
    print('Cost in Eth: ', newEthTnxCost)
    currentFiatCost =  multiCompute(newEthTnxCost)
    print('Cost in Fiat Currency: ', currentFiatCost)

if __name__== '__main__':
    main()
