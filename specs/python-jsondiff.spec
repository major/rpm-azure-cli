%global         srcname     jsondiff

Name:           python-%{srcname}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Diff JSON and JSON-like structures in Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Diff JSON and JSON-like structures in Python}

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


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/jdiff
%{_bindir}/%{srcname}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.3.0-1
- First package.
