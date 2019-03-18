@ECHO OFF
git subtree split --branch gh-pages --prefix docs/_build/html/
git push origin gh-pages:gh-pages --force
