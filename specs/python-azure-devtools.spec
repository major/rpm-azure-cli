%global         reponame        azure-sdk-for-python
%global         srcname         azure-devtools
%global         forgeurl        https://github.com/Azure/%{reponame}/
%global         commit          aa29c1cb5da14ab3efca04dc3838b473a88536d4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         distprefix      %{nil}
%global         short_version   1.2.1
%forgemeta

# Tests are disabled here because the testing code within this package depends
# on the most of the repository being checked out, installed, and added to
# PYTHONPATH.
%bcond_with     tests

Name:           python-%{srcname}
Version:        %{short_version}~git.1.%{shortcommit}
Release:        1%{?dist}
Summary:        Microsoft Azure Development Tools for SDK
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Development tools for Python-based Azure tools
This package contains tools to aid in developing Python-based Azure code.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -c -n %{srcname}-%{commit}


%build
# Allow for newer versions of vcrpy.
sed -i 's/vcrpy==3.0.0/vcrpy>=3.0.0/' %{reponame}-%{commit}/tools/azure-devtools/setup.py

# Bring down the README.rst and LICENSE.
cp %{reponame}-%{commit}/{LICENSE.txt,README.rst} .

pushd %{reponame}-%{commit}/tools/azure-devtools
    %pyproject_wheel
popd


%install
%pyproject_install
%pyproject_save_files azure_devtools

%if %{with tests}
%check
# NOTE(mhayden): The bot_framework/github_tools Tests are looking for
# `github.tests`, which don't appear to be in Fedora's version of
# python3-pygithub.
# Bug opened: https://github.com/Azure/azure-sdk-for-python/issues/19129
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/perfstress
%{_bindir}/systemperf


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.1~git.1.aa29c1c
- First package.
