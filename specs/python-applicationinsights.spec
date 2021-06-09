%global         srcname     applicationinsights

Name:           python-%{srcname}
Version:        0.11.10
Release:        1%{?dist}
Summary:        This project extends the Application Insights API surface to support Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This project extends the Application Insights API surface to support Python}

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
%license LICENSE.TXT
%doc README.rst
%{python3_sitelib}/applicationinsights
%{python3_sitelib}/applicationinsights-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 0.11.10-1
- First package.
