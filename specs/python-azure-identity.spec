%global         srcname     azure-identity

Name:           python-%{srcname}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Microsoft Azure Identity Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Microsoft Azure Identity Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.6.0-1
- First package.
