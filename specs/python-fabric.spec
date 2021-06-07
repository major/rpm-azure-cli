%global         srcname     fabric

# Tests are disabled by default. 😞
# Enable if https://bugzilla.redhat.com/show_bug.cgi?id=1949502 /
# https://github.com/bitprophet/pytest-relaxed/issues/12 is resolved:
%bcond_with     tests

Name:           python-%{srcname}
Version:        2.6.0
Release:        1%{?dist}
Summary:        High level SSH command execution
License:        BSD
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
# Use built-in unittest.mock in python 3.
# https://github.com/fabric/fabric/pull/2168
Patch0:         python-fabric-Use-standard-library-unittest.mock-on-Python-3.6-and.patch
# Use built-in pathlib in python 3.
# https://github.com/fabric/fabric/pull/2167
Patch1:         python-fabric-Put-conditional-unittest.mock-imports-last-to-placat.patch
# Fall back to system modules if vendorized ones do not exist.
# https://github.com/fabric/fabric/pull/2169
Patch2:         python-fabric-Finish-wrapping-invoke.vendor.-imports-so-standalone.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Runtime dependencies, needed for testing
BuildRequires:  python3-invoke
BuildRequires:  python3-paramiko
# Runtime dependencies upstream assumed would be vendored with invoke, but
# which we must use standalone
BuildRequires:  python%{python3_pkgversion}-decorator
BuildRequires:  python%{python3_pkgversion}-lexicon
BuildRequires:  python%{python3_pkgversion}-six


%if %{with tests}
# Extra pytest (a superset of extra testing)
BuildRequires:  python3-pytest
# Missing from setup.py (only in requirements-dev.txt), but still needed for
# testing:
BuildRequires:  python3-pytest-relaxed
%endif

BuildRequires:  help2man

%global _description %{expand:
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build

# Entry point script that allows us to use help2man before installing
cat > fab <<'EOF'
#!%{__python3}
from fabric.main import program
program.run()
EOF
chmod +x fab
PYTHONPATH="${PWD}" help2man --no-info --output fab.1 ./fab

%install
%py3_install

install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 -p fab.1


%check
%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/fab
%{_mandir}/man1/fab.1*
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.6.0-1
- First package.
