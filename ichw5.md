# 概论作业5
## 1.北京大学某单位的某台机器IP地址为162.105.80.160, 子网掩码为255.255.255.192，
 - 1） 该单位的网络号(网络+子网)是多少？
 - 解答： 192化为二进制是11000000，即网络号占26位，为10100010 01101001 00101000 01
 - 2） 该单位理论上可容纳多少主机？
 - 解答： 主机号共6位，即最多64台，除去网关和广播地址，剩余62台
 - 3） 北大可以有多少个这样的子网(假定北大全部是162.105网段)？
 - 解答：子网号共10位，可有1024个
 
## 2.解释TCP协议建立连接为什么设计为三步握手（3-way handshake）？
 * 经过发出信号及回复确认2次后，双方可确认建立了可靠的联系通路，保证信息传导可靠，无需更多次交互；而不足3次则无法保证连结准确。
## 3.有哪些恶意软件, 如何防范恶意软件？
* 1）种类有：木马、蠕虫、病毒、间谍软件、广告软件等。
* 2）防范:
 - 安装杀毒软件/安全防护软件, 及时打补丁
 - 使用防火墙, 禁止外部计算机通过网络访问本机
 - 不随便下载运行可执行程序 
 - 不打开未知的邮件附件 
 - U 盘 通常带毒, 打开前要先查毒 
 - 不随便暴露自己的 email、生日、手机等重要信息 
 - 不以 Administrator 权限操作计算机 
