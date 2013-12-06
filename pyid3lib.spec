Summary:	Python module for editing ID3v2 tags of MP3 audio files
Name:		pyid3lib
Version:	0.5.1
Release:	19
License:	LGPLv2
Group:		Sound
Url:		http://pyid3lib.sourceforge.net/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		pyid3lib-0.5.1-64bit.patch
Patch1:		pyid3lib-0.5.1-gcc-4.4.patch
BuildRequires:	id3lib-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python)

%description
%{name} is a Python module for editing ID3v2 tags of MP3 audio files.

%prep
%setup -q
%apply_patches
chmod -R go+rX .

%build
%{_bindir}/python setup.py build

%install
%{_bindir}/python setup.py install --root=%{buildroot}

%files
%doc COPYING doc.html README
%py_platsitedir/*

