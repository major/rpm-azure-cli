%global         srcname     azure-keyvault

Name:           python-%{srcname}
Version:        4.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Microsoft Azure Key Vault Client Libraries for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/azure_keyvault-%{version}.dist-info/


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 4.1.0
- First package.
