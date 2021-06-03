%global         srcname     azure-mgmt-datalake-analytics

Name:           python-%{srcname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Microsoft Azure Data Lake Analytics Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Data Lake Analytics Management Client Library for Python}

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

# Clean up files left at the base package directory.
rm -f %{buildroot}%{python3_sitelib}/azure/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__pycache__/__init__.cpython-*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/datalake/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__.cpython-*.pyc


%files -n python3-%{srcname}
%{python3_sitelib}/azure/mgmt/datalake/analytics
%{python3_sitelib}/azure_mgmt_datalake_analytics-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.2.1-1
- First package.
