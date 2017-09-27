```
from sys import argv
```
**import:** <br/>
- 将python的功能**引入**你的脚本的方法。
- Python不会一下子将它所有的功能给你，而是让你需要什么就调什么，这样可以让你的程序保持**精简**。
- 后面的程序员看到你的代码的时候，这些`import`可以作为**提示**，让他们明白你的代码用到了哪些功能

**argv：**<br/>
- 参数变量(argument variable)
- 这是一个非常标准的编程术语，在其他的编程语言里你也可以看到它。
- 这个变量包含了你传递给Python的参数

**模组**(modules)<br/>
把这些我们导入(import)进来的功能称作模组。如：“你需要把sys模组import进来”

```
script, first, second, third = argv
```
上面的代码：<br/>
- 把`argv`中的东西**解包**(unpack)，将所有的参数依次赋予左边的变量名
- 将每一个参数赋予一个变量名：script, first, second,以及third

用下面的方法运行程序<br/>
`python /Users/gusiyang/Desktop/ex13.py first 2nd 3rd`
你可以将"first"、"2nd"、"3rd"替换成任意三样东西

当你运行脚本时提供的参数的个数不对的时候:<br/>
`ValueError: need more than 3 values to unpack`

```
print "The script is called:", script
```
**?** 不管print里面的内容是什么，后面变量的名字取什么，打印出来的都是文件的路径和名字。如果不要这一行打印和这个参数，那么下一个打印就会变成文件的路径和名字

**?** 将`raw_input`和`argv`一起使用，让你的脚本从用户手上得到更多的输入
