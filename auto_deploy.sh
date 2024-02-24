#!/bin/bash
echo $2
cd $2
export HOME=/home
/usr/bin/git config --global --add safe.directory '*'

/usr/bin/git pull  # hoặc branch bạn đang sử dụng
#systemctl restart your_app.service  # khởi động lại ứng dụng

sudo /usr/bin/systemctl restart $1