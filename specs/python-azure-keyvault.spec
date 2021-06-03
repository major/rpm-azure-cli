%global         srcname     azure-keyvault

Name:           python-%{srcname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Key Vault Client Libraries for Python}

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
%{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure_keyvault-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.1.0-1
- First package.
