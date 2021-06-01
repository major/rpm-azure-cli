%global srcname azure-devtools

Name:           python-%{srcname}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Development tools for Python-based Azure tools

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Development tools for Python-based Azure tools}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure_devtools


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.2.0-1
- First package.
