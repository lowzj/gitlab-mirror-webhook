#!/bin/bash

pip show gitlab3 || sudo pip install gitlab3

data=/data/apps/var/gitlab-mirror/repositories
log=/data/apps/log/gitlab-mirror

for i in $data $log; do
  test -d $i || mkdir -p $i
done

touch private_token

git clone https://github.com/samrocketman/gitlab-mirrors.git
cd gitlab-mirrors
chmod 755 *.sh
cp config.sh.SAMPLE config.sh
