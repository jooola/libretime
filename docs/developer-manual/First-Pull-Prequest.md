This guide explains how to clone LibreTime, make changes and test them. The changes can then be submitted back to LibreTime as a pull request for inclusion into LibreTime's code base.

1. Fork LibreTime to your GitHub profile by clicking on the **Fork** button on https://github.com/LibreTime/libretime
1. Clone the git repo to your local computer and create a branch for your changes
```bash
git clone git@github.com/<your username>/libretime.git
cd libretime
git checkout -b <feature_branch>
```
1. Make your changes to the code
1. Review your changes and test them using [[vagrant|Vagrant Developer Setup]]
```bash
vagrant up ubuntu-bionic
vagrant ssh ubuntu-bionic
```
1. Configure [[ pre-commit ]]
1. Stage your files, commit them and push to your branch
```bash
git add .
git commit -m '<clear and concise description of the changes made>'
git push origin <feature_branch>
```
1. Open a pull request by going to https://github.com/LibreTime/libretime/pulls