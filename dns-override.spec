Summary: Library to override DNS settings
Name: libdns-override
Version: 1.0
Release: 1
License: GNU GPL v3

Source0: dns-override.c

%define dest_folder /var/lib64

%description
Used to override DNS settings for a single process (and its decendants) using the glibc resolv

%prep

%build
make all

%install
mkdir -p $RPM_BUILD_ROOT%{dest_folder}
cp -r %{source_folder}/dns-override.so %buildroot/var/lib64/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{dest_folder}/dns-override.so

%post

%preun

%postun
