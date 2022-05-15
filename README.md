# DC脚本使用步骤

DC_script

syn script for Design Compiler
How to use:

1 拷贝python脚本至工作目录

`cp main2.py {WorkDir}`

2 设置要综合的RTL地址和top_module以及工艺库

```tcl
main2.py修改3~5行
对应项目的指定目录
script1_file_dir = "/xxx/SynFlow.tcl"
script2_file_dir = "/xxx/Sdc.tcl"
design_file_dir = "/xxxxx/xxx/"

Sdc.tcl修改2~3行
对应顶层的时钟和复位
set RST_NAME				rst_n
set CLK_NAME				clk

SynFlow.tcl修改第2~5行和24行
设置工艺库路径{2~5}
set DESIGN_PATH /opt/PDKs/smic_180/SM00LB501-FE-00000-r0p0-00rel0/aci/sc-m/synopsys 
set search_path "$search_path $DESIGN_PATH"
set target_library "ss_1v62_125c.db"
set link_library "* $target_library"
设置顶层RTL的module{24}
set TOP_DESIGN top_module
```

3 根据不同设计修改script（可选）

​			也可在编译的脚本后修改syn下的script；但需要手动开启DC也就是注释掉main.py最后一行改为

`os.system('cd WORK ') `

4 在工作目录下编译脚本

`python3 main2.py `

一定要用3.0以上的版本；原来写的脚本要在3.6以上的版本跑，我这个带EDA的虚拟机没装上zlib呜呜。白写了qwq

	其中main2.py实现的功能有
	
	1 将RTL和SDC自动拷贝至工作目录下/rtl和/syn/scripts下
	
	2 自动创建/syn/mapped unmapped report WORK文件夹
	
	3 自动生成RTL的filelist,文件多可以不用手敲了
	        SynFlow中是DC脚本操作的流程
	        Sdc中是时序和面积和IO约束（所有约束采用变量引用的方式书写，改动只需在文件头修改变量即可）
	        
	4 启动DC，进入工作目录WORK，读入script（新增功能是可以自动打开DC并链接脚本；若不想直接打开DC可以注释掉main.py最后一行） 




  
