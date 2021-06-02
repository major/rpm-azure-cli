%global srcname azure-core

Name:           python-%{srcname}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Azure Core shared client library for Python

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Azure Core shared client library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove strict version requirement for azure-core.
sed -i 's/"azure-core.*",$/"azure-core",/' setup.py

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.14.0-1
- First package.
