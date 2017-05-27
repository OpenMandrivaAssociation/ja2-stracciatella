Name:           ja2-stracciatella
Version:        0.15.1
Release:        1
Summary:        Jagged Alliance 2 Stracciatella
License:        MIT
Group:          Games/Other
Url:            http://ja2-stracciatella.github.io/
Source:         https://github.com/ja2-stracciatella/ja2-stracciatella/archive/v0.15.1.tar.gz
BuildRequires:  pkgconfig(sdl)

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
%{_datadir}/ja2
%{_mandir}/man6/ja2.6.*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg
#---------------------------------------------------------

%prep
%setup -q

%build
#% configure2_5x
%cmake
%make

%install
sed -i "s|%{_prefix}|%{buildroot}%{_prefix}|" Makefile.config
%makeinstall_std
find %{buildroot} -size 0 -delete
chmod 0755 %{buildroot}%{_bindir}/ja2

%changelog

* Thu Apr 20 2017 abfonly <abfonly@gmail.com> 0.15.1-1
- (dad6cee) Imported from SRPM


