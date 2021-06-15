%global         srcname     azure-mgmt-iothub

Name:           python-%{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure IoTHub Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes: python-azure-sdk < 5.0.1

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools



%global _description %{expand:
Microsoft Azure IoTHub Management Client Library for Python}

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
%doc README.md
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%{python3_sitelib}/azure/mgmt/iothub
%{python3_sitelib}/azure_mgmt_iothub-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.0.0-1
- First package.
