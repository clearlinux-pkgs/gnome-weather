#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-weather
Version  : 3.32.1
Release  : 10
URL      : https://download.gnome.org/sources/gnome-weather/3.32/gnome-weather-3.32.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-weather/3.32/gnome-weather-3.32.1.tar.xz
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
BuildRequires : libgweather-dev

%description
No detailed description available

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
%setup -q -n gnome-weather-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554485536
export LDFLAGS="${LDFLAGS} -fno-lto"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-weather
cp COPYING.md %{buildroot}/usr/share/package-licenses/gnome-weather/COPYING.md
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
/usr/share/package-licenses/gnome-weather/COPYING.md

%files locales -f org.gnome.Weather.lang
%defattr(-,root,root,-)

