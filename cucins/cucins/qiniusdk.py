# -*- coding: utf-8 -*-

from cucins import app
from qiniu import Auth, put_stream, put_data, put_file
import os

#上传图片到七牛云（主要是免费）

#需要填写你的 Access Key 和 Secret Key
access_key = app.config['QINIU_ACCESS_KEY']
secret_key = app.config['QINIU_SECRET_KEY']

q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = app.config['QINIU_BUCKET_NAME']
save_dir = app.config['UPLOAD_DIR']
domain_prefix = app.config['QINIU_DOMAIN']

def qiniu_upload_file(source_file, save_file_name):
    # 生成上传Token，可以指定过期时间等
    token = q.upload_token(bucket_name, save_file_name)
    source_file.save(os.path.join(save_dir, save_file_name))# 图片存在本地

    ret, info = put_file(token, save_file_name, os.path.join(save_dir, save_file_name)) 
    print (os.getcwd() )
    os.remove("cucins\\upload\\"+save_file_name)#删除存在本地的图片
    #ret, info = put_data(token, save_file_name, source_file.stream)

    if(info.status_code == 200):
        return 'http://'+domain_prefix +'/'+ save_file_name
    else:
        return None







