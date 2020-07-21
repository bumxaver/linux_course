Name:          simple
Version:        1.0
Release:        1%{?dist}
Summary:        Test

License:        none
Source0:       simple-1.0.tgz

BuildRequires:  golang
Requires:       /bin/echo

%define debug_package %{nil}

%description
Example rpm 

%prep
%setup -qc


%build
go build simple-service.go

%install
mkdir -p %{buildroot}/usr/local/simple
mkdir -p %{buildroot}/usr/lib/systemd/system
cp simple-service %{buildroot}/usr/local/simple
cp -a simple-service.service %{buildroot}/usr/lib/systemd/system

%files
/usr/local/simple
/usr/local/simple/simple-service
/usr/lib/systemd/system/simple-service.service

%post
/bin/systemctl start simple-service.service >/dev/null 2>&1

%changelog
