%{?!python3_pkgversion:%global python3_pkgversion 3}

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

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Azure Management Core Library}

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
%{python3_sitelib}/azure/mgmt/core
%{python3_sitelib}/azure_mgmt_core-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.2-1
- First package.
