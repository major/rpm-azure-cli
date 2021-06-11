%global         srcname     azure-mgmt-sqlvirtualmachine

Name:           python-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Microsoft Azure SQL Virtual Machine Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel



%global _description %{expand:
Microsoft Azure SQL Virtual Machine Management Client Library for Python}

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
%{python3_sitelib}/azure/mgmt/sqlvirtualmachine
%{python3_sitelib}/azure_mgmt_sqlvirtualmachine-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.5.0-1
- First package.
