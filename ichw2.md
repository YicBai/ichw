# ichw2
##概论作业2

1,图灵对停机问题的证明
    
 （1）图灵为什么要证明停机问题：证伪停机问题，即证明图灵机不能解决所有问题。
 
 （2）证明方法：反证法。先假设存在程序f，能停机判定为真，否则判定为假。再构造程序g，若调用f判定为真，则进入死循环，输出假，否则输出真，那么，当g调用自身，则不论如何，都进入死循环。举出此反例，就证明了图灵机无法对所有程序和输入判定能否停机。
 
 2，二进制补码的原理
 
  二进制补码中，将第一位用于表示整数的符号，0表示正，1表示负。以四位为例，0111即表示7，而表示负数时，例如-2，先表示2，为0010，在每位取反，为1101，然后加一，为1110，其他负数表示方法相同，这样，四位即可表示-8到+7的16个数。这样，可以用正负数相加的方式统一加减法。相加时，超出位数的进位被舍去，其结果相当于计算与0的距离。仍以四位为例，负数-x相当于无符号数中16-x的表示，相加时舍去进位的16，就得到与负数相加的结果。
  
 3，浮点数的表示
 
  +0：0000000000000000   
  -0：1000000000000000    
  +1.0：0011111100000000  
  -1.0：1011111100000000
  
  最大非规范化数：1000000011111111/0000000011111111，表示+-（1-2^(-8))*2^(-62)
  
  最小非规范化数:1000000000000001/0000000000000001,表示+-2^(-8)*2^(-62)
  
  最小规范化浮点数:0000000100000000/1000000100000000,+-1*2^(-62)
  
  最大规范化浮点数:0111111011111111/1111111011111111,+-(2-2^(-8))*2^63
  
  正负无穷:0111111100000000/1111111100000000
  
  NaN:sign:0/1,exp:1111111,frac:non zero
  
