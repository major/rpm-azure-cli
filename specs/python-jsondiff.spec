%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     jsondiff

Name:           python-%{srcname}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Diff JSON and JSON-like structures in Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Diff JSON and JSON-like structures in Python}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/jsondiff
%{python3_sitelib}/jsondiff-*.egg-info
%{_bindir}/jdiff
%{_bindir}/jsondiff


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.3.0-1
- First package.
