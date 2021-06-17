%global         srcname     azure-datalake-store

Name:           python-%{srcname}
Version:        0.0.52
Release:        1%{?dist}
Summary:        Azure Data Lake Store Filesystem Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

Obsoletes:      python-azure-sdk < 5.0.1

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Azure Data Lake Store Filesystem Client Library for Python}

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

# Remove the samples since many of them are empty or have wrong line endings.
rm -rf %{buildroot}%{python3_sitelib}/samples


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.0.52-1
- First package.
