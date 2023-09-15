# Python-Commonly Used Personal Codes
I have organized commonly used personal codes, including time, colors and a progress bar for my personal use.
I an a beginner who has self-taught coding, so please feel free to provide guidance if there are any issues with the project.  
整理了个人常在Pytho中会调用的代码，进行了一些简化。暂时包括时间、颜色以及个人使用的进度条。纯自学小白，项目若有问题请指点。  

# 时间使用：
import Function  
if 6 <= Function.Time.hour <= 12:  

# 颜色使用：
from Function import Color  
#与rich.print二选一即可  
print(Color.bold + Color.underline + 'test' + Color.default)  
#rich.print('[cyan]text[/cyan]' + str('[bold red]{:.2f}[/bold red]'.format(level) + '[dim]text[/dim]'))  

# 进度条使用：(仅装饰使用，学的不深)
bar(int, float)  
int为进度条长度，float为进度条单位刷新时间  
总时间 = 长度*3/2*单位时间  
