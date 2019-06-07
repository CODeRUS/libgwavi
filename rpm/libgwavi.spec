Name:           libgwavi
Version:        1.0.0
Release:        0
Summary:        Tiny C library aimed at creating AVI files
License:        BSD3
Group:          Development/Tools/Building
Url:            https://github.com/Rolinh/libgwavi
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gcc

%description
libgwavi is a fork of libkohn-avi. It is a tiny C library aimed at creating AVI files.

%package devel
Summary:        Development files for libgwavi, a tiny C library aimed at creating AVI files
Group:          Development/Tools/Building
Requires:       %name = %version
BuildArch:      noarch

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the gRPC reference implementation.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/lib
install -m 755 lib/%{name}.* %{buildroot}/usr/lib

mkdir -p %{buildroot}/usr/include/gwavi
install -m 644 inc/*.h %{buildroot}/usr/include/gwavi
install -m 644 src/*.h %{buildroot}/usr/include/gwavi

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%_libdir/%{name}.*

%files devel
%defattr(-,root,root)
%{_includedir}/gwavi/*.h