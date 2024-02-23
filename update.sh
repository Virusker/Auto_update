#!/bin/bash

cd app/test/
git pull  # hoặc branch bạn đang sử dụng
#systemctl restart your_app.service  # khởi động lại ứng dụng
sudo supervisorctl restart app

sudo supervisorctl status app