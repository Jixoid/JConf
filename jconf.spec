Name:           jconf
Version:        0.9.5
Release:        1%{?dist}
Summary:        Lightweight configuration library with binary/text format support

License:        GPLv3
URL:            https://github.com/Jixoid/JConf
Source0:        jconf.tar.gz

BuildRequires:  gcc-c++, clang
Requires:       libstdc++


%define _debugsource_template %{nil}

%description
C API for Jix Config file, supporting both human-readable and binary formats.

%package devel
Summary:        Header and symlink files for jconf development
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for JConf. Required to compile software against libJConf.

%prep
%setup -q -n jconf


%build


%install
mkdir -p %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/include/jconf

# Asıl .so dosyasını kopyala
install -m 0755 Lib/libJConf.so %{buildroot}/usr/lib64/
install -m 0755 Lib/libJConf.a %{buildroot}/usr/lib64/

# Header dosyası
install -m 0644 Inc/JConf.h %{buildroot}/usr/include/jconf/
install -m 0644 Inc/JConf.hh %{buildroot}/usr/include/jconf/


%files
/usr/lib64/libJConf.so
/usr/lib64/libJConf.a

%files devel
/usr/include/jconf/JConf.h
/usr/include/jconf/JConf.hh


%changelog
* 05/12/2025 Kadir Aydın <jixoid@gmail.com> - 0.9.5
- Please see here https://github.com/Jixoid/JConf
