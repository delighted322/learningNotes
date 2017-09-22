```
formatter = "%r %r %r %r"
```
可以用上面的模板打印多个
```
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
```

因为一行太长要换行时 换行前面空四格 括号顶格

打印内容如果加了引号（字符串），则打印出的结果也会加引号
