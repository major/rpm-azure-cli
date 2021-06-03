%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-mgmt-batchai

Name:           python-%{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Batch AI Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Batch AI Management Client Library for Python}

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
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__pycache__/__init__.cpython-*.pyc


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/azure/mgmt/batchai
%{python3_sitelib}/azure_mgmt_batchai-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.0.0-1
- First package.
