git checkout backup-changes
git add .
git commit -m "automatic commit of deployment changes"
git push -u origin backup-changes
git fetch --all
git reset --hard origin/deploy
systemctl restart packpng.service
