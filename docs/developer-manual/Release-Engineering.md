Most time in RelEng is currently spent on the release notes. I also keep an eye on stability and try to not cut a buggy release and do some manual cross distro testing before each release.

Once the release notes are ready and I'm confident that everything looks good there are some last minute changes to be done on the release notes like adding emojis to the Colophon part and removing any draft warnings.

The actual release is done through the GitHub web interface by clicking the green publish button. Once the release has been published, the binary is created automatically by GitHub Actions and added to the release notes.

## Debian packaging

- See the [libretime-debian-packaging repository](https://github.com/LibreTime/libretime-debian-packaging).

## RPM packaging

- Is currently done on the _unsupported_ OBS [home:radiorabe:airtime OBS repo](https://build.opensuse.org/project/show/home:radiorabe:airtime).
