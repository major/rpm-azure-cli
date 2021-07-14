%global         srcname     azure-cli-core

Name:           python-%{srcname}
Version:        2.26.1
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools Core Module
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
Patch0:         python-azure-cli-core-requirements-fix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Microsoft Azure Command-Line Tools Core Module}

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


# License files are missing from some of the python packages. Filed a PR
# upstream to get it fixed: https://github.com/Azure/azure-cli/pull/18749
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.26.1-1
- First package.
