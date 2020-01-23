git stash push
git fetch --all
git reset --hard origin/deploy
systemctl restart packpng.service
