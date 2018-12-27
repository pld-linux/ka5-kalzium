%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kalzium
Summary:	Kalzium
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	dda62cded08b6246e574166ee9f4679b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel >= 5.42.0
BuildRequires:	kf5-kconfig-devel >= 5.42.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.42.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.42.0
BuildRequires:	kf5-kdoctools-devel >= 5.42.0
BuildRequires:	kf5-khtml-devel >= 5.42.0
BuildRequires:	kf5-ki18n-devel >= 5.42.0
BuildRequires:	kf5-kparts-devel >= 5.42.0
BuildRequires:	kf5-kplotting-devel >= 5.42.0
BuildRequires:	kf5-kunitconversion-devel >= 5.42.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.42.0
BuildRequires:	kf5-solid-devel >= 5.42.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kalzium is your digital replacement for the periodic table on paper.
It is a program that visualizes the Periodic Table of Elements (PSE)
and includes basic information about all common elements in the PSE.
It has a gained much more functions over time.

Features

- versatile overview of all important data from the elements like
  melting points, electron affinity, electronegativity, electron
  configuration, radii, mass, ionisation energy
- tool to visualize the spectral lines of each element
- different colored views of the PSE: separation of the different
  blocks, Year simulator, Temperature simulator
- Molecular weight calculator
- an Isotope table
- 3D molecule editor, with a load and save functionality
- an equation solver for stoichiometric problems
- filetype conversion for different types of chemical programs
- tool to produce a comprehensive list of all
  Risk_and_Safety_Statements

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kalzium.knsrc
%attr(755,root,root) %{_bindir}/kalzium
%attr(755,root,root) %ghost %{_libdir}/libscience.so.5
%attr(755,root,root) %{_libdir}/libscience.so.*.*.*
%{_desktopdir}/org.kde.kalzium.desktop
%{_desktopdir}/org.kde.kalzium_cml.desktop
%{_datadir}/config.kcfg/kalzium.kcfg
%{_iconsdir}/hicolor/128x128/apps/kalzium.png
%{_iconsdir}/hicolor/16x16/apps/kalzium.png
%{_iconsdir}/hicolor/22x22/apps/kalzium.png
%{_iconsdir}/hicolor/32x32/apps/kalzium.png
%{_iconsdir}/hicolor/48x48/apps/kalzium.png
%{_iconsdir}/hicolor/64x64/apps/kalzium.png
%{_iconsdir}/hicolor/scalable/apps/kalzium.svgz
%{_datadir}/kalzium
%dir %{_datadir}/kxmlgui5/kalzium
%{_datadir}/kxmlgui5/kalzium/kalziumui.rc
%dir %{_datadir}/libkdeedu
%dir %{_datadir}/libkdeedu/data
%{_datadir}/libkdeedu/data/elements.xml
%{_datadir}/libkdeedu/data/isotopes.xml
%{_datadir}/libkdeedu/data/spectra.xml
%{_datadir}/libkdeedu/data/symbols.csv
%{_datadir}/libkdeedu/data/symbols2.csv
%lang(ca) %{_mandir}/ca/man1/kalzium.1*
%lang(da) %{_mandir}/da/man1/kalzium.1*
%lang(de) %{_mandir}/de/man1/kalzium.1*
%lang(es) %{_mandir}/es/man1/kalzium.1*
%lang(et) %{_mandir}/et/man1/kalzium.1*
%lang(fr) %{_mandir}/fr/man1/kalzium.1*
%lang(gl) %{_mandir}/gl/man1/kalzium.1*
%lang(it) %{_mandir}/it/man1/kalzium.1*
%{_mandir}/man1/kalzium.1*
%lang(nl) %{_mandir}/nl/man1/kalzium.1*
%lang(pl) %{_mandir}/pl/man1/kalzium.1*
%lang(pt) %{_mandir}/pt/man1/kalzium.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kalzium.1*
%lang(ru) %{_mandir}/ru/man1/kalzium.1*
%lang(sv) %{_mandir}/sv/man1/kalzium.1*
%lang(uk) %{_mandir}/uk/man1/kalzium.1*
%{_datadir}/metainfo/org.kde.kalzium.appdata.xml

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/libkdeedu
%{_includedir}/libkdeedu/chemicaldataobject.h
%{_includedir}/libkdeedu/element.h
%{_includedir}/libkdeedu/elementparser.h
%{_includedir}/libkdeedu/isotope.h
%{_includedir}/libkdeedu/isotopeparser.h
%{_includedir}/libkdeedu/libkdeedu_science_export.h
%{_includedir}/libkdeedu/moleculeparser.h
%{_includedir}/libkdeedu/parser.h
%{_includedir}/libkdeedu/psetables.h
%{_includedir}/libkdeedu/spectrum.h
%{_includedir}/libkdeedu/spectrumparser.h
%attr(755,root,root) %{_libdir}/libscience.so
