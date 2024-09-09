from .models import User
from django.core.validators import validate_email



def validate_signup(signup_data):

    username = signup_data.get('username')
    password = signup_data.get('password')
    password2 = signup_data.get('password2')
    nickname = signup_data.get('nickname')
    birth = signup_data.get('birth')
    first_name = signup_data.get('first_name')
    last_name = signup_data.get('last_name')
    email = signup_data.get('email')

    err_msg_list = []
    #username_validate
    if User.objects.filter(username=username).exists():
        err_msg_list.append('이미 있는 username 입니다.')

    #passworkd_validate
    if not password == password2:
        err_msg_list.append('password가 일치하지않습니다.')

    #email_validate
    try:
        validate_email(email)
    except:
        err_msg_list.append('email형식이 맞지 않습니다.')

    if User.objects.filter(email=email).exists():
        err_msg_list.append('중복된 email이 있습니다.')
    
    if err_msg_list:
        return False, err_msg_list
    else:
        return True, err_msg_list