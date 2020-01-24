sudo git stash push
sudo git fetch --all
sudo git reset --hard origin/deploy
sudo systemctl restart packpng.service
# requires the executing user to have nopasswd rights in sudoers ti commands git and systemctl