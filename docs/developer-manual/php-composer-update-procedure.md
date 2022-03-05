LibreTime uses [composer](http://getcomposer.org) to manage PHP dependencies. Composer automatically resolves and downloads the right versions of dependencies based on the system it is running on and the `composer.json` list of required dependencies. It uses a `composer.lock` file to specify exactly which versions of dependencies to use to ensure that everyone is using the same versions of the dependencies. Many dependencies latest versions drop PHP 5.x support because it is no longer supported upstream. CentOS ships and still supports PHP 5.4. This is why LibreTime still supports PHP 5.4.

When an update is required to one of the dependencies (e.g. moving to `dev-master` to include a fix submitted upstream), only that dependency should be updated in the lock file. This is done by creating a CentOS vagrant box, updating the dependency and committing the `composer.lock` file. The CentOS box is used because this ensures compatibility with PHP >=5.4

```bash
vagrant up centos
vagrant ssh centos
cd /vagrant/legacy
composer update <package>
exit
git add composer.lock
git commit -m 'update php dependencies'
```

This should be done as part of any PR that changes `composer.json`
