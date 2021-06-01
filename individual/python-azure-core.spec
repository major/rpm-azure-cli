# tests are enabled by default
%bcond_without tests

%global srcname azure-core

Name:           python-%{srcname}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Azure Core shared client library for Python

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-aiohttp
BuildRequires:  python%{python3_pkgversion}-msrest
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-trio
%endif

%global _description %{expand:
Azure Core shared client library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.14.0-1
- First package.
