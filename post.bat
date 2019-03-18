@ECHO OFF
git subtree split --branch gh-pages --prefix docs/_build/html/
git checkout gh-pages
git push origin gh-pages --force
git checkout master
git branch -D gh-pages
