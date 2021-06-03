%global         srcname     azure-mgmt-core

Name:           python-%{srcname}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Azure Management Core Library
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
# Patch0:         python-azure-core-version-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Azure Management Core Library}

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


%files -n python3-%{srcname}
%{python3_sitelib}/azure/mgmt/core
%{python3_sitelib}/azure_mgmt_core-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.2-1
- First package.
