#!/bin/bash

VERSION=$(python3 setup.py --version)
echo "update version number in setup.py first!"

git add -u
git commit -m "Version $VERSION release"
git tag $VERSION -m "Version $VERSION"
git push --tags
python setup.py sdist upload -r pypi
sudo pip3 install hiplogging  --upgrade
python3 example.py
