Name:           jconf
Version:        0.9.1
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
mkdir -p %{buildroot}/usr/include

# Asıl .so dosyasını kopyala
install -m 0755 Lib/libJConf.so %{buildroot}/usr/lib64/

# Header dosyası
cp Inc/JConf.h %{buildroot}/usr/include/


%files
/usr/lib64/libJConf.so

%files devel
/usr/include/JConf.h


%changelog
* Sat Jul 05 2025 Kadir Aydın <jixoid@gmail.com> - 0.9.1
- Initial RPM build
