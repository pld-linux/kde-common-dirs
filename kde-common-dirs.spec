#
Summary:	K Desktop Environment - common directories
Name:		kde-common-dirs
Version:	0.1
Release:	1
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	acaa37e79e840d10dca326277a20863c
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE3 & KDE4 common directories.


%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d \
    $RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
    $RPM_BUILD_ROOT%{_datadir}/apps/{kconf_update,profiles,remotes} \
    $RPM_BUILD_ROOT%{_datadir}/autostart \
    $RPM_BUILD_ROOT%{_datadir}/services \
    $RPM_BUILD_ROOT%{_datadir}/config.kcfg \
    $RPM_BUILD_ROOT%{_docdir}/kde \
    $RPM_BUILD_ROOT%{_kdedocdir}/en \
    $RPM_BUILD_ROOT%{_desktopdir}/kde \
    $RPM_BUILD_ROOT%{_libdir}/kconf_update_bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps
%dir %{_datadir}/apps/kconf_update
%dir %{_datadir}/apps/profiles
%dir %{_datadir}/apps/remotes
%dir %{_datadir}/autostart
%dir %{_datadir}/services
%dir %{_datadir}/config.kcfg
%dir %{_docdir}/kde
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%dir %{_desktopdir}/kde
%dir %{_libdir}/kconf_update_bin
