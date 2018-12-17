"""give all valid schemes for covering an m*n wall with a*b bricks
 
__author__ = "YicBai"
__pkuid__  = "1800011840"
__email__  = "1800011840@pku.edu.cn"
"""

import turtle

alex=turtle.Turtle()


#####___________turtle_part_____________#####

def ksh(i,t,htanses):
    """use turtle to show a visible picture"""
    for (zs,ys,zx,yx) in htanses[i]:
        alex.penup()
        alex.goto((zs%m)*20-10*m,(zs//m)*20-10*n)
        alex.pendown()
        alex.goto((ys%m+1)*20-10*m,(ys//m)*20-10*n)
        alex.goto((yx%m+1)*20-10*m,(yx//m+1)*20-10*n)
        alex.goto((zx%m)*20-10*m,(zx//m+1)*20-10*n)
        alex.goto((zs%m)*20-10*m,(zs//m)*20-10*n)
    alex.hideturtle()
    
#####_________dg_part________#####
    
def dg(lst_0,lst,ans,anses,htans,htanses):
    """for a common brick"""
    
    if 0 not in lst:
        anses.append(ans.copy())
        htanses.append(htans.copy())#!!!!!!!!!!!!!!!!!!!!

    for i in range(m*n):
        zhuan=[]
        if lst[i]==1:
            pass
        else:
            zhuanhp=[]
            zhuansp=[]
            #hp        
            if (i%m+a<=m) and (i//m+b<=n):
                for ai in range(a):
                    for bi in range(b):
                        zhuanhp.append(lst[i+ai+bi*m])
                if 1 not in zhuanhp:
                    for ai in range(a):
                        for bi in range(b):
                            lst[i+ai+bi*m]=1
                            zhuan.append(lst_0[i+ai+bi*m])
                    ans.append(tuple(zhuan))
                    htans.append((i,i+a-1,i+(b-1)*m,i+a-1+(b-1)*m))#!!!!!!!!!!!!!!!!
                    zhuan=[]
                    dg(lst_0,lst,ans,anses,htans,htanses)
                    zhuanlhp=[]
                    for ai in range(a):
                        for bi in range(b):
                            lst[i+ai+bi*m]=0
                    ans.pop()
                    htans.pop()#!!!!!!!!!!!!!!!!!!!!!!!!
                else:
                    pass
            #sp            
            if (i%m+b<=m) and (i//m+a<=n):
                for bi in range(b):
                    for ai in range(a):
                        zhuansp.append(lst[i+bi+ai*m])
                if 1 not in zhuansp:     
                    for bi in range(b):
                        for ai in range(a):
                            lst[i+bi+ai*m]=1
                            zhuan.append(lst_0[i+bi+ai*m])
                    ans.append(tuple(zhuan))
                    htans.append((i,i+b-1,i+(a-1)*m,i+b-1+(a-1)*m))#!!!!!!!!!!!!!!!!
                    zhuan=[]
                    dg(lst_0,lst,ans,anses,htans,htanses)
                    zhuansp=[]
                    for bi in range(b):
                        for ai in range(a):
                            lst[i+bi+ai*m]=0
                    zhuan=[]
                    ans.pop()
                    htans.pop()#!!!!!!!!!!!!!!!!!!!!!!!!
                else:
                    pass
            return    
    
##________main_part________####

def main():
    """print all valid schemes for covering an m*n wall with a*b bricks"""
    
    global m,n,a,b
    
    m=int(input("墙长"))
    n=int(input("墙宽"))
    a=int(input("砖长"))
    b=int(input("砖宽"))

    mn=[]
    plmy=[]

    anses=[]
    ans=[]
    htanses=[]#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    htans=[]#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ans,anses,htans,htanses
    
    for i in range(m*n):
        mn.append(i)
        plmy.append(0)

    if a==b:
        if m%a!=0 or n%a!=0:
            anses=[]
        else:
            zhuan=[]
            for i in range(m//a):
                for j in range(n//a):
                    for k in range(a):
                        for ki in range(a):
                            zhuan.append(mn[i*a+j*a*m+k+ki*m])
                    ans.append(tuple(zhuan))
                    zhuan=[]
                    htans.append(((i*a+j*a*m),(i*a+j*a*m)+a-1,(i*a+j*a*m)+(a-1)*m,(i*a+j*a*m)+(a-1)*m+a-1))
            anses.append(ans.copy())
            htanses.append(htans.copy())
    else:
        dg(mn,plmy,ans,anses,htans,htanses)

    print("共有方案数",len(anses))
    if len(anses)!=0:
        i=input("查看详细结果(输入任意键)？可直接回车跳过")
        if i=="":
            pass
        else:
            for j in range(len(anses)):
                print("方案%d"%(j+1),anses[j])
        fa=int(input('想可视化的方案'))
        ksh(fa-1,alex,htanses) 
    else:
        pass

if __name__ == '__main__':
    main()
