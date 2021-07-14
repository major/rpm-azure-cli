%global         srcname     azure-cli

Name:           %{srcname}
Version:        2.26.1
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
Patch0:         azure-cli-requirements-fix.patch

BuildArch:      noarch

# The telemetry library is an optional requirement in the python requirements
# list, but the `az` command throws errors if it is not present.
Requires:       python-azure-cli-telemetry

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

Conflicts:      python3-azure-sdk

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
%doc README.rst HISTORY.rst
%license LICENSE.txt
%{_bindir}/az
%{_sysconfdir}/bash-completion.d/%{srcname}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.26.1-1
- First package.
