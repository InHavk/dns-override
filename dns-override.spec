Summary: Library to override DNS settings
Name: libdns-override
Version: 1.0
Release: 1%{?dist}
License: GNU GPL v3

Source0: dns-override.c

%description
Used to override DNS settings for a single process (and its decendants) using the glibc resolv

%prep

%build
gcc -Wall -Werror -fPIC -shared -o dns-override.so ${SOURCE0} -ldl

%install
mkdir -p %{buildroot}/%{_libdir}
cp -r %{source_folder}/dns-override.so %{buildroot}/%{_libdir}/

%clean
%{__rm} -rf %{buildroot}

%files
%{_libdir}/dns-override.so

%post

%preun

%postun
