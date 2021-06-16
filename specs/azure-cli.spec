%global         srcname     azure-cli

Name:           %{srcname}
Version:        2.24.2
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source
Patch0:         azure-cli-sane-versions.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Microsoft Azure Command-Line Tools


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install

# Batch scripts are only for windows.
rm -f %{buildroot}%{_bindir}/az.bat

# Install the az bash completion script properly.
install -D -p -m 0644 %{buildroot}%{_bindir}/az.completion.sh \
    %{buildroot}%{_sysconfdir}/bash-completion.d/azure-cli
rm -f %{buildroot}%{_bindir}/az.completion.sh


%files
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/cli/
%{python3_sitelib}/azure_cli-%{version}-py%{python3_version}.egg-info
%{_bindir}/az
%{_sysconfdir}/bash-completion.d/%{srcname}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
