# DC_script
syn script for DC Compiler
How to use:

1 拷贝python脚本至工作目录

`cp main2.py {WorkDir}`

2 设置要综合的RTL地址和top_module

3 根据不同设计修改script

4 编译脚本

`python3 main2.py `一定要用3.0以上的版本；原来写的脚本要在3.6以上的版本跑，我这个带EDA的虚拟机没装上zlib呜呜。白写了qwq

​		其中main2,py实现的功能有

​		1 将RTL和SDC自动拷贝至工作目录下/rtl和/syn/scripts下

​		2 自动创建/syn/mapped unmapped report文件夹

​		3 自动生成RTL的filelist,文件多可以不用手敲了
​		SynFlow中是DC脚本操作的流程

​		Sdc中是时序和面积和IO约束（所有约束采用变量引用的方式书写，改动只需在文件头修改变量即可）
​		 启动DC，读入script（新增功能是可以自动打开DC并链接脚本；若不想直接打开DC可以注释掉main.py最后一行）


