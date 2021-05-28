gasUsed = 0.000399
TnxCost = 1.00

# If new cost given, compute new TnxCost.
newGasUsed = 0.0024
newTnxCost = 0

newTnxCost = (newGasUsed/gasUsed)*TnxCost
print('New Tnx cost: ', newTnxCost)
