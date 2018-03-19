from random import Random
from django.core.mail import send_mail
from PetHospital.settings import EMAIL_FROM

# 生成随机字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, verifyCode, send_type="register"):

    # 如果为注册类型
    if send_type == "register":
        email_title = "邮箱验证码"
        email_body = "邮箱验证码为{0}".format(verifyCode)
        # 发送邮件
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass