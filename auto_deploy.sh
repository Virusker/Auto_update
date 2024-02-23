#!/bin/bash

cd $2
git pull  # hoặc branch bạn đang sử dụng
#systemctl restart your_app.service  # khởi động lại ứng dụng
sudo supervisorctl restart $1

sudo supervisorctl status $1