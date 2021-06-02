%{?!python3_pkgversion:%global python3_pkgversion 3}

# tests are enabled by default
%bcond_without tests

%global         srcname     avro

Name:           python-%{srcname}
Version:        1.10.2
Release:        1%{?dist}
Summary:        Apache Avro is a data serialization system
License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif


%global _description %{expand:
Apache Avro is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not required to
  read or write data files nor to use or implement RPC protocols. Code
  generation as an optional optimization, only worth implementing for
  statically typed languages.}
%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove shebang from non-executable python files.
PYTHON_FILES=$(find . -name '*.py')
for lib in $PYTHON_FILES; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


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
%license %{python3_sitelib}/avro/LICENSE
%{python3_sitelib}/avro
%{python3_sitelib}/avro-*.egg-info
%{_bindir}/avro

%changelog
* Wed Jun 02 2021 Major Hayden <major@mhtx.net> - 1.10.2-1
- First package.
