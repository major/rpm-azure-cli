%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     fabric

Name:           python-%{srcname}
Version:        2.6.0
Release:        1%{?dist}
Summary:        High level SSH command execution
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/fabric
%{python3_sitelib}/fabric-*.egg-info
%{_bindir}/fab


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.6.0-1
- First package.
