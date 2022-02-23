Summary:	K Desktop Environment - common directories
Summary(pl.UTF-8):	Wspólne katalogi KDE (K Desktop Environment)
Name:		kde-common-dirs
Version:	0.8
Release:	12
License:	LGPL
Group:		X11/Libraries
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
# avoid rpm 4.4.9 adding rm -rf buildroot, we need the dirs to check consistency
%define		__spec_clean_body	%{nil}

%description
KDE 3/4/5 common directories.

%description -l pl.UTF-8
Katalogi wspólne dla KDE 3/4/5.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
	$RPM_BUILD_ROOT%{_libdir}/kde4 \
	$RPM_BUILD_ROOT%{_libdir}/kde4/plugins \
	$RPM_BUILD_ROOT%{_libdir}/kde4/imports/org/kde \
	$RPM_BUILD_ROOT%{_libdir}/qt4/imports/org/kde \
	$RPM_BUILD_ROOT%{_libdir}/qt4/imports/org/kde/edu \
	$RPM_BUILD_ROOT%{_datadir}/kde4 \
	$RPM_BUILD_ROOT%{_datadir}/kde4/services \
	$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
	$RPM_BUILD_ROOT%{_datadir}/apps/appdata \
	$RPM_BUILD_ROOT%{_datadir}/apps/kde \
	$RPM_BUILD_ROOT%{_datadir}/apps/konqueror \
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
	$RPM_BUILD_ROOT%{_iconsdir}/oxygen/{scalable,8x8,16x16,22x22,32x32,48x48,64x64,128x128,512x512}/{actions,animations,apps,categories,devices,emblems,emotes,mimetypes,places,special,status} \
	$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{8x8,16x16,22x22,32x32,48x48,64x64,128x128,512x512}/{actions,animations,apps,categories,devices,emblems,emotes,mimetypes,places,special,status} \
	$RPM_BUILD_ROOT%{_docdir}/kde \
	$RPM_BUILD_ROOT%{_desktopdir}/kde \
	$RPM_BUILD_ROOT%{_kdedocdir}/{ca,cs,da,de,en,en_GB,en_US,es,et,fi,fr,gl,hu,id,it,ja,nb,nl,pl,pt,pt_BR,ro,ru,sk,sl,sq,sv,tr,uk,zh_CN,zh_TW}/common \
	$RPM_BUILD_ROOT%{_kdedocdir}/en/kcontrol

%clean
cd $RPM_BUILD_ROOT
check_filesystem_dirs() {
	RPMFILE=%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	TMPFILE=$(mktemp)
	# NOTE:	we must exclude from check all existing dirs belonging to FHS and qt4
	find | sed -e 's|^\.||g' -e 's|^$||g' | LC_ALL=C sort | grep -v $TMPFILE | grep -E -v '^/(usr|usr/%{_lib}|usr/share|usr/share/doc|usr/share/applications|usr/share/icons|usr/%{_lib}/qt4|usr/%{_lib}/qt4/imports|usr/%{_lib}/qt4/imports/org)$' > $TMPFILE

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
%dir %{_libdir}/kde4
%dir %{_libdir}/kde4/imports
%dir %{_libdir}/kde4/imports/org
%dir %{_libdir}/kde4/imports/org/kde
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/qt4/imports/org/kde
%dir %{_libdir}/qt4/imports/org/kde/edu
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps
%dir %{_datadir}/apps/appdata
%dir %{_datadir}/apps/kde
%dir %{_datadir}/apps/konqueror
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
%dir %{_desktopdir}/kde
%dir %{_iconsdir}/oxygen
%{_iconsdir}/oxygen/*
%dir %{_iconsdir}/crystalsvg
%{_iconsdir}/crystalsvg/*
%lang(ca) %dir %{_kdedocdir}/ca
%lang(ca) %dir %{_kdedocdir}/ca/common
%lang(cs) %dir %{_kdedocdir}/cs
%lang(cs) %dir %{_kdedocdir}/cs/common
%lang(da) %dir %{_kdedocdir}/da
%lang(da) %dir %{_kdedocdir}/da/common
%lang(de) %dir %{_kdedocdir}/de
%lang(de) %dir %{_kdedocdir}/de/common
%lang(en) %dir %{_kdedocdir}/en
%lang(en) %dir %{_kdedocdir}/en/common
%lang(en) %dir %{_kdedocdir}/en/kcontrol
%lang(es) %dir %{_kdedocdir}/es
%lang(es) %dir %{_kdedocdir}/es/common
%lang(en_GB) %dir %{_kdedocdir}/en_GB
%lang(en_GB) %dir %{_kdedocdir}/en_GB/common
%lang(en_US) %dir %{_kdedocdir}/en_US
%lang(en_US) %dir %{_kdedocdir}/en_US/common
%lang(et) %dir %{_kdedocdir}/et
%lang(et) %dir %{_kdedocdir}/et/common
%lang(fi) %dir %{_kdedocdir}/fi
%lang(fi) %dir %{_kdedocdir}/fi/common
%lang(fr) %dir %{_kdedocdir}/fr
%lang(fr) %dir %{_kdedocdir}/fr/common
%lang(gl) %dir %{_kdedocdir}/gl
%lang(gl) %dir %{_kdedocdir}/gl/common
%lang(hu) %dir %{_kdedocdir}/hu
%lang(hu) %dir %{_kdedocdir}/hu/common
%lang(id) %dir %{_kdedocdir}/id
%lang(id) %dir %{_kdedocdir}/id/common
%lang(it) %dir %{_kdedocdir}/it
%lang(it) %dir %{_kdedocdir}/it/common
%lang(ja) %dir %{_kdedocdir}/ja
%lang(ja) %dir %{_kdedocdir}/ja/common
%lang(nb) %dir %{_kdedocdir}/nb
%lang(nb) %dir %{_kdedocdir}/nb/common
%lang(nl) %dir %{_kdedocdir}/nl
%lang(nl) %dir %{_kdedocdir}/nl/common
%lang(pl) %dir %{_kdedocdir}/pl
%lang(pl) %dir %{_kdedocdir}/pl/common
%lang(pt) %dir %{_kdedocdir}/pt
%lang(pt) %dir %{_kdedocdir}/pt/common
%lang(pt_BR) %dir %{_kdedocdir}/pt_BR
%lang(pt_BR) %dir %{_kdedocdir}/pt_BR/common
%lang(ro) %dir %{_kdedocdir}/ro
%lang(ro) %dir %{_kdedocdir}/ro/common
%lang(ru) %dir %{_kdedocdir}/ru
%lang(ru) %dir %{_kdedocdir}/ru/common
%lang(sk) %dir %{_kdedocdir}/sk
%lang(sk) %dir %{_kdedocdir}/sk/common
%lang(sl) %dir %{_kdedocdir}/sl
%lang(sl) %dir %{_kdedocdir}/sl/common
%lang(sq) %dir %{_kdedocdir}/sq
%lang(sq) %dir %{_kdedocdir}/sq/common
%lang(sv) %dir %{_kdedocdir}/sv
%lang(sv) %dir %{_kdedocdir}/sv/common
%lang(tr) %dir %{_kdedocdir}/tr
%lang(tr) %dir %{_kdedocdir}/tr/common
%lang(uk) %dir %{_kdedocdir}/uk
%lang(uk) %dir %{_kdedocdir}/uk/common
%lang(zh_TW) %dir %{_kdedocdir}/zh_TW
%lang(zh_TW) %dir %{_kdedocdir}/zh_TW/common
