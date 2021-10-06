# import the contract into the script
# accounts package is native to brownie
from brownie import accounts, config, GradeStorage, network

# function for the deploy logic
# brownie deploys to local ganache chain if not defined
# brownie knows if a transaction or call is getting made
def deploy_grade_storage():

    account = get_account()

    # from key is required when deploying to a chain to make a transaction
    grade_storage = GradeStorage.deploy({"from": account})

    # from key is not requied in a view function
    stored_grade = grade_storage.readGrade()
    print(stored_grade)

    # contract interacton to change the value of stored_grade
    transaction = grade_storage.storeGrade(10, {"from": account})

    # wait for transaction to be included in a block
    transaction.wait(1)

    # save the updated grade in a variable
    updated_stored_grade = grade_storage.readGrade()
    print(updated_stored_grade)

# function pulls from config if not on development network
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_grade_storage()
