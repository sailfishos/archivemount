Name:       archivemount

Summary:    Mounts an archive for access as a file system
Version:    0.8.7+git1.1
Release:    1
Group:      Applications/System
License:    LGPL2
URL:        http://www.cybernoia.de/software/archivemount/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  automake
BuildRequires:  autoconf

%description
%{summary}.

%package doc
Summary: archivemount docs
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description doc
%summary

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf --force --install
%configure

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/archivemount

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/archivemount.*

