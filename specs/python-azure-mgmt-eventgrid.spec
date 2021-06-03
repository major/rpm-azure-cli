%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-mgmt-eventgrid

Name:           python-%{srcname}
Version:        9.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure EventGrid Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure EventGrid Management Client Library for Python}

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
%{python3_sitelib}/azure/mgmt/eventgrid
%{python3_sitelib}/azure_mgmt_eventgrid-*.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 9.0.0-1
- First package.
