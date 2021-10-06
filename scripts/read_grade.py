from brownie import GradeStorage, accounts, config

# read from a deployed contract on the rinkeby test network
# get the last item in the array
# brownie is aware of the abi and address
def read_contract():
    grade_storage = GradeStorage[-1]
    print(grade_storage.readGrade())

def main():
    read_contract
