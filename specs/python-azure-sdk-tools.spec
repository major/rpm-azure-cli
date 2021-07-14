%global         reponame        azure-sdk-for-python
%global         srcname         azure-sdk-tools
%global         forgeurl        https://github.com/Azure/%{reponame}/
%global         commit          aa29c1cb5da14ab3efca04dc3838b473a88536d4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         distprefix      %{nil}
%global         short_version   0.0.0
%forgemeta

# Tests are disabled here because the testing code within this package depends
# on the entire repository being checked out, installed, and added to
# PYTHONPATH.
%bcond_with     tests

Name:           python-%{srcname}
Version:        %{short_version}~git.1.%{shortcommit}
Release:        1%{?dist}
Summary:        Specific tools for Azure SDK for Python testing
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
Specific tools for Azure SDK for Python testing}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -c -n %{srcname}-%{commit}


%build
# Bring down the README.rst and LICENSE.
cp %{reponame}-%{commit}/{LICENSE.txt,README.rst} .

pushd %{reponame}-%{commit}/tools/azure-sdk-tools
    # Some tools are only used for the Azure SDK CI system and there's no need
    # to package those.
    rm -rf packaging_tools pypi_tools

    # Some requirements are only used by packaging tools and can be removed.
    sed -i '/azure-storage-common/d' setup.py
    sed -i '/json-delta/d' setup.py
    sed -i '/pytoml/d' setup.py

    # There's a dangling empty setup.py in the devtools_testutils directory.
    rm -f devtools_testutils/setup.py

    %pyproject_wheel
popd


%install
%pyproject_install

# Some provided executables are only used internally in Azure SDK's CI.
rm -f %{buildroot}/%{_bindir}/{auto_codegen,auto_package,generate_package,generate_sdk}

%pyproject_save_files devtools_testutils testutils


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.0~git.1.aa29c1c
- First package.
