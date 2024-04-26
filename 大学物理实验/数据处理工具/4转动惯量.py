"""
这是一个计算转动惯量的程序。

大家只需要把主函数的实参替换成自己的数据就可以啦。

这里，变量命名时，前缀 ex 代表实验值， cal 代表理论值。

传入实参时，要注意 m 的单位是 kg, 但几何尺度的单位是 cm。
"""

PI = 3.1415


def exJ_0(K, T_0):
    """
    计算转动惯量的实验值

    """
    J = K * (T_0**2) / (4 * PI**2)
    return J


def calJ_1(m, D):
    """
    计算 J_1 的理论值

    m:质量
    D:直径
    J:转动惯量
    """
    D *= 0.01

    J_1 = 1 / 8 * m * (D**2)
    return J_1


def calK(J_1, T_0, T_1):
    """
    计算扭转常量 k

    J:转动惯量
    K:扭转常量
    """
    k = 4 * (PI**2) * J_1 / (T_1**2 - T_0**2)
    return k


def calJ_2(m, D, d):
    """
    计算 J_2 的理论值

    m:质量
    D:外径
    d:内径
    J:转动惯量
    """

    D *= 0.01
    d *= 0.01

    J_2 = 1 / 8 * m * (D**2 + d**2)
    return J_2


def exJ_2(K, T_2, exJ_0):
    """
    计算 J_2 的实验值

    K:扭转常量
    """
    J_2 = (K / (4 * (PI**2))) * T_2**2 - exJ_0
    return J_2


def calJ_3(m, a, b):
    """
    计算 J_3 的理论值

    m:质量
    J:转动惯量
    """
    a *= 0.01
    b *= 0.01

    J_3 = 1 / 12 * m * (a**2 + b**2)
    return J_3


def exJ_3(K, T_3, exJ_0):
    """
    计算 J_3 的实验值

    K:扭转常量
    """
    J_3 = (K / (4 * (PI**2))) * T_3**2 - exJ_0
    return J_3


def calJ_4(m, D):
    """
    计算 J_4 的理论值

    m:质量

    J:转动惯量
    """
    D *= 0.01

    J_4 = 1 / 10 * m * (D**2)
    return J_4


def exJ_4(K, T_4):
    """
    计算 J_4 的实验值

    K:扭转常量
    """
    J_4 = (K / (4 * (PI**2))) * T_4**2
    return J_4


def calJ_5(m, l):
    """
    计算 J_5 的理论值

    m:质量
    l:长度

    J:转动惯量
    """
    l *= 0.01

    J_5 = 1 / 12 * m * (l**2)
    return J_5


def exJ_5(K, T_5):
    """
    计算 J_5 的实验值

    K:扭转常量
    """
    J_5 = (K / (4 * (PI**2))) * T_5**2
    return J_5


def cal_J(J_5, m, x, J_6):
    """
    验证平行轴转动定理

    计算 J 的理论值
    """
    x *= 0.01
    J = J_5 + 2 * m * x**2 + J_6
    return J


def ex_J(K, T):
    """
    验证平行轴转动定理

    计算 J 的实验值
    """
    J = K / (4 * PI**2) * T**2
    return J


def main():
    """
    主函数
    在这里代入数据即可。

    注意传入的实参中：
    质量的单位是 kg,
    几何尺度的单位是 cm,
    其余与国际单位制一致。
    """
    CAJ_1 = calJ_1(0.71711, 10.011)  # 计算 J_1 的理论值
    K = calK(CAJ_1, 0.858, 1.385)  # 计算扭转常量
    EXJ_0 = exJ_0(K, 0.858)  # 计算 J_0 的实验值

    CAJ_2 = calJ_2(0.71857, 10.000, 9.371)  # 计算 J_2 的理论值
    EXJ_2 = exJ_2(K, 1.720, EXJ_0)  # 计算 J_2 的实验值

    CAJ_3 = calJ_3(0.17504, 7.029, 6.960)  # 计算 J_3 的理论值
    EXJ_3 = exJ_3(K, 0.960, EXJ_0)  # 计算 J_3 的实验值

    CAJ_4 = calJ_4(1.1727, 11.370)  # 计算 J_4 的理论值
    EXJ_4 = exJ_4(K, 1.408)  # 计算 J_4 的实验值

    CAJ_5 = calJ_5(0.13333, 61.00)  # 计算 J_5 的理论值
    EXJ_5 = exJ_5(K, 2.224)  # 计算 J_5 的实验值

    # 输出结果
    print("扭转常量 K:\n")
    print("K = %.4f\n" % K)

    print("理论值：\n")
    print("J_1 = %.6f\n" % CAJ_1)
    print("J_2 = %.6f\n" % CAJ_2)
    print("J_3 = %.6f\n" % CAJ_3)
    print("J_4 = %.6f\n" % CAJ_4)
    print("J_5 = %.6f\n" % CAJ_5)

    print("实验值：\n")
    print("J_0 = %.6f\n" % EXJ_0)
    print("J_2 = %.6f\n" % EXJ_2)
    print("J_3 = %.6f\n" % EXJ_3)
    print("J_4 = %.6f\n" % EXJ_4)
    print("J_5 = %.6f\n" % EXJ_5)

    print("百分差：\n")
    print("J_2 = %.6f\n" % ((EXJ_2 - CAJ_2) / CAJ_2 * 100))
    print("J_3 = %.6f\n" % ((EXJ_3 - CAJ_3) / CAJ_3 * 100))
    print("J_4 = %.6f\n" % ((EXJ_4 - CAJ_4) / CAJ_4 * 100))
    print("J_5 = %.6f\n" % ((EXJ_5 - CAJ_5) / CAJ_5 * 100))

    print("验证平行轴转动定理： \n")
    J_6 = 1 / 2 * 0.87 * 10 ** (-4)
    x = [5.00, 10.00, 15.00, 20.00, 25.00]  # 距离（无需更改）
    T = [2.635, 3.434, 4.451, 5.600, 6.726]  # 周期平均值

    for i in range(5):
        print("x = %.2f 时:\n" % x[i])

        caJ = cal_J(CAJ_5, 0.2397, x[i], J_6)  # 计算 J 的理论值
        exJ = ex_J(K, T[i])  # 计算 J 的实验值

        print("\tcaJ = %.6f\n" % caJ)
        print("\texJ = %.6f\n" % exJ)
        print("\t百分差 = %.6f\n" % ((exJ - caJ) / caJ * 100))


if __name__ == "__main__":
    main()
