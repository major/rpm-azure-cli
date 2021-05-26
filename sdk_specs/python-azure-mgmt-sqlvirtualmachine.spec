%global         srcname         azure-mgmt-sqlvirtualmachine

Name:           python-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

%global _description %{expand:
Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure/mgmt/sqlvirtualmachine

# %check
# %{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
* Wed May 26 2021 Major Hayden <major@mhtx.net> - 0.5.0-1
- First package.