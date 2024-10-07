from lib.user_old_enough import *
import pytest # type: ignore

def test_user_acces_granted():
    assert user_old_enough('1986-05-20') == "Access granted"
    
def test_user_access_denied():
    assert user_old_enough('2016-05-20') == f"You are 8 years old which is underage. You must be 16."
    
def test_user_access_granted_birthday_message():
    assert user_old_enough('2008-10-07') == f"Happy 16th! In you go!"
    
    
@pytest.mark.parametrize("alis_bad_inputs", [None, int, float,bool,[]])

def test_user_access_exception(alis_bad_inputs):
    with pytest.raises(Exception) as e:
        user_old_enough(alis_bad_inputs)
    assert str(e.value) == "DOB must be given. Please enter DOB like so `YYYY-MM-DD`"