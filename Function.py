"""
version 1.01
"""

from time import sleep


class Time:
    import time

    now_time = time.localtime()
    # 年
    year = now_time.tm_year
    # 月
    month = now_time.tm_mon
    # 日
    day = now_time.tm_mday
    # 小时
    hour = now_time.tm_hour
    # 分钟
    minute = now_time.tm_min
    # 秒
    second = now_time.tm_sec


# 颜色
class Color:
    # 前景色
    black = '\33[30m'
    red = '\33[31m'
    green = '\33[32m'
    yellow = '\33[33m'
    blue = '\33[34m'
    purple = '\33[35m'
    cyan = '\33[36m'
    white = '\33[37m'
    # 背景色
    black_bg = '\33[40m'
    red_bg = '\33[41m'
    green_bg = '\33[42m'
    yellow_bg = '\33[43m'
    blue_bg = '\33[44m'
    purple_bg = '\33[45m'
    cyan_bg = '\33[46m'
    white_bg = '\33[47m'
    # 显示方式
    default = '\33[0m'  # 默认
    bold = '\33[1m'  # 加粗
    underline = '\33[4m'  # 下划线
    blink = '\33[5m'  # 闪烁
    inverse = '\33[7m'  # 反色
    invisible = '\33[8m'  # 不可见


# 进度条
def bar(long, time):  # import Function：Function.bar(长度，屏幕刷新时间)
    for i in range(long + 1 + long // 2):
        print('\r\33[1;31m' + '—' * abs(long - abs(long - i)) + '\33[34m' + '—' * abs(long - i) + '\33[0m', end='')
        sleep(time)
    print('\33[36mΔΔ\33[0m')  # 完成结束语(\n)ΔΔ
