%global         srcname     azure-functions-devops-build

Name:           python-%{srcname}
Version:        0.0.22
Release:        1%{?dist}
Summary:        Python package for integrating Azure Functions with Azure DevOps
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel



%global _description %{expand:
Python package for integrating Azure Functions with Azure DevOps}

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
%{python3_sitelib}/azure_functions_devops_build
%{python3_sitelib}/azure_functions_devops_build-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.22-1
- First package.
