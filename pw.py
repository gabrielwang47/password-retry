# 密碼重試程式

# 先在程式碼中設定好密碼 password = 'a123456'
# 讓使用者最多輸入三次密碼
# 不對的話, 就印出"密碼錯誤！ 還有＿次機會"
# 對的話, 就印出"登入成功!"

password = 'a123456'

i = 2

while i >= 0:

	entry = input('請輸入密碼: ')
	
	if password == entry:
		print('登入成功!')
		break # 逃出迴圈

	else: 
		print('密碼錯誤! 還有', i, '次機會')
		i = i - 1

if i < 0:
	print('你已經錯誤三次, 暫時不能登入！')




