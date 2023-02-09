password = 'a123456'
i = 1
while i < 4:
	inp = input('請輸入密碼:')
	if inp == password:
		print('登入成功')
		break
	elif inp != password:
		if i < 3:
			print('密碼錯誤! 還有', 3-i,'次機會')
		else:
			print('密碼錯誤3次，請稍後再登錄')
	i = i+1