%global         srcname     azure-keyvault-administration

Name:           python-%{srcname}
Version:        4.0.0b3
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Administration Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description %{expand:
Microsoft Azure Key Vault Administration Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides    python3-azure-keyvault

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.md
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%dir %{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure/keyvault/administration
%{python3_sitelib}/azure_keyvault_administration-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 4.0.0b3-1
- First package.
