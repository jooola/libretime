# Checking Installation

Check your version of silan by running `silan --version`. This should report `0.3.3` or higher.

If you are on Debian or Ubuntu, run `sudo dpkg -s silan | awk '/Version/ {print $2}'` to show the exact package version you installed. Please include this information if you file bugs concerning silan.

There are multiple workarounds to get silan 0.3.0 or higher. Currently the silan package is in Debian Buster (Ubuntu 18.04) and above as can be seen in the [Debian PTS](https://tracker.debian.org/pkg/silan).

If you are running something older, you should re-install silan from a source you trust. If your distro has not updated to 0.3.3 yet you should also help by asking your distros maintainers for a bump.

The following solutions have been reported to work. If they do not work, please note that it is your responsibility to get working silan packages.

# Workarounds

## LibreTime PPA

Works for all relevant Ubuntu releases and installs silan `0.4.0-1ltppa2`

```bash
sudo add-apt-repository ppa:libretime/libretime
sudo apt-get update
sudo apt-get install silan
```

## Silan from OBS build ([#177 (comment)](https://github.com/LibreTime/libretime/issues/177#issuecomment-299195796))

Works for all relevant Debian and Ubuntu distros and installs silan `0.3.3~nmu1`.

```bash
# install package signing key from obs
wget -qO- http://download.opensuse.org/repositories/home:/hairmare:/silan/Debian_7.0/Release.key \
  | apt-key add -

# add OBS repo to sources list (pick the distro you need)

# Debian Stretch
echo 'deb http://download.opensuse.org/repositories/home:/hairmare:/silan/Debian_9.0_standard/ ./' \
  > /etc/apt/sources.list.d/hairmare_silan.list
# Debian Jessie
echo 'deb http://download.opensuse.org/repositories/home:/hairmare:/silan/Debian_8.0 ./' \
  > /etc/apt/sources.list.d/hairmare_silan.list
# Ubuntu Xenial
echo 'deb http://download.opensuse.org/repositories/home:/hairmare:/silan/xUbuntu_16.04 ./' \
  > /etc/apt/sources.list.d/hairmare_silan.list

# update local package database
apt-get update

# install silan 0.3.3 from obs packages
apt-get install silan
```

## Local armhf builds for Raspberry Pi 3 ([#214 (comment)](https://github.com/LibreTime/libretime/issues/214#issuecomment-305988355))

Since build.opensuse.org can't build Debian packages on arm due to missing dependencies, the `0.3.3~nmu1` arm package was built in a docker crossdev environment. This is reported to work on Debian Jessie on a Raspberry Pi 3 Model B.

```bash
curl -L -O https://github.com/LibreTime/libretime/files/1049738/silan_0.3.3.nmu1_armhf.deb.tar.gz
tar xvf silan_0.3.3.nmu1_armhf.deb.tar.gz
sudo dpkg -i silan_0.3.3~nmu1_armhf.deb
```

## Legacy upstream silan packages ([#197](https://github.com/LibreTime/libretime/issues/197))

Legacy upstream hosts patched packages for Ubuntu Trusty on `apt.sourcefabric.org`. They install as `0.3.2~trusty~sfo-1`.

```bash
sudo tee -a /etc/apt/sources.list <<EOD
deb http://apt.sourcefabric.org/ trusty main
EOD

sudo apt-get update
sudo apt-get install sourcefabric-keyring
sudo apt-get update
sudo apt-get install --reinstall silan=0.3.2~trusty~sfo-1
```

## Remove silan completely ([#193 (comment)](https://github.com/LibreTime/libretime/issues/193#issuecomment-299174997))

It is worth mentioning that you can disable cue point detection by removing silan from the system.

```bash
sudo apt-get uninstall silan
```

Reportedly this might have [side effects](https://github.com/LibreTime/libretime/issues/214#issuecomment-305748757).
