> Prerequisites: git, [Vagrant](https://vagrantup.com), libvirt or VirtualBox

## (Optional) Setup `apt-cacher-ng` on the host

In order to reduce the downloading time between each vagrant setup, you can install `apt-cacher-ng` on your host. The vagrant machine will automatically detect the apt proxy running on your host and will use it as cache.

If you encounter a `HTTP 502` error while downloading a package, please raise an issue on the bug tracker. See https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=986356 for more details.

## VirtualBox

You will need to install [VirtualBox](https://www.virtualbox.org) and may want to consider
installing [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) to update the
guest extensions to match your host system on vagrant up.
                                                    
```bash
vagrant plugin install vagrant-vbguest
```                          

## Libvirt                                                                                               
                                                                                                         
Setting the libvirt provider up on Ubuntu and Debian is straight-forward,
using the distribution provided packages. While on
other distributions it can be built from within vagrant.
                                                                                                         
If you try run a libvirt provided box after using a VirtualBox one, you will receive an
error:                  
                                                    
```
Error while activating network:                                                                          
Call to virNetworkCreate failed: internal error: Network is already in use by interface vboxnet0.
```
                                                                                                         
This is fixed by stopping virtualbox and re-creating the vagrant box:                  
                                                    
```
sudo systemctl stop virtualbox 
vagrant destroy ubuntu-xenial
vagrant up ubuntu-xenial --provider=libvirt                                                              
```                                                                                                      

### Debian and Ubuntu                                                                                                                                                                                             
                                                                                                                                                                                                                  
```bash                                                                                                                                                                                                           
sudo apt install vagrant vagrant-libvirt libvirt-daemon-system vagrant-mutate libvirt-dev                                                                                                                         
sudo usermod -aG libvirt $USER                                                                                                                                                                                    
                                                                                                                                                                                                                  
# Reboot                                                                                                                                                                                                          

vagrant box add bento/ubuntu-16.04 --provider=virtualbox
vagrant mutate bento/ubuntu-16.04 libvirt
vagrant up ubuntu-xenial --provider=libvirt                                                              
```                     

### Other Distributions
                                                    
You will need to install [libvirt](https://libvirt.org/) and `vagrant-mutate` and then run                                                                                                                        

```bash
vagrant plugin install vagrant-libvirt
sudo usermod -a -G libvirt $USER

# Reboot

vagrant plugin install vagrant-mutate
vagrant box fetch bento/ubuntu-16.04
vagrant mutate bento/ubuntu-16.04 libvirt
vagrant up ubuntu-xenial --provider=libvirt
```

## Starting LibreTime Vagrant

To get started you clone the repo and run `vagrant up`. The command accepts a parameter to
change the default provider if you have multiple installed. This can be done by appending
`--provider=virtualbox` or `--provider=libvirt` as applicable.

```bash
git clone https://github.com/libretime/libretime.git 
cd libretime
vagrant up ubuntu-xenial
```

If everything works out, you will find LibreTime on [port 8080](http://localhost:8080)
and Icecast on [port 8000](http://localhost:8000).

Before provisioning, you may tweak the following options according to your needs:

```sh
# Disable port forwarding, ports will only be accessible at 192.168.10.100:* and not on localhost:*.
# This can help reduce ports conflicts with existing services using these ports.
export VAGRANT_NO_PORT_FORWARDING=true

# Increase CPU count or dedicated memory for the vagrant virtual machine. 
export VAGRANT_CPUS=4
export VAGRANT_MEMORY=4096
vagrant up debian-buster
```

Once you reach the web setup GUI you can click through it using the default values. To
connect to the vagrant machine you can run `vagrant ssh ubuntu-xenial` in the libretime
directory.

## Alternative OS installations

With the above instructions LibreTime is installed on Ubuntu Xenial Xerus. The Vagrant setup
offers the option to choose a different operation system according to you needs.

| OS           | Command                     | Comment                                                     |
| ------------ | --------------------------- | ----------------------------------------------------------- |
| Debian 10    | `vagrant up debian-buster`  | Install on Debian Buster.                                   |
| Debian 9     | `vagrant up debian-stretch` | Install on current Debian Stretch.                          |
| Ubuntu 18.04 | `vagrant up ubuntu-bionic`  | Install on current Ubuntu Bionic Beaver.                    |
| Ubuntu 16.04 | `vagrant up ubuntu-xenial`  | Install on Ubuntu Xenial Xerus.                             |
| CentOS       | `vagrant up centos`         | CentOS 8 with native systemd support and activated SELinux. |

## Troubleshooting

If anything fails during the initial provisioning step you can try running `vagrant provision`
to re-run the installer.

If you only want to re-run parts of the installer, use `--provision-with $step`. The
supported steps are `prepare` and `install`.