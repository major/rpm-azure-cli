%global         srcname     vsts

Name:           python-%{srcname}
Version:        0.1.25
Release:        1%{?dist}
Summary:        Python wrapper around the VSTS APIs
License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Python wrapper around the VSTS APIs}

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
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jun 02 2021 Major Hayden <major@mhtx.net> - 0.1.25-1
- First package.
