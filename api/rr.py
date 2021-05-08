"""
Created on Wed Jan 13 17:20:54 2021

@author: Anderson Ryen
"""

import os
#预览地址
view_path = "https://www.prlrr.com/prl/lxr/rr.php"
#文件的绝对路径
file_path_1 = "E:\\GitHub Desktop\\GitHub\\rr\\img\\"
#CDN前缀
web_path = "https://cdn.jsdelivr.net/gh/"
#GITHUB账户名
user_path = "anderson-ryen"
#仓库名
warehouse_path_1 = "rr"
#仓库内文件夹
img_path = "img"
#合并path
api_path_1 = os.path.join( web_path + user_path + "/" + warehouse_path_1 + "/" + img_path + "/")

print("")
print("效果预览: " + view_path)
print("=" *50)
print("rr-已完成")
print("=" *50)
print("")

if __name__ == '__main__':
    filelist = os.listdir(file_path_1)
    with open(r"E:\GitHub Desktop\GitHub\rr\api\rr.txt",'w') as f:
        for file in filelist:
            f.write(api_path_1+file+'\n')
