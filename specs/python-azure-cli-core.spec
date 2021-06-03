%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-cli-core

Name:           python-%{srcname}
Version:        2.24.2
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools Core Module
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
Microsoft Azure Command-Line Tools Core Module}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove version cap on cryptography.
sed -i "s/'cryptography>=3.2,<3.4',$/'cryptography>=3.2',/" setup.py

# Allow for newer versions of PyJWT.
sed -i "s/'PyJWT==1.7.1',$/'PyJWT>=1.7.1',/" setup.py


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
