#!/bin/bash

GITLAB_CONFIG=/data/apps/config/gitlab
GITLAB_LOG=/data/apps/log/gitlab
GITLAB_DATA=/data/apps/var/gitlab

for i in $GITLAB_LOG $GITLAB_DATA $GITLAB_CONFIG; do
    test -d $i || mkdir -p $i
done

sudo docker run --detach \
    --net=host \
    --name gitlab \
    --restart always \
    --volume $GITLAB_CONFIG:/etc/gitlab \
    --volume $GITLAB_LOG:/var/log/gitlab \
    --volume $GITLAB_DATA:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
