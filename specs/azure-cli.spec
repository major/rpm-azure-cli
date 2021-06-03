%{?!python3_pkgversion:%global python3_pkgversion 3}

%global         srcname     azure-cli

Name:           %{srcname}
Version:        2.24.2
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Microsoft Azure Command-Line Tools


%prep
%autosetup -n %{srcname}-%{version}

# Allow for newer versions of certain python components.
sed -i "s/antlr4-python3-runtime~=4.7.2/antlr4-python3-runtime>=4.7.2/" setup.py
sed -i "s/javaproperties==0.5.1/javaproperties>=0.5.1/" setup.py
sed -i "s/jsondiff==1.2.0/jsondiff>=1.2.0/" setup.py
sed -i "s/PyGithub==1.38/PyGithub>=1.38/" setup.py
sed -i "s/pytz==2019.1/pytz>=2019.1/" setup.py
sed -i "s/urllib3\[secure\]>=1.25.9,<2.0.0/urllib3>=1.25.9/" setup.py
sed -i "s/websocket-client~=0.56.0/websocket-client>=0.56.0/" setup.py

# CLI depends on 3.0.0rc9 of eventgrid, but that version is malformed. Just use
# use any version 3.0.0 or higher.
sed -i "s/azure-mgmt-eventgrid==3.0.0rc9/azure-mgmt-eventgrid>=3.0.0/" setup.py

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
%{_sysconfdir}/bash-completion.d/%{srcname}


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
