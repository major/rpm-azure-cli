%global         srcname     azure-multiapi-storage

Name:           python-%{srcname}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Client Library for Python with multi API version support
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

Obsoletes: python-azure-sdk < 5.0.1

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools



%global _description %{expand:
Microsoft Azure Storage Client Library for Python with multi API version
support}

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
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
# This is the only multiapi package, so it takes everything under the path.
%{python3_sitelib}/azure/multiapi
%{python3_sitelib}/azure_multiapi_storage-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.6.2-1
- First package.
