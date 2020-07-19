%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE addressbook application
Name:		kaddressbook
Version:	20.07.80
Release:	1
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
%{_datadir}/kconf_update/kaddressbook*
%dir %{_kde5_datadir}/kaddressbook/
%{_datadir}/kaddressbook/*
%{_datadir}/kontact/ksettingsdialog/kaddressbook.setdlg
%{_iconsdir}/hicolor/*/apps/kaddressbook.*
%{_kde5_services}/kaddressbook_config_plugins.desktop
%{_kde5_services}/kaddressbook_config_userfeedback.desktop
%{_kde5_services}/kontact/kaddressbookplugin.desktop
%{_datadir}/qlogging-categories5/kaddressbook.categories
%{_datadir}/qlogging-categories5/kaddressbook.renamecategories
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_qt5_plugindir}/kaddressbook_config_plugins.so
%{_qt5_plugindir}/kaddressbook_config_userfeedback.so
%{_qt5_plugindir}/kaddressbookpart.so
%{_qt5_plugindir}/kontact5/kontact_kaddressbookplugin.so
%{_datadir}/applications/kaddressbook-view.desktop

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

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
