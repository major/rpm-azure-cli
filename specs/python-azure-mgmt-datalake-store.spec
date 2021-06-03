%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-mgmt-datalake-store

Name:           python-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Microsoft Azure Data Lake Store Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Data Lake Store Management Client Library for Python}

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

# Clean up files left at the base package directory.
rm -f %{buildroot}%{python3_sitelib}/azure/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-39*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__pycache__/__init__.cpython-39*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/datalake/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__.cpython-39*.pyc


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/azure/mgmt/datalake/store
%{python3_sitelib}/azure_mgmt_datalake_store-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.5.0-1
- First package.