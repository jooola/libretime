This serves as a place to track what distro packages we need and what state they are in.

The main focus of this is list is that it contains the needed links to figure out where to get the package from and where it stands for a distro to maintain it.

In cases where distros already have a package we prefer to work with the existing upstream and try getting that bumped.

# Support Matrix

| Distro                | PHP           | Python | Liquidsoap                                                                                           | Silan                                                                                            | Works with LT                |
| --------------------- | ------------- | ------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------- |
| Debian 11 'Bullseye'  | 7.4 (Working) | 3.9    | 1.4.4 (Working)                                                                                      | 0.4.0 (Working)                                                                                  | Yes                          |
| Ubuntu 18.04 'Bionic' | 7.2 (Working) | 3.6    | 1.1.1-7.2u1 (Working)                                                                                | 0.3.3 (Working)                                                                                  | Yes                          |
| Ubuntu 20.04 'Groovy' | 7.4 (Working) | 3.8    | 1.4.1-1 (Working)                                                                                    | 0.4.0 (Working)                                                                                  | Yes                          |
| CentOS 8              | 7.3 (Working) | 3.6    | 1.3.7 (Untested, from [RaBe LSD](https://build.opensuse.org/project/show/home:radiorabe:liquidsoap)) | 0.4.0 (Untested, from [RaBe APEL](https://build.opensuse.org/project/show/home:radiorabe:audio)) | No (untested installer, etc) |

# [silan](https://github.com/x42/silan)

LibreTime Bugs: [~#177~](https://github.com/LibreTime/libretime/issues/177), [~#193~](https://github.com/LibreTime/libretime/issues/193), [~#197~](https://github.com/LibreTime/libretime/issues/197), [~#552~](https://github.com/LibreTime/libretime/issues/552)

|                         | Info                                                                                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Status                  | CentOS package should move to Nux Dextop since ffmpeg is from there                                                                                       |
| Debian<sup>1</sup>      | [PTS](https://tracker.debian.org/pkg/silan)                                                                                                               |
| Ubuntu<sup>1</sup>      | [launchpad](https://launchpad.net/ubuntu/+source/silan)                                                                                                   |
| 3rd party .deb          | [provisional libretime NMU build](https://github.com/LibreTime/libretime/issues/177#issuecomment-299195796), [sourcefabric](http://apt.sourcefabric.org/) |
| CentOS<sup>2</sup>      |                                                                                                                                                           |
| Fedora EPEL<sup>2</sup> |                                                                                                                                                           |
| 3rd party RPM           | [RaBe APEL](https://build.opensuse.org/package/show/home:radiorabe:audio/silan)                                                                           |

# [liquidsoap](http://liquidsoap.fm/)

LibreTime Bugs: [~#192~](https://github.com/LibreTime/libretime/issues/192)

|                         | Info                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Status                  | Needs an `ocaml-ssl` update on CentOS                                                    |
| Debian<sup>1</sup>      | [PTS](https://tracker.debian.org/pkg/liquidsoap)                                         |
| Ubuntu<sup>1</sup>      | [launchpad](https://tracker.debian.org/pkg/liquidsoap)                                   |
| 3rd party .deb          |
| CentOS<sup>2</sup>      |
| Fedora EPEL<sup>2</sup> |
| 3rd party RPM           | [RaBe LSD](https://build.opensuse.org/package/show/home:radiorabe:liquidsoap/liquidsoap) |

# [mutagen](https://github.com/quodlibet/mutagen)

|                         | Info                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| Status                  | Might have version conflict/need code updates                                                               |
| Debian<sup>1</sup>      | [PTS](https://tracker.debian.org/pkg/mutagen)                                                               |
| Ubuntu<sup>1</sup>      | [launchpad](https://launchpad.net/ubuntu/+source/mutagen)                                                   |
| 3rd party .deb          | -                                                                                                           |
| CentOS<sup>2</sup>      | [r-m.o](https://release-monitoring.org/project/3931/), [pkgs.org](https://pkgs.org/download/python-mutagen) |
| Fedora EPEL<sup>2</sup> | -                                                                                                           |
| 3rd party RPM           | -                                                                                                           |

---

<sup>1</sup> No link means there is no package available.

<sup>2</sup> No link means no package available. Once it is available it needs to be mapped to Fedora in https://release-monitoring.org/ for Fedora and Fedora EPEL. Once a package is in Fedora rawhide a epel7 branch can be requested for the package. All of this will understandably not get much traction unless a large RHEL customer decides to use LibreTime. Please look at the [libretime-rpm-packaging issues](https://github.com/LibreTime/libretime-rpm-packaging/issues) to get a current overview of the needed packages.
