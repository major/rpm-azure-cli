%global         srcname     azure-common

Name:           python-%{srcname}
Version:        1.1.27
Release:        1%{?dist}
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
Microsoft Azure Client Library for Python (Common)}

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
%{python3_sitelib}/azure/common
%{python3_sitelib}/azure/profiles
%{python3_sitelib}/azure_common-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 1.1.27-1
- First package.
