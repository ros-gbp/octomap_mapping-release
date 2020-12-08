%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-octomap-server
Version:        0.6.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS octomap_server package

License:        BSD
URL:            http://www.ros.org/wiki/octomap_server
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-octomap
Requires:       ros-noetic-octomap-msgs
Requires:       ros-noetic-octomap-ros
Requires:       ros-noetic-pcl-conversions
Requires:       ros-noetic-pcl-ros
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-octomap
BuildRequires:  ros-noetic-octomap-msgs
BuildRequires:  ros-noetic-octomap-ros
BuildRequires:  ros-noetic-pcl-conversions
BuildRequires:  ros-noetic-pcl-ros
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
octomap_server loads a 3D map (as Octree-based OctoMap) and distributes it to
other nodes in a compact binary format. It also allows to incrementally build 3D
OctoMaps, and provides map saving in the node octomap_saver.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Dec 08 2020 Wolfgang Merkt <opensource@wolfgangmerkt.com> - 0.6.6-1
- Autogenerated by Bloom

* Thu Apr 23 2020 Wolfgang Merkt <opensource@wolfgangmerkt.com> - 0.6.5-1
- Autogenerated by Bloom

