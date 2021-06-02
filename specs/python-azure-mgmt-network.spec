%global srcname azure-mgmt-network

Name:           python-%{srcname}
Version:        19.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Network Management Client Library for Python

License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Network Management Client Library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p0 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 19.0.0-1
- First package.
