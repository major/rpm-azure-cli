%global         srcname     azure-mgmt-applicationinsights

Name:           python-%{srcname}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Microsoft Azure Application Insights Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Application Insights Management Client Library for Python}

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
    %{buildroot}%{python3_sitelib}/azure/mgmt/__pycache__/__init__.cpython-*.pyc

%files -n python3-%{srcname}
%{python3_sitelib}/azure/mgmt/applicationinsights
%{python3_sitelib}/azure_mgmt_applicationinsights-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.1.1-1
- First package.
