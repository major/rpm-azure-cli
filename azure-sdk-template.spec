%global         srcname         {{ srcname }}

Name:           python-%{srcname}
Version:        {{ version }}
Release:        1%{?dist}
Summary:        {{ summary }}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version} {{ extension }}}

BuildArch:      noarch

%global _description %{expand:
{{ summary }}}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files {{ slashed_srcname }}

# %check
# %{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
* Wed May 26 2021 Major Hayden <major@mhtx.net> - {{ version }}-1
- First package.
