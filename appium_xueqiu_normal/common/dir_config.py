import os


# 根目录
base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

caps_dir=os.path.join(base_dir,"Desired_Caps")
log_dir=os.path.join(base_dir, "Outputs", 'logs')
report_path=os.path.join(base_dir,"Outputs",'reports')
screenshot_root_dir=os.path.join(base_dir,"outputs",'screenshots')






