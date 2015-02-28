%global owner ojuba-org
%global commit #Write commit number here

Name:           ojuba-bookmarks
Version:        35
Release:        3%{?dist}
Summary:        Ojuba bookmarks
Group:          Applications/Internet
License:	WAQFv2
URL:            http://ojuba.org/
Source:		https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch
Provides:       system-bookmarks
Provides:       fedora-bookmarks
Obsoletes:      fedora-bookmarks
Obsoletes:      system-bookmarks
Provides:       redhat-bookmarks
Obsoletes:      redhat-bookmarks

%description
This package contains the default bookmarks for Ojuba Linux.

%prep
%setup -q -n %{name}-%{commit}

%build
# NOTHING TO BUILD.

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 default-bookmarks.html $RPM_BUILD_ROOT%{_datadir}/bookmarks
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
cd $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
ln -s %{_datadir}/bookmarks/default-bookmarks.html bookmarks.html

%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html
%{_libdir}/firefox/defaults/profile/bookmarks.html

%changelog
* Sun Mar 2 2014 Mosaab Alzoubi <moceap@hotmail.com> - 35-3
- Fixes

* Sun Feb 16 2014 Mosaab Alzoubi <moceap@hotmail.com> - 35-1
- General Revision.
- Release For Ojuba 35.

* Fri Jan 13 2012 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 16-1
- release for ojuba 16

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
