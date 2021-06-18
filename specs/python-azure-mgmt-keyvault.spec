%global         srcname     azure-mgmt-keyvault

Name:           python-%{srcname}
Version:        9.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Keyvault Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
Patch0:         python-azure-mgmt-keyvault-sane-requirements.patch

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Microsoft Azure Keyvault Management Client Library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 9.0.0-1
- First package.
