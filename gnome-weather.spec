#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-weather
Version  : 44.0
Release  : 24
URL      : https://download.gnome.org/sources/gnome-weather/44/gnome-weather-44.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-weather/44/gnome-weather-44.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-weather-bin = %{version}-%{release}
Requires: gnome-weather-data = %{version}-%{release}
Requires: gnome-weather-license = %{version}-%{release}
Requires: gnome-weather-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : geoclue-dev
BuildRequires : gjs-dev
BuildRequires : pkgconfig(gjs-1.0)
BuildRequires : pkgconfig(gweather4)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libgeoclue-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Weather
Monitor the current weather conditions for your city, or anywhere in the world.

%package bin
Summary: bin components for the gnome-weather package.
Group: Binaries
Requires: gnome-weather-data = %{version}-%{release}
Requires: gnome-weather-license = %{version}-%{release}

%description bin
bin components for the gnome-weather package.


%package data
Summary: data components for the gnome-weather package.
Group: Data

%description data
data components for the gnome-weather package.


%package license
Summary: license components for the gnome-weather package.
Group: Default

%description license
license components for the gnome-weather package.


%package locales
Summary: locales components for the gnome-weather package.
Group: Default

%description locales
locales components for the gnome-weather package.


%prep
%setup -q -n gnome-weather-44.0
cd %{_builddir}/gnome-weather-44.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679693561
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-weather
cp %{_builddir}/gnome-weather-%{version}/COPYING.md %{buildroot}/usr/share/package-licenses/gnome-weather/323be5b629b728c08f2c9a998725c4584f97fb18 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang org.gnome.Weather

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-weather

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Weather.desktop
/usr/share/dbus-1/services/org.gnome.Weather.BackgroundService.service
/usr/share/dbus-1/services/org.gnome.Weather.service
/usr/share/glib-2.0/schemas/org.gnome.Weather.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Weather.svg
/usr/share/icons/hicolor/scalable/status/temperature-symbolic.svg
/usr/share/icons/hicolor/scalable/status/weather-clear-large.svg
/usr/share/icons/hicolor/scalable/status/weather-clear-night-large.svg
/usr/share/icons/hicolor/scalable/status/weather-clear-night-small.svg
/usr/share/icons/hicolor/scalable/status/weather-clear-small.svg
/usr/share/icons/hicolor/scalable/status/weather-few-clouds-large.svg
/usr/share/icons/hicolor/scalable/status/weather-few-clouds-night-large.svg
/usr/share/icons/hicolor/scalable/status/weather-few-clouds-night-small.svg
/usr/share/icons/hicolor/scalable/status/weather-few-clouds-small.svg
/usr/share/icons/hicolor/scalable/status/weather-fog-large.svg
/usr/share/icons/hicolor/scalable/status/weather-fog-small.svg
/usr/share/icons/hicolor/scalable/status/weather-hourly-symbolic.svg
/usr/share/icons/hicolor/scalable/status/weather-overcast-large.svg
/usr/share/icons/hicolor/scalable/status/weather-overcast-small.svg
/usr/share/icons/hicolor/scalable/status/weather-severe-alert-large.svg
/usr/share/icons/hicolor/scalable/status/weather-severe-alert-small.svg
/usr/share/icons/hicolor/scalable/status/weather-showers-large.svg
/usr/share/icons/hicolor/scalable/status/weather-showers-scattered-large.svg
/usr/share/icons/hicolor/scalable/status/weather-showers-scattered-small.svg
/usr/share/icons/hicolor/scalable/status/weather-showers-small.svg
/usr/share/icons/hicolor/scalable/status/weather-snow-large.svg
/usr/share/icons/hicolor/scalable/status/weather-snow-small.svg
/usr/share/icons/hicolor/scalable/status/weather-storm-large.svg
/usr/share/icons/hicolor/scalable/status/weather-storm-small.svg
/usr/share/icons/hicolor/scalable/status/weather-tornado-large.svg
/usr/share/icons/hicolor/scalable/status/weather-tornado-small.svg
/usr/share/icons/hicolor/scalable/status/weather-windy-large.svg
/usr/share/icons/hicolor/scalable/status/weather-windy-small.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Weather-symbolic.svg
/usr/share/metainfo/org.gnome.Weather.appdata.xml
/usr/share/org.gnome.Weather/org.gnome.Weather
/usr/share/org.gnome.Weather/org.gnome.Weather.BackgroundService
/usr/share/org.gnome.Weather/org.gnome.Weather.BackgroundService.data.gresource
/usr/share/org.gnome.Weather/org.gnome.Weather.BackgroundService.src.gresource
/usr/share/org.gnome.Weather/org.gnome.Weather.data.gresource
/usr/share/org.gnome.Weather/org.gnome.Weather.src.gresource

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-weather/323be5b629b728c08f2c9a998725c4584f97fb18

%files locales -f org.gnome.Weather.lang
%defattr(-,root,root,-)

