%global         srcname     azure-mgmt-iothubprovisioningservices

Name:           python-%{srcname}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Microsoft Azure IoTHub Provisioning Services Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure IoTHub Provisioning Services Client Library for Python}

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

# Some __init__.py files are left hanging around in azure and azure/mgmt which
# do not belong in this package.
rm -f \
    %{buildroot}%{python3_sitelib}/azure/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-*.pyc \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/mgmt/__pycache__/__init__.cpython-*.pyc

%files -n python3-%{srcname}
%{python3_sitelib}/azure/mgmt/iothubprovisioningservices
%{python3_sitelib}/azure_mgmt_iothubprovisioningservices-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.2.0
- First package.
