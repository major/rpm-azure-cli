%global srcname azure-mgmt-core

Name:           python-%{srcname}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Azure Management Core Library

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
# Patch0:         python-azure-core-version-fix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Azure Management Core Library}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p0 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.2-1
- First package.
