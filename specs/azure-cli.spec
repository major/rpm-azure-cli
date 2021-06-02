%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-cli

Name:           python-%{srcname}
Version:        2.24.2
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%description
Microsoft Azure Command-Line Tools

%{py3_provides} python3-%{srcname}


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
%{python3_sitelib}/azure/cli/
%{python3_sitelib}/azure_cli-*.egg-info
%{_bindir}/az
%{_sysconfdir}/bash-completion.d/azure-cli


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
