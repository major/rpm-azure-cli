%global         srcname         msrestazure

Name:           python-%{srcname}
Version:        0.6.4
Release:        1%{?dist}
Summary:        Microsoft Azure Python SDK - MsRest Azure

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version} tar.gz}

BuildArch:      noarch

%global _description %{expand:
Microsoft Azure Python SDK - MsRest Azure}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*' +auto

# %check
# %{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
* Wed May 26 2021 Major Hayden <major@mhtx.net> - 0.6.4-1
- First package.