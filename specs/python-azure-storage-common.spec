%global         srcname     azure-storage-common

Name:           python-%{srcname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Common Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
Microsoft Azure Storage Common Client Library for Python}

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
%doc README.rst
%license LICENSE.txt
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/storage/common
%{python3_sitelib}/azure_storage_common-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jun 10 2021 Major Hayden <major@mhtx.net> - 2.1.0-1
- First package.
