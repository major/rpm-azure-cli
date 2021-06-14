# The azure-sdk-tools package is used to help test various parts of the Azure
# SDK components. It isn't released to pypi, but it is available from GitHub.
# However, the git repository is huge (150MB) since it contains 220+ Python
# packages.
# Use the generate-sdk-tools-tarball.sh script to generate the source for this
# package without all of the additional packages from the upstream repository.
%global         srcname         azure-sdk-tools
%global         commit          aa29c1cb5da14ab3efca04dc3838b473a88536d4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         distprefix      %{nil}
%global         short_version   0.0.0

# tests are enabled by default
%bcond_without  tests

Name:           python-%{srcname}
Version:        %{short_version}~git.1.%{shortcommit}
Release:        1%{?dist}
Summary:        Specific tools for Azure SDK for Python testing
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/
Source0:        azure-sdk-tools-%{commit}.tar.gz
Source1:        generate-sdk-tools-tarball.sh

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-dotenv

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
%endif



%global _description %{expand:
Specific tools for Azure SDK for Python testing}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -c -n %{srcname}-%{commit}

# There are jinja2 templates that end in .py in packaging_tools/templates and
# they won't byte compile properly since they're templates and not true python
# code. We can move them out of the way and move them back at the end.
mkdir hold_templates
mv packaging_tools/templates/*.py hold_templates/


%build
%py3_build


%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
%py_byte_compile %{python3} %{buildroot}%{_datadir}/packaging_tools
%py_byte_compile %{python3} %{buildroot}%{_datadir}/devtools_testutils

# Move the templates back into place.
mkdir -p %{buildroot}%{python3_sitelib}/packaging_tools/templates
mv hold_templates/*.py %{buildroot}%{python3_sitelib}/packaging_tools/templates/

%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname}
%{python3_sitelib}/packaging_tools
%{python3_sitelib}/devtools_testutils


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.0~git.1.19e35d6
- First package.
