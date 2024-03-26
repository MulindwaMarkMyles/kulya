import pytest
from django.contrib.auth.models import User


# def test_set_check_password(user_1):
#     user_1.set_password("pass")
#     assert user_1.username == "test_usr"
    
def test_new_user(user_A):
    print(user_A.username)
    assert user_A.username == "Test_usr"
    
    
def test_new_user_2(user_B):
    print(user_B.is_staff)
    assert user_B.is_staff == 'True'