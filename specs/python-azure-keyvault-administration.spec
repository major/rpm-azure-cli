%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-keyvault-administration

Name:           python-%{srcname}
Version:        4.0.0b3
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Administration Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Key Vault Administration Client Library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/azure/keyvault/administration
%{python3_sitelib}/azure_keyvault_administration-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 4.0.0b3-1
- First package.
