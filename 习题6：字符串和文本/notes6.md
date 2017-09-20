**字符串**

字符串通常是指你想要展示给别人的、或者是你想要从程序里“导出”的一小段字符。Python可以通过文本里的双引号或者单引号识别出字符串来

**问题**

- `%s`和`%r`的区别
- 下面代码中`%r`的作用

  ```
  joke_evaluation = "Isn't that joke so funny?! %r"
  ```
- 为什么 w 和 e 用 `+`连起来就可以生成一个更长的字符串

`%s` - str() 对用户比较友好<br/>
`%r` _ repr() 对python比较友好


```
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
```
上面的三行代码要连起来理解

**python字符串连接的方法**

- 直接通过加号`+`操作符连接
  ```
  website = 'python' + 'tab' + '.com'
  ```
- join方法
  ```
  listStr = ['python', 'tab', '.com']
  website = ''.join(listStr)
  ```
- 替换
  ```
  website = '%s%s%s' % ('python', 'tab', '.com')
  ```
其中第一种方法需要多次重新申请内存，效率比较低<br/>
第三种方法比较简洁高效
