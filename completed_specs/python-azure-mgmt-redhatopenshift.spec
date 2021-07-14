%global         srcname     azure-mgmt-redhatopenshift

%bcond_without  tests

Name:           python-%{srcname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Red Hat Openshift Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-azure-devtools < 5.0.0
%endif

%global _description %{expand:
Microsoft Azure Red Hat Openshift Management Client Library for Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.0.0-1
- First package.
