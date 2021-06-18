%global         srcname     azure-functions-devops-build

Name:           python-%{srcname}
Version:        0.0.22
Release:        1%{?dist}
Summary:        Python package for integrating Azure Functions with Azure DevOps
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Python package for integrating Azure Functions with Azure DevOps}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.md


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure_functions_devops_build


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.22-1
- First package.
