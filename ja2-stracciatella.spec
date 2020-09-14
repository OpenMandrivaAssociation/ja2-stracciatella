Name:           ja2-stracciatella
Version:	0.17.0
Release:	1
Summary:        Jagged Alliance 2 Stracciatella
License:        MIT
Group:          Games/Other
Url:            http://ja2-stracciatella.github.io/
Source0:	https://github.com/ja2-stracciatella/ja2-stracciatella/archive/v%{version}.tar.gz
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  cmake(RapidJSON)
BuildRequires:  cmake
BuildRequires:  cargo
BuildRequires:  fltk-fluid
BuildRequires:  fltk-devel
BuildRequires:  boost-devel

%description
The goal of the project was to make
Jagged Alliance 2 available on a wide
range of platforms,
improve its stability,
fix bugs and provide a stable
platform for mod development

Edit the ~/.ja2/ja2.ini and set
parameter data_dir to point on the
directory where the original
game was installed.

If you installed not English version of
the original game, but one of the localized varieties,
you need to start the game with the appropriate
parameter, e.g. ja2 -resversion ITALIAN.

%files
%doc *.txt *.md
%{_bindir}/ja2
%{_bindir}/ja2-launcher
%{_bindir}/ja2-resource-pack
#% {_libdir}/libstracciatella.so
%{_datadir}/ja2
%{_mandir}/man6/ja2.6.*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg
#---------------------------------------------------------

%prep
%autosetup -p1
rm -rf dependencies/lib-gtest
rm -rf dependencies/lib-boost
rm -rf dependencies/lib-SDL*

%build
mkdir build
pushd build
cmake -DINSTALL_LIB_DIR=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DLOCAL_GTEST_LIB=OFF \
	-DWITH_UNITTESTS=OFF \
	-DLOCAL_RAPIDJSON_LIB=ON \
	-DEXTRA_DATA_DIR=%{_datadir}/ja2 ../

%make_build

%install
%makeinstall_std -C build
find %{buildroot} -size 0 -delete
chmod 0755 %{buildroot}%{_bindir}/ja2
