%define version 0.5.1
%define release %mkrel 13

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


