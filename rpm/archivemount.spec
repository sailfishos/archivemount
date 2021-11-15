Name:       archivemount

Summary:    Mounts an archive for access as a file system
Version:    0.9.1
Release:    1
License:    LGPLv2
URL:        https://www.cybernoia.de/software/archivemount.html
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  automake
BuildRequires:  autoconf
Patch1: 0001-archivemount-Don-t-apply-read-only-st_mode-changes-i.patch

%description
%{summary}.

%package doc
Summary: archivemount docs
Requires: %{name} = %{version}-%{release}
%description doc
%summary

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf --force --install
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/archivemount
%license COPYING

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/archivemount.*

