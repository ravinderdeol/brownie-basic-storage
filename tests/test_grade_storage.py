from brownie import accounts, GradeStorage

# test functions follow 'arrange' 'act' and 'assert'
def test_deploy():

    account = accounts[0]

    grade_storage = GradeStorage.deploy({"from": account})
    starting_grade = grade_storage.readGrade()
    expected = 0

    assert starting_grade == expected

def test_updating_grade():

    account = accounts[0]
    grade_storage = GradeStorage.deploy({"from": account})

    expected = 10
    grade_storage.storeGrade(expected, {"from": account})

    assert expected == grade_storage.readGrade()
