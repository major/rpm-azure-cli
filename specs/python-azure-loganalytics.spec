%global         srcname     azure-loganalytics

Name:           python-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Log Analytics Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel



%global _description %{expand:
Microsoft Azure Log Analytics Client Library for Python}

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
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-*.pyc


%files -n python3-%{srcname}
%{python3_sitelib}/azure/loganalytics
%{python3_sitelib}/azure_loganalytics-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.1.0-1
- First package.
