%define version 0.5.1
%define release %mkrel 14

Summary:	Python module for editing ID3v2 tags of MP3 audio files
Name:		pyid3lib
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Sound
URL:		http://pyid3lib.sourceforge.net/
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0: pyid3lib-0.5.1-64bit.patch
Patch1: pyid3lib-0.5.1-gcc-4.4.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libid3-devel
BuildRequires:	zlib-devel
BuildRequires:	python-devel

%description
%{name} is a Python module for editing ID3v2 tags of MP3 audio files.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
chmod -R go+rX .

%build
%{_bindir}/python setup.py build

%install
rm -rf %{buildroot}
%{_bindir}/python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING doc.html README
%py_platsitedir/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-13mdv2011.0
+ Revision: 667906
- mass rebuild

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.5.1-12mdv2011.0
+ Revision: 591320
- rebuild for py 2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-11mdv2010.1
+ Revision: 523752
- rebuilt for 2010.1

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.5.1-10mdv2010.0
+ Revision: 453353
- fix build with gcc 4.4 (patch from gentoo)

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.1-9mdv2009.1
+ Revision: 319620
- rebuild with python 2.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-8mdv2009.0
+ Revision: 225125
- rebuild

* Tue Feb 26 2008 Erwan Velu <erwan@mandriva.org> 0.5.1-7mdv2008.1
+ Revision: 175339
- REbuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-6mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.1-6mdv2007.0
+ Revision: 94780
- bump release tag
- fix build on 64 bit
- Import pyid3lib

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-5mdv2007.1
- update file list

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.5.1-4mdk
- Rebuild for new python

* Tue Jun 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-3mdk
- rebuild for new g++

