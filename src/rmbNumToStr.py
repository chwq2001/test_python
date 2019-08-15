#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
  把一个浮点数分解成整数部分和小数部分字符串
  num 需要被分解的浮点数
  返回分解出来的整数部分和小数部分。
  第一个数组元素是整数部分，第二个数组元素是小数部分
"""

def divide(num):
    # 将一个浮点数强制类型转换为int型，即得到它的整数部分
    s_num = str(num)
    i_f = s_num.split('.')
    integer = i_f[0]
    fraction = 0
    if len(i_f) > 1 :
        fraction = i_f[1]
    # print(locals())
    # print(globals())
    # 下面把整数转换为字符串
    return (integer, fraction)


han_list = ["零" , "壹" , "贰" , "叁" , "肆" ,\
    "伍" , "陆" , "柒" , "捌" , "玖"]
unit_list = ["拾", "佰", "仟"]

'''
  把一个四位的数字字符串变成汉字字符串
  num_str 需要被转换的四位的数字字符串
  返回四位的数字字符串被转换成汉字字符串
'''


def four_to_hanstr(num_str, is_integer = True):
    result = ""
    if not is_integer:
        num_str = num_str.rstrip('0')
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转成数值
        num = int(num_str[i])
        # 如果不是最后一位数字，而且数字不是零，则需要添加单位（千、百、十）
        if not is_integer:
            result += han_list[num]
        else:
            if i != num_len - 1:
                if num != 0:
                    result += han_list[num] + unit_list[num_len - 2 - i]
                elif num_str[i+1] == '0':
                    continue
                else:
                    result += han_list[num]
            else:
                if num != 0:
                    result += han_list[num]

        # if i != num_len - 1 and num != 0 and is_integer:
        #     result += han_list[num] + unit_list[num_len - 2 - i]
        # # 否则不要添加单位
        # else:
        #     result += han_list[num]
    return result


def integer_to_str(num_str, is_integer=True):
    """
      把数字字符串变成汉字字符串
      num_str 需要被转换的数字字符串
      返回数字字符串被转换成汉字字符串
    """

    if is_integer :
        num_str = num_str.lstrip('0')
        str_len = len(num_str)
        if str_len > 12 :
            print('数字太大，翻译不了')
            return
        # 如果大于8位，包含单位亿
        elif str_len > 8:
            return four_to_hanstr(num_str[:-8], is_integer) + "亿" + \
                four_to_hanstr(num_str[-8: -4], is_integer) + "万" + \
                four_to_hanstr(num_str[-4:], is_integer)
        # 如果大于4位，包含单位万
        elif str_len > 4:
            return four_to_hanstr(num_str[:-4], is_integer) + "万" + \
                four_to_hanstr(num_str[-4:], is_integer)
        else:
            return four_to_hanstr(num_str, is_integer)
    else :
        return four_to_hanstr(num_str, is_integer)

# print(integer_to_str.__doc__)
# print(__doc__)
s_input = input("请输入一个浮点数: ")
while s_input.lower() != 'q':
    # 测试把一个浮点数分解成整数部分和小数部分
    integer, fraction = divide(s_input)
    # 测试把一个四位的数字字符串变成汉字字符串
    print(integer_to_str(integer), end='')
    if int(fraction) != 0:
        print('点'+integer_to_str(fraction, False))
    s_input = input("请输入一个浮点数: ")


