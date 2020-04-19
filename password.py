password = 'a123456'
x = 3
while x > 0 :
	correct = input('請輸入密碼:')
	if correct != password:
		x = x-1
		print('密碼錯誤!您還剩下', x,'次機會')
	else: 
		print('您成功登入')
		break