%global         srcname     applicationinsights

Name:           python-%{srcname}
Version:        0.11.10
Release:        1%{?dist}
Summary:        This project extends the Application Insights API surface to support Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
This project extends the Application Insights API surface to support Python}

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
%pyproject_save_files applicationinsights


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.11.10-1
- First package.
