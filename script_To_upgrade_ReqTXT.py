# Simple script that can be used to replace all == in the requirements.txt file with >=

def getReqFile(reqFile):
    with open(reqFile, 'r') as f:
        file_Data = f.read()
        file_Data = file_Data.replace('==', '>=')
    with open('requirementsUpgraded.txt', 'w') as temp_file:
        temp_file.write(file_Data)

if __name__ == "__main__":
    filename = 'requirements.txt'
    getReqFile(filename)
