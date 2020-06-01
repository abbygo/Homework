import os


# 根目录
base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

log_dir=os.path.join(base_dir, "outputs", 'logs')
report_path=os.path.join(base_dir,"outputs",'reports')
screenshot_root_dir=os.path.join(base_dir,"outputs",'screenshots')
data_dir=os.path.join(base_dir,"testdata")
video_dir=os.path.join(base_dir,"outputs",'video')
page_path=os.path.join(base_dir,"page")






