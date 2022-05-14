import os

def CopyScript():
    os.system('cp {} ./syn/script/'.format(script1_file_dir))
    os.system('cp {} ./syn/script/'.format(script2_file_dir))

def WriteFilelist(filename,wdata):
    with open(filename,'a') as file:
        file.write(wdata+"\n")
    
def CopyAndCreatFilelist(file_dir):
    work_dir =  "./rtl"
    os.system('rm -rf {}'.format(work_dir))
    os.system('mkdir rtl')
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            design = os.path.splitext(file)[0]
            if os.path.splitext(file)[1] == ".v":
                wdata ="{}/{}.v".format(root,design)
                WriteFilelist('./files_syn.fl',wdata)
                dir_path ="{}/{}.v".format(work_dir,design)
                source_path="{}/{}.v".format(root,design)
                os.system('cp {} {}'.format(source_path,dir_path))
            elif os.path.splitext(file)[1] == ".vh":
                wdata ="{}/{}.vh".format(root,design)
                WriteFilelist("./files_syn.fl",wdata)
                dir_path ="{}/{}.vh".format(work_dir,design)
                source_path="{}/{}.vh".format(root,design)
                os.system('cp {} {}'.format(source_path,dir_path))
script1_file_dir = "/home/IC/q/SynFlow.tcl"
script2_file_dir = "/home/IC/q/Sdc.tcl"
design_file_dir = "/home/IC/ridecore-master/src/fpga"
os.system('rm -rf ./rtl ./syn ./files_syn.fl ./WORK')
os.system('mkdir -p ./rtl ./syn/mapped ./syn/report ./syn/script ./syn/unmapped ./WORK ./syn/log')
CopyAndCreatFilelist(design_file_dir)
CopyScript()
os.system('cd WORK && dc_shell -f ../syn/script/SynFlow.tcl -gui -output_log_file ../syn/log/top_syn.log')
