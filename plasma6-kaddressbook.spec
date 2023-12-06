%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define oldlibname %mklibname KPimAddressbookImportExport 6
%define olddevname %mklibname -d KPimAddressbookImportExport
%define libname %mklibname KPim6AddressbookImportExport
%define devname %mklibname -d KPim6AddressbookImportExport

Summary:	KDE addressbook application
Name:		plasma6-kaddressbook
Version:	24.01.80
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kaddressbook-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
Requires:	grantlee-editor
Requires:	akonadi-common
Requires:	kdepim-runtime
Suggests:	kdepim-addons

%description
KDE addressbook application.

%files -f %{name}.lang
%{_datadir}/applications/kaddressbook-importer.desktop
%{_datadir}/applications/org.kde.kaddressbook.desktop
%{_bindir}/kaddressbook
%dir %{_datadir}/kaddressbook/
%{_datadir}/kaddressbook/*
%{_iconsdir}/hicolor/*/apps/kaddressbook.*
%{_datadir}/qlogging-categories6/kaddressbook.categories
%{_datadir}/qlogging-categories6/kaddressbook.renamecategories
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_qtdir}/plugins/kaddressbookpart.so
%{_datadir}/applications/kaddressbook-view.desktop
%{_qtdir}/plugins/pim6/kcms/kaddressbook/kaddressbook_config_plugins.so
%{_qtdir}/plugins/pim6/kcms/kaddressbook/kaddressbook_config_userfeedback.so
%{_qtdir}/plugins/pim6/kontact/kontact_kaddressbookplugin.so

#----------------------------------------------------------------------------

%define kaddressbookprivate_major 6
%define oldlibkaddressbookprivate %mklibname kaddressbookprivate 6
%define libkaddressbookprivate %mklibname kaddressbookprivate

%package -n %{libkaddressbookprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries
%rename %{oldlibkaddressbookprivate}

%description -n %{libkaddressbookprivate}
KDE PIM shared library.

%files -n %{libkaddressbookprivate}
%{_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*
%{_libdir}/libkaddressbookprivate.so.5*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for address book import/export
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
KDE PIM address book shared library.

%files -n %{libname}
%{_libdir}/libKPim6AddressbookImportExport.so.6*
%{_libdir}/libKPim6AddressbookImportExport.so.5*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for the address book import/export library
Group:		Development/Libraries
Requires:	%{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Headers for the address book import/export library

%files -n %{devname}
%{_libdir}/libKPim6AddressbookImportExport.so
%{_includedir}/KPim6/KAddressBookImportExport
%{_libdir}/cmake/KPim6AddressbookImportExport

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kaddressbook-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
