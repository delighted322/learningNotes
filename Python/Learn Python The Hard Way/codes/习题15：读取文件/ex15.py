from sys import argv  # 把sys模组导入(import)进来

script, filename = argv  # 使用argv来获取文件名

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
