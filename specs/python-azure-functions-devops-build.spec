%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-functions-devops-build

Name:           python-%{srcname}
Version:        0.0.22
Release:        1%{?dist}
Summary:        Python package for integrating Azure Functions with Azure DevOps
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Python package for integrating Azure Functions with Azure DevOps}

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
%{python3_sitelib}/azure_functions_devops_build
%{python3_sitelib}/azure_functions_devops_build-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.22-1
- First package.
