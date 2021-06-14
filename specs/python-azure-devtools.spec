# The azure-devtools package is used to help test various parts of the Azure
# SDK components. It isn't released to pypi, but it is available from GitHub.
# However, the git repository is huge (150MB) since it contains 220+ Python
# packages.
# Use the generate-devtools-tarball.sh script to generate the source for this
# package without all of the additional packages from the upstream repository.
%global         srcname         azure-devtools
%global         commit          aa29c1cb5da14ab3efca04dc3838b473a88536d4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         distprefix      %{nil}
%global         short_version   1.2.1

# tests are enabled by default
%bcond_without  tests

Name:           python-%{srcname}
Version:        %{short_version}~git.1.%{shortcommit}
Release:        1%{?dist}
Summary:        Microsoft Azure Development Tools for SDK
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/
Source0:        azure-devtools-%{commit}.tar.gz
Source1:        generate-devtools-tarball.sh

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-aiohttp
BuildRequires:  python3-configargparse
BuildRequires:  python3-GitPython
BuildRequires:  python3-httpx
BuildRequires:  python3-pycurl
BuildRequires:  python3-pygithub
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-tornado
BuildRequires:  python3-vcrpy
%endif



%global _description %{expand:
Development tools for Python-based Azure tools
This package contains tools to aid in developing Python-based Azure code.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -c -n %{srcname}-%{commit}

# Allow for versions of python-vcrpy later than 3.0.0.
sed -i 's/vcrpy==3.0.0/vcrpy>=3.0.0/' setup.py

%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
# NOTE(mhayden): The bot_framework/github_tools Tests are looking for
# `github.tests`, which don't appear to be in Fedora's version of
# python3-pygithub.
# Bug opened: https://github.com/Azure/azure-sdk-for-python/issues/19129
#
# The remaining tests are skipped because they require network access.
%pytest --ignore src/azure_devtools/ci_tools/tests/test_bot_framework.py \
    --ignore src/azure_devtools/ci_tools/tests/test_github_tools.py \
    --ignore src/azure_devtools/ci_tools/tests/test_git_tools.py \
    --ignore src/azure_devtools/scenario_tests/tests/async_tests/test_preparer_async.py \
    --ignore src/azure_devtools/scenario_tests/tests/test_preparer_order.py \
    --ignore src/azure_devtools/scenario_tests/tests/test_recording_processor.py \
    -k "not test_get_sha1_hash and not test_preparer_async_handling"
%endif


%files -n python3-%{srcname}
%{_bindir}/perfstress
%{_bindir}/systemperf
%{python3_sitelib}/azure_devtools
%{python3_sitelib}/azure_devtools-%{short_version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.1~git.1.19e35d6
- First package.
