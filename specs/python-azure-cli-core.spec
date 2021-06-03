%global         srcname     azure-cli-core

Name:           python-%{srcname}
Version:        2.24.2
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools Core Module
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Command-Line Tools Core Module}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


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


%files -n python3-%{srcname}
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
