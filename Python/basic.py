2/2 # 结果为float型
2//2 # 结果为int型
bin(10) # 将数字转2进制
oct(10) # 转8进制
hex(10) # 转16进制
ord('w') # 获取字符ASCII码

bool('') # 空字符串，空列表，空字典，0，None等返回False

r'c:\n123' # 会输出原始字符转，不会解释转义字符
aa = 'test'
aa = u'test'  # 轉爲unicode類型

# tuple不可變，存取時tuple和字典都快於列表

#set是无序的，无法用下标取值
{1,2,3} - {2,3} # 取集合差值
{1,2,3} & {2,3} # 取交集
{1,2,3} | {2,3,4} # 取并集

# is比较两个变量内存地址是否相同
# isinstance(a, int)判断变量类型
# isinstance可以多个类型筛选 e.g. isinstance(a, (int, str, float))

# for..else 如果有break则else不会触发

# a[0:10:2]去a的0到9下表, 步数为2

# 模块定义时, 可以通过__all__ = ['a', 'c'] 来指定只导出a变量和c变量
# dir()获取模块内置变量名，不传参默认为当前模块，对于入口文件__package__为None，__name__为__main__，__file__只是根据调用时路径决定
# python -m 可以将执行文件当成模块然运行，e.g python -m severn.c15，此时__package__会变成seven，但是__name__还是__main__
# from import的方式可以使用相对导入，e.g. from .m3 import m, 这里.代表当前路径，..代表上一级路径，每加一个点多一层。
# 注意入口文件不可以使用相对导入，如果想要做到的话就需要用python -m来实现

# sys.setrecursionlimit(1000)设定递归的最多次数

# 关键字参数 e.g. def add(x, y),  add(y=3, x=4)
# 可变参数 e.g. def demo(*param), demo(1,2,3,4) 或者 a = (1,2,3,4) demo(*a)
# 关键字可变参数 e.g. def demo(**param), demo(a='123', b='566') 或者 a = {'a':'32', 'b':'dd'} demo(**a)

# global c; c = 2 可以将局部变量变成全局变量

# 变量可以通过__dict__来获取它的属性和方法
# 在python中，使用对象来访问类变量会自动fallback回类中去寻找
# 实例方法中调用类变量可以通过Student.count或者self.__class__.count

# 通过装饰器@classmethod来定义类方法 e.g.
# @classmethod
# def test(cls):
# python中是可以用对象来调用类方法的，但是不建议使用

# 通过装饰器@staticmethod来定义类方法
# 不需要像类方法或者实例方法一样默认传入一个像self或者cls的参数

# 变量或方法前面加__就会变为私有的
# 但如果结尾使用__的话python就不会当为私有的
# 类中定义私有变量之后其实变量名会变成类似_Student__score
# 所以在外部也还是可以根据这个规范来读写私有变量的

# python中的类是可以多继承的
# 子类中调用父类构造方法可以使用super(Student, self).init(name, age)
# 子类中调用父类的实例方法也可以使用super的方式来调用

# json.loads(json_str) json反序列化
# json.dumps(dict) json序列化

# 將列表轉換位迭代器
iter([1, 2, 3]) # 此時該對象就可以通過next方法調用

# 生成器
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o) # 1
next(o) # 3
next(o) # 5
next(o) # 報錯

# 列表解析
aa = [1, 2, 3]
[ item + 2 for item in aa ] # [3, 4, 5]

# 生成器表達式
( item + 2 for item in aa ) # 返回一個生成器，可以通過next調用

# lambda定義匿名函數
a = lambda x, y: x + y
a(20, 40)

# Regex
# {N}                  匹配前面出现的正则表达式N次    [0-9]{3}
# {M,N}                匹配重复出现M次到N次正则表达式 [0-9]{5,9} 
# re1|re2              匹配正则表达式re1或re2 
# \bthe                任何以"the"开始的字符串
# \bthe\b              仅匹配单词"the"
# \Bthe                任意包含"the"但不以"the"开头的单词
# b[aeiu]t             bat, bet, bit, but
# [cr][23][dp][o2]     一个包含 4 个字符的字符串: 第一个字符是“r”或“c”,后面是“2”或 “3”,再接下来是 “d” 或 “p”,最后是 “o” 或 “2“ ,例 如:c2do, r3p2, r2d2, c3po, 等等。 
# [r-u][env-y][us]     “r”“s,”“t” 或 “u” 中的任意一个字符,后面跟的是 “e,” “n,” “v,” “w,” “x,” 或 “y”中的任意一个字符,再后面 是字符“u” 或 “s”. 
# [^aeiou]             一个非元音字符 
# [^\t\n]              除 TAB 制表符和换行符以外的任意一个字符 
# \w+@\w+\.com         简单的 XXX@YYY.com 格式的电子邮件地址 
# \d+(\.\d*)?          浮点数 匹配：0.004,”“2.”“75.”
# python中正则默认为贪婪模式， e.g. [0-9]{5,9}会贪婪匹配最多到9，如果要转为非贪婪，则使用[0-9]{5,9}?

import re
# from re import search as ss  導入模塊的某個方法並取別名
re.search("a.c", "123abcyul") # 返回第一个匹配的对象
r = re.match("(a.c)", "123abcyul") # match會從頭開始匹配,只要前面不匹配就會返回空
r.groups() # 返回匹配的內容, 是一個元組
r.group(0) # 返回原字符串
r.group(1) # 返回第一個匹配
r.group(0,1,2) # 一次返回多个匹配
# re.findall('正则表达式', 字符串)  查找匹配到的正则字符串，返回列表
# re.findall('正则表达式', 字符串, re.I | re.S)  re.I代表忽略大小写, re.S代表.可以代表包括\n在内的所有字符，默认是不包括\n的
# re.sub('正则表达式', 替换的字串, 原字串, 0)  0代表匹配所有
# 替换的字串也可以改为一个函数 e.g.
# def covert(value): 返回值将作为替换的字串
#     return "!!" + value.group()  value是一个对象
# re.sub('正则表达式', convert, 原字串, 0) 

# 裝飾器
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()
