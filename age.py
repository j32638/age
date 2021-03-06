driving = input('請問你有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #系統終止

age = input('請問你的年齡')
age = int(age)
if driving == ('有'):
	if age >= 18:
		print('恭喜你通過了')
	else:
		print('小心被警察捉喔')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照了喔')
	else:
		print('慢慢等安全第一')
