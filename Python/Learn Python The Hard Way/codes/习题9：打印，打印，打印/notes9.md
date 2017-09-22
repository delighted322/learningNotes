**?** 打印时什么时候会出来引号

双引号所表示的字符串通常要写成一行，如：
```
print "Hello,world,haha."
```
如果要写成**多行**
- 其中`\`为连行符
  ```
  print "Hello,\
  world,\
  haha"
  ```
- 或用三个双引号
  ```
  print """
  Hello,
  world,
  haha.
  """
  ```
- 实际上就是
  ```
  print "Hello,\nworld,\nhaha."
  ```
