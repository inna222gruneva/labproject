import pytest
from bank import Account

def test_initial_balance():
    # create a new account with a name and default value
    a = Account("some dude")
    assert a.get_balance() == 0
    assert a.owner == "some dude"

def test_deposit():
    a = Account("test", 50.0)
    a.deposit(50.0)
    assert a.get_balance() == 100.0

def test_withdraw():
    a = Account("test", 50.0)
    a.withdraw(25.0)
    assert a.get_balance() == 25.0

def test_deposit_negative_amount():
    a = Account("test")
    with pytest.raises(ValueError) as v:
        a.deposit(-5.0)
    
    assert str(v.value) == "You can't deposit values lower than zero."

def test_withdraw_more_than_balance():
    a = Account("test", 0)
    with pytest.raises(ValueError) as v:
        a.withdraw(5.0)
    
    assert str(v.value) == "Value is negative or you do not have proper account balance."

def test_withdraw_negative_amount():
    pass