%global         srcname     azure-mgmt-servicefabricmanagedclusters

Name:           python-%{srcname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Service Fabric Managed Clusters Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Service Fabric Managed Clusters Management Client Library for
Python}

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
%{python3_sitelib}/azure/mgmt/servicefabricmanagedclusters
%{python3_sitelib}/azure_mgmt_servicefabricmanagedclusters-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.0.0-1
- First package.
