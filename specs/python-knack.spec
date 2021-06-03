%global         srcname     knack

# tests are enabled by default
%bcond_without  tests

Name:           python-%{srcname}
Version:        0.8.2
Release:        1%{?dist}
Summary:        A Command-Line Interface framework
License:        MIT
URL:            https://github.com/microsoft/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-argcomplete
BuildRequires:  python3-colorama
BuildRequires:  python3-jmespath
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-tabulate
%endif

%global _description %{expand:
A Command-Line Interface framework}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

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


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.8.2-1
- First package.
