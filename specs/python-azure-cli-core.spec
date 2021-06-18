%global         srcname     azure-cli-core

Name:           python-%{srcname}
Version:        2.25.0
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools Core Module
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
# Allow for newer versions of most components, but allow for slightly older
# urllib3.
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


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.25.0-1
- First package.
