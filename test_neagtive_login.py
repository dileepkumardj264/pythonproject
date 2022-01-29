from loginpage import LoginPage
from pytest import mark
from excel_lib import read_data

header = 'email,password'
# data = [('dileepkumar.dj@gmail.com', 'Darwin264'), ('dileepkumar123.dj@gmail.com', 'Darwin264')]
data = read_data('login_negative')
print(data)


@mark.parametrize(header, data)
def test_login(setup, email, password):

    login = LoginPage(setup)
    login.homepage_click_login()
    login.login_enter_email(email)
    login.login_enter_password(password)
    login.login_click_login()
    message = 'Login was unsuccessful. Please correct the errors and try again.'
    assert login.is_login_error_displayed(message) == True
