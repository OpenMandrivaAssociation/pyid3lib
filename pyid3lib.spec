%define version 0.5.1
%define release %mkrel 7

Summary:	Python module for editing ID3v2 tags of MP3 audio files
Name:		pyid3lib
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Sound
URL:		http://pyid3lib.sourceforge.net/
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch: pyid3lib-0.5.1-64bit.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libid3-devel
BuildRequires:	zlib-devel
BuildRequires:	python-devel

%description
%{name} is a Python module for editing ID3v2 tags of MP3 audio files.

%prep
%setup -q
%patch -p1
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


