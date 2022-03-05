Welcome to the LibreTime wiki! This contains the documentation useful for developers working on the LibreTime code. The [website](https://libretime.org) hosts all documentation related to using LibreTime and should be consulted if you wish to use LibreTime.

# Git

The LibreTime code is maintained using [git](https://git-scm.com). LibreTime uses [Github flow](https://guides.github.com/introduction/flow/) with topic branches. This wiki [[describes|Git Workflow]] how to use `git rebase` and `git commit --amend` to ensure that all topic branches are kept up to date with `master` and have a clean commit history.

# Codebase

LibreTime is a complicated platform and uses a variety of technologies and languages. Most of the interface and business logic is implemented in PHP using the [zf1s framework](https://github.com/zf1s). The back-end audio processing is written in [Python 3](https://python.org) and [liquidsoap](http://liquidsoap.fm) is used for stream and play-out management. Version 2 of the API is also written in Python using the [Django](https://www.djangoproject.com/) framework. The [[documentation|User Documentation]] is built using [Jekyll](https://jekyllrb.com/). This wiki includes a [[technical overview of LibreTime under the hood]]. It also tracks the [[supported distributions and software versions|Distro Packages]].

Updating the PHP dependencies is tricky because LibreTime supports PHP >=5.4. This is because CentOS 7 ships with PHP 5.4. When updating the PHP dependencies, developers must follow [[this guide|PHP Composer Update Procedure]].

This wiki also takes developers through proposing a change to the code base [[here|First Pull Prequest]].

# Testing Changes

LibreTime uses [pre-commit](https://pre-commit.com/) for managing linting and code-style checks. This is run on GitHub actions on every pull request and can be set up locally as described [[here|pre-commit]]. Test instances of LibreTime can be easily spun up using [Vagrant](https://www.vagrantup.com/). See the [[setup guide|Vagrant Developer Setup]] to get it set up and working.

There are [[unit tests|Testing LibreTime]] for some of the PHP and Python code and these are run in GitHub Actions on every pull request. [Xdebug](https://xdebug.org/) is also useful when working on the PHP code and can be enabled by following [[this guide|How To Enable Xdebug for LibreTime with PhpStorm]].
