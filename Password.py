#密码重试程式

#先在程式码中 设定好密码 password = 'a123456'
#让使用者【最多输入3次密码】
#不对的话，就印出“密码错误！还有__次机会“
#对的话，就印出”登入成功“

password = 'Deskjet911'
i = 3 #剩余机会
while i > 0:
	pwd = input ('请输入密码:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		i = i - 1 
		print('密码错误！还有', i, '次机会')
		
