from registrationpage import RegistrationPage
from pytest import mark
from excel_lib import read_data

header = 'gender,fname,lname,email,password'
data = [('Male', 'dileep', 'kumar', 'dileep@gmail.com', 'dileep123')]
# data = read_data('registration')

@mark.parametrize(header, data)
def test_registration(setup, gender, fname, lname, email, password):
    """ setup indirectly passes driver instance """

    reg = RegistrationPage(setup)
    reg.homepage_click_register()
    if gender == 'Male':
        reg.registration_select_male()
    else:
        reg.registration_select_female()
    reg.registration_enter_first_name(fname)
    reg.registration_enter_last_name(lname)
    reg.registration_enter_email(email)
    reg.registration_enter_password(password)
    reg.registration_enter_confirm_password(password)
    reg.registration_click_register()








