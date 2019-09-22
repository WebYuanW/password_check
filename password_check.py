password = 'a123456'
x = 0
while x < 3:
    y = input('請輸入密碼： ')
    if y == password:
        print('登入成功')
        break
    elif x == 2:
        print('密碼錯誤三次，帳號已鎖定')
        break
    else:
        print('密碼錯誤，你還有', 2 - x, '次機會')
    x = x + 1