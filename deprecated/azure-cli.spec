# Tests are enabled by default
%bcond_without tests

%global         srcname         azure-cli
Version:        2.24.2
%global         forgeurl        https://github.com/Azure/azure-cli
%global         tag             %{srcname}-%{version}
%global         distprefix      %{nil}
%forgemeta

Name:           azure-cli
Release:        1%{?dist}
Summary:        Microsoft Azure Command-Line Tools

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-argcomplete
BuildRequires:  python%{python3_pkgversion}-asn1crypto
BuildRequires:  python%{python3_pkgversion}-bcrypt
BuildRequires:  python%{python3_pkgversion}-certifi
BuildRequires:  python%{python3_pkgversion}-cffi
BuildRequires:  python%{python3_pkgversion}-chardet
BuildRequires:  python%{python3_pkgversion}-colorama
BuildRequires:  python%{python3_pkgversion}-configargparse
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-humanfriendly
BuildRequires:  python%{python3_pkgversion}-idna
BuildRequires:  python%{python3_pkgversion}-invoke
BuildRequires:  python%{python3_pkgversion}-isodate
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-jmespath
BuildRequires:  python%{python3_pkgversion}-jsmin
BuildRequires:  python%{python3_pkgversion}-jwt
BuildRequires:  python%{python3_pkgversion}-knack
BuildRequires:  python%{python3_pkgversion}-markupsafe
BuildRequires:  python%{python3_pkgversion}-msal
BuildRequires:  python%{python3_pkgversion}-msrest
BuildRequires:  python%{python3_pkgversion}-msrestazure
BuildRequires:  python%{python3_pkgversion}-oauthlib
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-paramiko
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-pkginfo
BuildRequires:  python%{python3_pkgversion}-portalocker
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-pycparser
BuildRequires:  python%{python3_pkgversion}-pygithub
BuildRequires:  python%{python3_pkgversion}-pyOpenSSL
BuildRequires:  python%{python3_pkgversion}-pynacl
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytz
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-requests-oauthlib
BuildRequires:  python%{python3_pkgversion}-scp
BuildRequires:  python%{python3_pkgversion}-semver
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sshtunnel
BuildRequires:  python%{python3_pkgversion}-tabulate
BuildRequires:  python%{python3_pkgversion}-urllib3
BuildRequires:  python%{python3_pkgversion}-wcwidth
BuildRequires:  python%{python3_pkgversion}-websocket-client
BuildRequires:  python%{python3_pkgversion}-wrapt
BuildRequires:  python%{python3_pkgversion}-xmltodict

BuildRequires:  %{py3_dist azure-core}
BuildRequires:  %{py3_dist azure-mgmt-advisor}
BuildRequires:  %{py3_dist azure-mgmt-apimanagement}
BuildRequires:  %{py3_dist azure-mgmt-appconfiguration}
BuildRequires:  %{py3_dist azure-mgmt-applicationinsights}
BuildRequires:  %{py3_dist azure-mgmt-authorization}
BuildRequires:  %{py3_dist azure-mgmt-batch}
BuildRequires:  %{py3_dist azure-mgmt-billing}
BuildRequires:  %{py3_dist azure-mgmt-botservice}
BuildRequires:  %{py3_dist azure-mgmt-cdn}
BuildRequires:  %{py3_dist azure-mgmt-cognitiveservices}
BuildRequires:  %{py3_dist azure-mgmt-compute}
BuildRequires:  %{py3_dist azure-mgmt-consumption}
BuildRequires:  %{py3_dist azure-mgmt-containerinstance}
BuildRequires:  %{py3_dist azure-mgmt-containerregistry}
BuildRequires:  %{py3_dist azure-mgmt-containerservice}
BuildRequires:  %{py3_dist azure-mgmt-core}
BuildRequires:  %{py3_dist azure-mgmt-cosmosdb}
BuildRequires:  %{py3_dist azure-mgmt-databoxedge}
BuildRequires:  %{py3_dist azure-mgmt-datalake-analytics}
BuildRequires:  %{py3_dist azure-mgmt-datalake-store}
BuildRequires:  %{py3_dist azure-mgmt-datamigration}
BuildRequires:  %{py3_dist azure-mgmt-deploymentmanager}
BuildRequires:  %{py3_dist azure-mgmt-devtestlabs}
BuildRequires:  %{py3_dist azure-mgmt-dns}
BuildRequires:  %{py3_dist azure-mgmt-eventgrid}
BuildRequires:  %{py3_dist azure-mgmt-eventhub}
BuildRequires:  %{py3_dist azure-mgmt-hdinsight}
BuildRequires:  %{py3_dist azure-mgmt-imagebuilder}
BuildRequires:  %{py3_dist azure-mgmt-iotcentral}
BuildRequires:  %{py3_dist azure-mgmt-iothub}
BuildRequires:  %{py3_dist azure-mgmt-iothubprovisioningservices}
BuildRequires:  %{py3_dist azure-mgmt-keyvault}
BuildRequires:  %{py3_dist azure-mgmt-kusto}
BuildRequires:  %{py3_dist azure-mgmt-loganalytics}
BuildRequires:  %{py3_dist azure-mgmt-managementgroups}
BuildRequires:  %{py3_dist azure-mgmt-maps}
BuildRequires:  %{py3_dist azure-mgmt-marketplaceordering}
BuildRequires:  %{py3_dist azure-mgmt-media}
BuildRequires:  %{py3_dist azure-mgmt-monitor}
BuildRequires:  %{py3_dist azure-mgmt-msi}
BuildRequires:  %{py3_dist azure-mgmt-netapp}
BuildRequires:  %{py3_dist azure-mgmt-network}
BuildRequires:  %{py3_dist azure-mgmt-policyinsights}
BuildRequires:  %{py3_dist azure-mgmt-privatedns}
BuildRequires:  %{py3_dist azure-mgmt-rdbms}
BuildRequires:  %{py3_dist azure-mgmt-recoveryservices}
BuildRequires:  %{py3_dist azure-mgmt-recoveryservicesbackup}
BuildRequires:  %{py3_dist azure-mgmt-redhatopenshift}
BuildRequires:  %{py3_dist azure-mgmt-redis}
BuildRequires:  %{py3_dist azure-mgmt-relay}
BuildRequires:  %{py3_dist azure-mgmt-reservations}
BuildRequires:  %{py3_dist azure-mgmt-resource}
BuildRequires:  %{py3_dist azure-mgmt-search}
BuildRequires:  %{py3_dist azure-mgmt-security}
BuildRequires:  %{py3_dist azure-mgmt-servicebus}
BuildRequires:  %{py3_dist azure-mgmt-servicefabric}
BuildRequires:  %{py3_dist azure-mgmt-servicefabricmanagedclusters}
BuildRequires:  %{py3_dist azure-mgmt-signalr}
BuildRequires:  %{py3_dist azure-mgmt-sql}
BuildRequires:  %{py3_dist azure-mgmt-sqlvirtualmachine}
BuildRequires:  %{py3_dist azure-mgmt-storage}
BuildRequires:  %{py3_dist azure-mgmt-synapse}
BuildRequires:  %{py3_dist azure-mgmt-trafficmanager}
BuildRequires:  %{py3_dist azure-mgmt-web}
%endif

%description
%{summary}


%package python-azure-cli-core
Version: %{version}
Summary: Microsoft Azure Command-Line Tools Core Module

%description python-azure-cli-core
Microsoft Azure Command-Line Tools Core Module


%package python-azure-cli-telemetry
Version: %{version}
Summary: Microsoft Azure CLI Telemetry

%description python-azure-cli-telemetry
Microsoft Azure CLI Telemetry


%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
for PROJECT in azure-cli azure-cli-core azure-cli-telemetry; do
    pushd "src/${PROJECT}"
        %pyproject_wheel
    popd
done


%install
%pyproject_install

# Batch scripts are only for windows.
rm -f %{buildroot}%{_bindir}/az.bat

# Install the az bash completion script properly.
install -D -p -m 0644 %{buildroot}%{_bindir}/az.completion.sh \
    %{buildroot}%{_sysconfdir}/bash-completion.d/azure-cli
rm -f %{buildroot}%{_bindir}/az.completion.sh


%if %{with tests}
%check
%pytest
%endif


%files
%license LICENSE.txt
%{_bindir}/az
%{_sysconfdir}/bash-completion.d/azure-cli
%{python3_sitelib}/azure/cli/__main__.py
%{python3_sitelib}/azure/cli/__pycache__/__main__.cpython-39*.pyc
%{python3_sitelib}/azure/cli/command_modules
%{python3_sitelib}/azure_cli-*.dist-info

%files python-azure-cli-core
%{python3_sitelib}/azure/cli/core
%{python3_sitelib}/azure_cli_core-*.dist-info

%files python-azure-cli-telemetry
%{python3_sitelib}/azure/cli/telemetry
%{python3_sitelib}/azure_cli_telemetry-*.dist-info

%changelog
* Wed Jun 02 2021 Major Hayden <major@mhtx.net> - 2.24.2-1
- First package.
