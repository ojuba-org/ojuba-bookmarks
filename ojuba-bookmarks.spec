Name:           ojuba-bookmarks
Version:        15
Release:        5
Summary:        Ojuba bookmarks
Group:          Applications/Internet
License:        Waqf
URL:            http://www.ojuba.org/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks
Provides:       fedora-bookmarks
Obsoletes:      fedora-bookmarks < %{version}.%{release}
Obsoletes:      system-bookmarks < %{version}.%{release}

%description
This package contains the default bookmarks for Ojuba Linux.

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%triggerin -- firefox
for i in %{_libdir}/firefox-*
do
 if [ -x $i/firefox ]; then
   mkdir -p $i/defaults/profile/ || :
   ln -sf %{_datadir}/bookmarks/default-bookmarks.html $i/defaults/profile/bookmarks.html
 fi
done

%triggerpostun -- firefox
for i in %{_libdir}/firefox-*
do
 if [ ! -x $i/firefox ]; then
   [ -e $i/defaults/profile/bookmarks.html ] && rm $i/defaults/profile/bookmarks.html
 fi
done

%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Wed Jul 21 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 13.0.0-5
- add thawab

* Wed Jun 16 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 13.0.0-4
- update and rebuild for ojuba 4

* Mon Jul 20 2009 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 11.0.0-1
- update bookmarks

* Wed Jan 14 2009 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 10.0.0-1
- more bookmarks

* Thu Jul 24 2008 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 8.0.0-2
- remove duplicated links
* Tue May 20 2008 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 8.0.0-1
- Initial version

