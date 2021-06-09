%global         srcname     azure-core

Name:           python-%{srcname}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Azure Core shared client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Obsoletes:      python3-azure-sdk < 5.0.1
Conflicts:      python3-azure-sdk

%global _description %{expand:
Azure Core shared client library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


# Source from pypi does not contain a license file. 😞
%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/azure/core
%{python3_sitelib}/azure_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.14.0-1
- First package.
