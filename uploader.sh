
echo "start git uploader"

git add *
git commit

git remote remove origin
git remote add origin 

git push -u origin main


echo "finish git uploader"

