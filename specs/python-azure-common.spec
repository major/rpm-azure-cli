%global         srcname     azure-common

Name:           python-%{srcname}
Version:        1.1.27
Release:        1%{?dist}
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


Conflicts:      python3-azure-sdk

%global _description %{expand:
Microsoft Azure Client Library for Python (Common)}

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
%{python3_sitelib}/azure/common
%{python3_sitelib}/azure/profiles
%{python3_sitelib}/azure_common-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.1.27-1
- First package.
