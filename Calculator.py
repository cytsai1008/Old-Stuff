from getch import pause
被除數 = input('請輸入被除數')
被除數 = float(被除數)
print('被除數=',被除數)
除數 = input('請輸入除數')
除數 = float(除數)
print('除數=',除數)
if(除數 == 0):
    print('誰給我在除0的，你想把電腦搞死嗎？答案是無限大啦！')
else:
    print('商=', int(被除數//除數))
    print('餘數=', (被除數-除數*被除數//除數))
    print('商x除數=', int(除數*被除數//除數))
pause('按任意鍵以離開')
