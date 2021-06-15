%global         srcname     azure-core

Name:           python-%{srcname}
Version:        1.15.0
Release:        1%{?dist}
Summary:        Azure Core shared client library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes: python-azure-sdk < 5.0.1

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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


# NOTE(mhayden): Source from pypi does not contain a license file. 😞
# PR made upstream: https://github.com/Azure/azure-sdk-for-python/pull/19191
%files -n python3-%{srcname}
%doc README.md
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/core
%{python3_sitelib}/azure_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.15.0-1
- First package.
