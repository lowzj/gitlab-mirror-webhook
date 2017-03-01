#!/bin/bash

home=`dirname $0`

nohup python $home/../webhook.py 8081 >> /data/apps/log/gitlab-mirror/webhook.log 2>&1 &
