%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname KPimAddressbookImportExport 5
%define devname %mklibname -d KPimAddressbookImportExport

Summary:	KDE addressbook application
Name:		kaddressbook
Version:	22.08.2
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5KaddressbookImportExport)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:	grantlee-editor
Requires:	akonadi-common
Requires:	kdepim-runtime
Suggests:	kdepim-addons

%description
KDE addressbook application.

%files -f %{name}.lang
%{_kde5_applicationsdir}/kaddressbook-importer.desktop
%{_kde5_applicationsdir}/org.kde.kaddressbook.desktop
%{_bindir}/kaddressbook
%dir %{_kde5_datadir}/kaddressbook/
%{_datadir}/kaddressbook/*
%{_iconsdir}/hicolor/*/apps/kaddressbook.*
%{_datadir}/qlogging-categories5/kaddressbook.categories
%{_datadir}/qlogging-categories5/kaddressbook.renamecategories
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_qt5_plugindir}/kaddressbookpart.so
%{_datadir}/applications/kaddressbook-view.desktop
%{_libdir}/qt5/plugins/pim5/kcms/kaddressbook/kaddressbook_config_plugins.so
%{_libdir}/qt5/plugins/pim5/kcms/kaddressbook/kaddressbook_config_userfeedback.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_kaddressbookplugin.so

#----------------------------------------------------------------------------

%define kaddressbookprivate_major 5
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE PIM shared library.

%files -n %{libkaddressbookprivate}
%{_kde5_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for address book import/export
Group:		System/Libraries

%description -n %{libname}
KDE PIM address book shared library.

%files -n %{libname}
%{_libdir}/libKPimAddressbookImportExport.so.5*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for the address book import/export library
Group:		Development/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Headers for the address book import/export library

%files -n %{devname}
%{_libdir}/libKPimAddressbookImportExport.so
%{_includedir}/KPim/KAddressBookImportExport
%{_includedir}/KPim/kaddressbookimportexport
%{_includedir}/KPim/kaddressbookimportexport_version.h
%{_libdir}/cmake/KPimAddressbookImportExport
%{_libdir}/qt5/mkspecs/modules/qt_KAddressbookImportExport.pri

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
