This is a set of working instructions for Ubuntu Trusty - we will probably enable this for other distributions or in vagrant and PHP-Storm (should work similar for Eclipse or others)

First install xdebug extension via apt
`apt-get install php5-xdebug`

Next modify the xdebug.ini file 
`sudo nano /etc/php5/apache2/conf.d/20-xdebug.ini`

Add the following to the end of the file after zend_extension=xdebug.so
xdebug.idekey=PHPSTORM
xdebug.remote_autostart=1
xdebug.remote_enable=1
xdebug.remote_connect_back = on

Restart apache via init.d or systemd or upstart (below works on ubuntu-trusty)
sudo /etc/init.d/apache2 reload

And it should work if you setup code breaks with xdebug_break() and have PhpStorm configured to listen