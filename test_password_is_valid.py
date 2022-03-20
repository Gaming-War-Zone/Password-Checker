import pytest
from password_checker import PSW_check

    
def get_data():
    password = 'Fhatuwani@ft1 '
    psw_check = PSW_check()
    result = psw_check.password_is_valid(password)
    return result

def test_pwd_exist():
    result = get_data()
    assert result.get('pwd_len') !=0,  "password should exist"

def test_len():
    result = get_data()
    assert result.get('pwd_len') >8, "password should be longer than than 8 characters"

def test_lowercase():
    result = get_data()
    assert result.get('has_lowercase') == 'Yes', "password should have at least one lowercase letter"

def test_uppercase():
    result = get_data()
    assert result.get('has_uppercase') == 'Yes', "password should have at least one uppercase letter"

def test_digit():
    result = get_data()
    assert result.get('has_digit') == 'Yes', "password should have at least have one digit"

def test_special_char():
    result = get_data()
    assert result.get('has_special_chr') == 'Yes', "password should have at least one special character"

def test_wht_spc():
    result = get_data()
    assert result.get('has_wht_spc') == 'Yes', "password should have at least one whitespace character"



if __name__ == '__main__':
    pytest.main()
