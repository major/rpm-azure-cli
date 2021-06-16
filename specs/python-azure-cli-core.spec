%global         srcname     azure-cli-core

Name:           python-%{srcname}
Version:        2.25.0
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools Core Module
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
# Allow for newer versions of certain components.
Patch0:         python-azure-cli-core-requirements-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
Microsoft Azure Command-Line Tools Core Module}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p0 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.rst
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.25.0-1
- First package.
