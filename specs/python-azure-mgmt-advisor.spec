%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-mgmt-advisor

Name:           python-%{srcname}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Microsoft Azure Advisor Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Advisor Client Library for Python}

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
%{python3_sitelib}/azure/mgmt/advisor
%{python3_sitelib}/azure_mgmt_advisor-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.0.1-1
- First package.
