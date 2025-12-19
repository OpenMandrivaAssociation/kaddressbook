#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define oldlibname %mklibname KPimAddressbookImportExport 6
%define olddevname %mklibname -d KPimAddressbookImportExport
%define libname %mklibname KPim6AddressbookImportExport
%define devname %mklibname -d KPim6AddressbookImportExport

Summary:	KDE addressbook application
Name:		kaddressbook
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kaddressbook/-/archive/%{gitbranch}/kaddressbook-%{gitbranchd}.tar.bz2#/kaddressbook-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kaddressbook-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(KPim6LdapWidgets)
BuildRequires:	cmake(KPim6PimCommonActivities)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6TextAddonsWidgets)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	gettext
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)

%rename plasma6-kaddressbook

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
%{_qtdir}/plugins/pim6/kcms/kaddressbook/kaddressbook_config_activities.so
%{_qtdir}/plugins/pim6/kcms/kaddressbook/kaddressbook_config_ldap.so
%{_qtdir}/plugins/pim6/kontact/kontact_kaddressbookplugin.so
# No need for a libpackage with private libs that don't even have headers.
# Besides they conflict with P5
%{_libdir}/libkaddressbookprivate.so*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for address book import/export
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
KDE PIM address book shared library.

%files -n %{libname}
%{_libdir}/libKPim6AddressbookImportExport.so.6*

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
