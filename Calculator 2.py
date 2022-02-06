from decimal import *
import os
# from getch import pause
setcontext(ExtendedContext)
try:
    被除數 = input('請輸入被除數')
    被除數 = float(被除數)
    print('被除數=', 被除數)
    除數 = input('請輸入除數')
    除數 = float(除數)
    print('除數=', 除數)
    被除數/除數
except ZeroDivisionError:
    print()
    print('誰給我在除0的，你想把電腦搞死嗎？答案是無限大啦！')
except KeyboardInterrupt:
    print()
    print('計算已終止，原因：手動停止')
    print('貼心提醒：Ctrl+C不是複製')
except ValueError:
    print()
    print('您輸入的不是數字')
else:
    print('商=', int(Decimal(str(被除數))//Decimal(str(除數))))
    print('餘數=', Decimal(str(被除數)) % Decimal(str(除數)))
finally:
    os.system('pause')
