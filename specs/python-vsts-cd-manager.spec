%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     vsts-cd-manager

Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Python wrapper around some of the VSTS APIs
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Python wrapper around some of the VSTS APIs}

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


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/aex_accounts
%{python3_sitelib}/continuous_delivery
%{python3_sitelib}/vsts_cd_manager
%{python3_sitelib}/vsts_info_provider
%{python3_sitelib}/vsts_cd_manager-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.0.2-1
- First package.
