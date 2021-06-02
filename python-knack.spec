%{?!python3_pkgversion:%global python3_pkgversion 3}

# tests are enabled by default
%bcond_without tests

%global         srcname     knack
%global         forgeurl    https://github.com/microsoft/%{srcname}
Version:        0.8.2
%global         tag         v%{version}
%global         distprefix  %{nil}
%forgemeta

Name:           python-%{srcname}
Release:        1%{?dist}
Summary:        A Command-Line Interface framework
License:        MIT
URL:            https://github.com/microsoft/knack
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-argcomplete
BuildRequires:  python%{python3_pkgversion}-colorama
BuildRequires:  python%{python3_pkgversion}-jmespath
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-tabulate
BuildRequires:  python%{python3_pkgversion}-vcrpy
%endif

%global _description %{expand:
A Command-Line Interface framework}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Use unittest's mock that is built in for Python 3.x.
# Upstream PR made to fix this: (thanks, Ben!)
#   https://github.com/microsoft/knack/pull/248
sed -i 's/^import mock/from unittest import mock/' tests/*.py


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
# Skip the tests which require network connectivity.
%pytest -k "not test_server_with_path"
%endif


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/knack
%{python3_sitelib}/knack-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.8.2-1
- First package.
