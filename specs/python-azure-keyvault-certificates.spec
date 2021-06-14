%global         srcname     azure-keyvault-certificates

Name:           python-%{srcname}
Version:        4.2.1
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Certificates Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools



%global _description %{expand:
Microsoft Azure Key Vault Certificates Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install

# Clean up files left at the base package directory.
rm -f %{buildroot}%{python3_sitelib}/azure/__init__.py \
    %{buildroot}%{python3_sitelib}/azure/__pycache__/__init__.cpython-*.pyc

%files -n python3-%{srcname}
%doc README.md
# Co-owned namespace package directory
%dir %{python3_sitelib}/azure
%dir %{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure/keyvault/certificates
%{python3_sitelib}/azure_keyvault_certificates-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 4.2.1-1
- First package.
