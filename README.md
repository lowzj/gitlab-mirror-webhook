# gitlab-mirror-webhook
A docker image contains gitlab-ce, gitlab-mirrors and a simple github webhook web server

#### run docker image gitlab-ce

```sh
sh start-gitlab.sh
```

#### Clone the gitlab-mirrors repository and set values in config.sh.

```sh
sh build-mirror.sh
```

#### Modify gitlab-mirror's config.sh

Modify the values in `config.sh` for your setup.
Write the private token of the gitmirror GitLab user into `~/private_token` of
your `gitmirror` system user.

```ini
system_user="${your_system_user}"
repo_dir="${user_home}/apps/var/gitlab-mirror/repositories"
#This is the Gitlab group where all project mirrors will be grouped.
gitlab_namespace="${your_project_group}"
#This is the base web url of your Gitlab server.
gitlab_url="http://${your_gitlab_url}"
#Special user you created in Gitlab whose only purpose is to update mirror sites and admin the $gitlab_namespace group.
gitlab_user="root"
#Generate a token for your $gitlab_user and set it here.
gitlab_user_token_secret="$(head -n1 "${user_home}/apps/opt/gitlab-mirror/private_token" 2> /dev/null || echo "")"
```

#### Add github repo

```sh
cd gitlab-mirrors && ./add_mirror.sh --git --project-name YOUR_GITLAB_PROJECT_NAME --mirror YOUR_GITHUB_REPO_URL
```

#### Set webhook env

```sh
export GITLAB_MIRROR_WEBHOOK_SECRET=xxxx
export GITLAB_MIRROR_WORK_DIR=yyyy
```

#### Start webhook.py

```sh
sh start-webhook.py
```


