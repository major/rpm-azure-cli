%global         srcname     azure-datalake-store

Name:           python-%{srcname}
Version:        0.0.52
Release:        1%{?dist}
Summary:        Azure Data Lake Store Filesystem Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools



%global _description %{expand:
Azure Data Lake Store Filesystem Client Library for Python}

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

# Remove the samples since many of them are empty or have wrong line endings.
rm -rf %{buildroot}%{python3_sitelib}/samples

# Clean up files left at the base package directory.
rm -f %{buildroot}%{python3_sitelib}/azure/datalake/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/datalake/__pycache__/__init__.cpython-*.pyc


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/datalake/store
%{python3_sitelib}/azure_datalake_store-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.52-1
- First package.
