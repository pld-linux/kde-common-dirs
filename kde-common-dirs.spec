# avoid rpm 4.4.9 adding rm -rf buildroot, we need the dirs to check consistency
%define		__spec_clean_body	%{nil}
%define		_enable_debug_packages	0
Summary:	K Desktop Environment - common directories
Summary(pl.UTF-8):	Wspólne katalogi KDE (K Desktop Environment)
Name:		kde-common-dirs
Version:	0.1
Release:	2
License:	LGPL
Group:		X11/Libraries
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE 3 & KDE 4 common directories.

%description -l pl.UTF-8
Katalogi wspólne dla KDE 3 i KDE 4.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
	$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
	$RPM_BUILD_ROOT%{_datadir}/apps/kde \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/css \
	$RPM_BUILD_ROOT%{_datadir}/apps/kjava \
	$RPM_BUILD_ROOT%{_datadir}/apps/kconf_update \
	$RPM_BUILD_ROOT%{_datadir}/apps/kstyle/themes \
	$RPM_BUILD_ROOT%{_datadir}/apps/profiles \
	$RPM_BUILD_ROOT%{_datadir}/apps/remotes \
	$RPM_BUILD_ROOT%{_datadir}/autostart \
	$RPM_BUILD_ROOT%{_datadir}/services \
	$RPM_BUILD_ROOT%{_datadir}/config/ui \
	$RPM_BUILD_ROOT%{_datadir}/config.kcfg \
	$RPM_BUILD_ROOT%{_datadir}/emoticons \
	$RPM_BUILD_ROOT%{_docdir}/kde \
	$RPM_BUILD_ROOT%{_kdedocdir}/en \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
cd $RPM_BUILD_ROOT
check_filesystem_dirs() {
	RPMFILE=%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	TMPFILE=$(mktemp)
	# NOTE: we must exclude from check all existing dirs belonging to FHS
	find | sed -e 's|^\.||g' -e 's|^$||g' | LC_ALL=C sort | grep -v $TMPFILE | grep -E -v '^/(usr|usr/lib|usr/lib64|usr/share|usr/share/doc|usr/share/applications)$' > $TMPFILE

	# find finds also '.', so use option -B for diff
	if rpm -qpl %{_rpmdir}/$RPMFILE | grep -v '^/$' | LC_ALL=C sort | diff -uB $TMPFILE -; then
		rm -rf $RPM_BUILD_ROOT
	else
		echo -e "\nNot so good, some directories are not included in package\n"
		exit 1
	fi
	rm -f $TMPFILE
}
check_filesystem_dirs

%files
%defattr(644,root,root,755)
%dir %{_libdir}/kconf_update_bin
%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps
%dir %{_datadir}/apps/kde
%dir %{_datadir}/apps/kjava
%dir %{_datadir}/apps/khtml
%dir %{_datadir}/apps/khtml/css
%dir %{_datadir}/apps/kconf_update
%dir %{_datadir}/apps/kstyle
%dir %{_datadir}/apps/kstyle/themes
%dir %{_datadir}/apps/profiles
%dir %{_datadir}/apps/remotes
%dir %{_datadir}/autostart
%dir %{_datadir}/config
%dir %{_datadir}/config/ui
%dir %{_datadir}/config.kcfg
%dir %{_datadir}/emoticons
%dir %{_datadir}/services
%dir %{_docdir}/kde
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%dir %{_desktopdir}/kde
