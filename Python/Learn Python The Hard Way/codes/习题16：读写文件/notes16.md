**文件相关的命令(方法/函数)**<br/>
- `close`：关闭文件 跟编辑器的 文件 -> 保存...一个意思 `open().close()`
- `read`：读取文件内容。你可以把结果赋给一个变量 `open().read()`
- `readline`：读取文本文件中的一行
- `truncate`：清空文件 小心使用该命令 `open().truncate()`
- `write(stuff)`：将stuff写入文件

`write`需要接收一个字符串作为参数，从而将该字符串写入文件 `open().write()`

```
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")  # 会弹出一个问号的提示 让用户确认 而不是直接执行后面的代码
```
CTRL-C(^C):用户中断执行 ——> KeyboardInterrupt

```
target = open(filename, 'w')
target.truncate()
```
- `open('/tmp/hello', 'w')`<br/>
  **？** 这里路径加文件名的部分要加引号，但上面的filename没有，是因为filename是变量，还是filename已经是字符串了？<br/>
  \# `open(路径+文件名, 读写模式)`<br/>
  \# 读写模式：r只读，r+读写，w新建(会覆盖原有文件)，a追加，b二进制文件

- 使用`'w'`，文件若存在，首先要清空，然后重新创建

```
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
```

**?** 用一个`target.write()`将line1、line2和line3打印出来
