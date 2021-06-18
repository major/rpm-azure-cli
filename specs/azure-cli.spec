%global         srcname     azure-cli

Name:           %{srcname}
Version:        2.25.0
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
Patch0:         azure-cli-sane-versions.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%description
Microsoft Azure Command-Line Tools


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure

# Batch scripts are only for windows.
rm -f %{buildroot}%{_bindir}/az.bat

# Install the az bash completion script properly.
install -D -p -m 0644 %{buildroot}%{_bindir}/az.completion.sh \
    %{buildroot}%{_sysconfdir}/bash-completion.d/azure-cli
rm -f %{buildroot}%{_bindir}/az.completion.sh


%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/az
%{_sysconfdir}/bash-completion.d/%{srcname}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.25.0-1
- First package.
