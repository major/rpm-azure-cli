%global         srcname     javaproperties

# tests are enabled by default
%bcond_without  tests

Name:           python-%{srcname}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Read & write Java .properties files
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-dateutil
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
%endif

%global _description %{expand:
Read & write Java .properties files}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Project uses pyproject for building, but pyproject-rpm-macros don't exist in
# EPEL. This is a workaround to make it easily installable with setuptools.
tee setup.py > /dev/null << EOF
from setuptools import setup
setup()
EOF


%build
%{py3_build}


%install
%py3_install


%if %{with tests}
%check
# Environment variables come from upstream's tox.ini:
#   https://github.com/major/javaproperties/blob/master/tox.ini
# Tests fail if they are not present due to time zone shenanigans.
export LC_ALL=en_US.UTF-8
export TZ=EST5EDT,M3.2.0,M11.1.0
%pytest
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.8.0-1
- First package.
