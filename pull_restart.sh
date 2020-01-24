git stash push
git fetch --all
git reset --hard origin/deploy
sudo systemctl restart packpng.service
