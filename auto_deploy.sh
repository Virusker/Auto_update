#!/bin/bash
echo $2
cd $2
/usr/bin/git config --global --add safe.directory $2
/usr/bin/git pull  # hoặc branch bạn đang sử dụng
#systemctl restart your_app.service  # khởi động lại ứng dụng

systemctl restart $1