%global         srcname         azure-mgmt-billing

Name:           python-%{srcname}
Version:        6.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Python SDK - Resource Management - Billing

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

%global _description %{expand:
Microsoft Azure Python SDK - Resource Management - Billing}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure/mgmt/billing

# %check
# %{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Wed May 26 2021 Major Hayden <major@mhtx.net> - 6.0.0-1
- First package.