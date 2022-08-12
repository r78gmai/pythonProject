import random
import platform
print(platform.system()) #OS

# for
print('########## for ##########')
for x in range(9, 11):
    print (x)

# if
print('########## if ##########')
a = 20
if a > 10 and a <= 20:
    print('aは１１から２０までの数字')
if 10 < a <= 20:
    print('aは１１から２０までの数字')
if a == 10 or a <= 20:
    print('aは１0もしくは２０以下の数字')
if not a == 10:
    print('aは１0以外の数字')

# 配列
print('########## 配列 ##########')
array = [1, 2, 3, 4, 5]
for v in array:
    if v == 3:
        continue
    if v == 5:
        break
    print(v)

# 辞書
print('########## 辞書 ##########')
hash_array = dict(age=30, name='John')
if 'name' in hash_array:
    print('name はあります')
if 'aaa' not in hash_array:
    print('aaa というキーはありません')
if 'age' in hash_array:
    print('age はあります')
print(hash_array)
print(hash_array['age'])
print(hash_array['name'])

# 関数
print('########## 関数 ##########')
bb = len('python7')
print(bb)
bb = pow(2, 2)
print(bb)

def max(a, b):
    if a > b:
        return a
    return b
print ( max(2, 5) )

def nabe(v):
    if v % 3 == 0:
        return 'aaa'
    elif "3" in str(v):
        return 'bbb'
    return v
for x in range(1,4):
    print ( nabe(x) )

def make_random_array(size):
    result = []
    for v in range(size):
        result.append( random.randint(0, 100) )
    return result
result = make_random_array(10)
print(result)
result = make_random_array(25)
print(result)
print(result[2])

def foo(*args):
    print(args[0])
    print(args[1])
    print(args[2])
foo("bar", 444, [1, 2, 3])

# 集合
print('########## 集合 ##########')
a_set = set( ['aaa', 'bbbb', 'cc', 'd'] )
if 'bbbb' in a_set:
    print ('True')

b_set = set(['A', 'B', 'C'])
c_set = set(['A', 'B', 'C', 'D'])
print(b_set | c_set)
print(c_set - b_set)
print(b_set & c_set)
print(b_set ^ c_set)