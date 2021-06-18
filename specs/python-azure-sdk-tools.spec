%global         srcname         azure-sdk-tools
%global         forgeurl        https://github.com/azure/azure-sdk-for-python
%global         commit          d3930215a1bf184f3cb3f104884a46609cb85ef2
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         distprefix      %{nil}
%global         short_version   0.0.0
%forgemeta

# tests are enabled by default
%bcond_without  tests

Name:           python-%{srcname}
Version:        %{short_version}~git.1.%{shortcommit}
Release:        1%{?dist}
Summary:        Specific tools for Azure SDK for Python testing
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Patch0:         python-azure-sdk-tools-sane-requirements.patch

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-dotenv
BuildRequires:  pyproject-rpm-macros
BuildRequires:  make

%if %{with tests}
BuildRequires:  python-azure-mgmt-keyvault
BuildRequires:  python-azure-mgmt-resource
BuildRequires:  python-azure-mgmt-storage
BuildRequires:  python-azure-storage-common
BuildRequires:  python%{python3_pkgversion}-pyOpenSSL
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  python%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-readme-renderer
%endif


%global _description %{expand:
Specific tools for Azure SDK for Python testing}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%forgesetup


%build
pushd tools/azure-sdk-tools
    %pyproject_wheel
popd


%generate_buildrequires
pushd tools/azure-sdk-tools
    %pyproject_buildrequires
popd


%install
%pyproject_install
%pyproject_save_files azure


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.0~git.1.d393021
- First package.
