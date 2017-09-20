**格式化字符串**(format string)

- 每一次使用""把一些文本引用起来，你就建立了一个字符串
- 字符串是程序将信息展示给人的方式
- 你可以打印字符串 可以将它们写入文件，还可以将它们发送给网站服务器

学会创建包含变量内容的字符串，使用专门的格式和语法把变量的内容放到字符串里


**问题：**

- `%`后打不出英文括号，不知道为什么
- `%d`、`%s`
- python一行代码不能太长，换行后总是提醒缩进有错

**格式化字符**<br/>
- `%s`:字符串（采用str()的显示）
- `%r`:字符串（采用repr()的显示 不管什么都打印出来）
- `%c`:单个字符
- `%b`:二进制整数
- `%d`:十进制整数
- `%f`:浮点数
- `%%`:字符%
- ... ...

**注：**

格式化字符串时，Python使用一个字符串作为模板。模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。Python用一个tuple将多个值传递给模板，每个值对应一个格式符。如：
```
print "I'm %s. I'm %d year old." % ('Vamei', 99)
```
上面的例子中，`"I'm %s. I'm %d year old."`为我们的模板。%s为第一个格式符，表示一个字符串。%d为第二个格式符，表示一个整数。`('Vamei', 99)`的两个元素'Vamei'和99为替换%s和%d的真实值。<br/>
在模板和tuple之间有一个%号分隔，它代表了格式化操作

**使用变量将英寸和磅转换成厘米和千克**（不会）

1英寸(in)=2.54厘米(cm)<br/>
1磅(lb)=0.45359237千克(kg)
```
my_height = 65  # inches
my_weight = 100  # lb
transform_height = 2.54 * my_height  # cm
transform_weight = 0.45359237 * my_weight  # kg
print "I'm %f inches tall, %f cm." % (my_height, transform_height)
print "I'm %f ponds weight, %f kg." % (my_weight, transform_weight)
```
