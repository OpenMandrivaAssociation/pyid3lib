Summary:	Python module for editing ID3v2 tags of MP3 audio files
Name:		pyid3lib
Version:	0.5.1
Release:	27
License:	LGPLv2
Group:		Sound
Url:		http://pyid3lib.sourceforge.net/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		pyid3lib-0.5.1-64bit.patch
Patch1:		pyid3lib-0.5.1-gcc-4.4.patch
BuildRequires:	id3lib-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python2)

%description
%{name} is a Python module for editing ID3v2 tags of MP3 audio files.

%prep
%setup -q
%autopatch -p1
chmod -R go+rX .

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot}

%files
%doc COPYING doc.html README
%py2_platsitedir/*

