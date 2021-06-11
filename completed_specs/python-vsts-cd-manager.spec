%global         srcname     vsts-cd-manager

Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Visual Studio Team Services Continuous Delivery Manager
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package provides the class ContinuousDeliveryManager and supporting
classes. This CD manager class allows the caller to manage Azure Continuous
Delivery pipelines that are maintained within a VSTS account.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Fix wrong line endings in the README.rst.
sed -i 's/\r$//' README.rst

%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/aex_accounts
%{python3_sitelib}/continuous_delivery
%{python3_sitelib}/vsts_cd_manager
%{python3_sitelib}/vsts_info_provider
%{python3_sitelib}/vsts_cd_manager-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.0.2-1
- First package.
