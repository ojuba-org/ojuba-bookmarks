Name:           ojuba-bookmarks
Version:        16
Release:        1
Summary:        Ojuba bookmarks
Group:          Applications/Internet
License:        Waqf
URL:            http://www.ojuba.org/
Source0:        http://git.ojuba.org/cgit/ojuba-bookmarks/plain/default-bookmarks.html
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
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
cd $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
ln -s ../../../../bookmarks/default-bookmarks.html bookmarks.html

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html
%{_libdir}/firefox/defaults/profile/bookmarks.html

%changelog
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

