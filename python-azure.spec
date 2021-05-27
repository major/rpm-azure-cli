# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Missing dependencies for tests
%bcond_with check

Name:           python-azure
Version:        20210527
Release:        1%{?dist}

Summary:        Azure SDK for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        %{pypi_source azure-mgmt-advisor 9.0.0 zip}
Source1:        %{pypi_source azure-mgmt-apimanagement 2.0.0 zip}
Source2:        %{pypi_source azure-mgmt-appconfiguration 1.0.1 zip}
Source3:        %{pypi_source azure-mgmt-applicationinsights 1.0.0 zip}
Source4:        %{pypi_source azure-mgmt-authorization 1.0.0 zip}
Source5:        %{pypi_source azure-mgmt-batch 15.0.0 zip}
Source6:        %{pypi_source azure-mgmt-batchai 2.0.0 zip}
Source7:        %{pypi_source azure-mgmt-billing 6.0.0 zip}
Source8:        %{pypi_source azure-mgmt-botservice 1.0.0 zip}
Source9:        %{pypi_source azure-mgmt-cdn 11.0.0 zip}
Source10:       %{pypi_source azure-mgmt-cognitiveservices 11.0.0 zip}
Source11:       %{pypi_source azure-mgmt-compute 21.0.0 zip}
Source12:       %{pypi_source azure-mgmt-consumption 8.0.0 zip}
Source13:       %{pypi_source azure-mgmt-containerinstance 7.0.0 zip}
Source14:       %{pypi_source azure-mgmt-containerregistry 8.0.0 zip}
Source15:       %{pypi_source azure-mgmt-containerservice 15.1.0 zip}
Source16:       %{pypi_source azure-mgmt-core 1.2.2 zip}
Source17:       %{pypi_source azure-mgmt-cosmosdb 6.3.0 zip}
Source18:       %{pypi_source azure-mgmt-databoxedge 1.0.0 zip}
Source19:       %{pypi_source azure-mgmt-datalake-analytics 0.6.0 zip}
Source20:       %{pypi_source azure-mgmt-datalake-nspkg 3.0.1 zip}
Source21:       %{pypi_source azure-mgmt-datalake-store 0.5.0 zip}
Source22:       %{pypi_source azure-mgmt-datamigration 9.0.0 zip}
Source23:       %{pypi_source azure-mgmt-deploymentmanager 1.0.0 zip}
Source24:       %{pypi_source azure-mgmt-devtestlabs 9.0.0 zip}
Source25:       %{pypi_source azure-mgmt-dns 8.0.0 zip}
Source26:       %{pypi_source azure-mgmt-eventgrid 9.0.0 zip}
Source27:       %{pypi_source azure-mgmt-eventhub 9.0.0 zip}
Source28:       %{pypi_source azure-mgmt-hdinsight 7.0.0 zip}
Source29:       %{pypi_source azure-mgmt-imagebuilder 0.4.0 zip}
Source30:       %{pypi_source azure-mgmt-iotcentral 4.1.0 zip}
Source31:       %{pypi_source azure-mgmt-iothub 2.0.0 zip}
Source32:       %{pypi_source azure-mgmt-iothubprovisioningservices 0.2.0 zip}
Source33:       %{pypi_source azure-mgmt-keyvault 9.0.0 zip}
Source34:       %{pypi_source azure-mgmt-kusto 2.0.0 zip}
Source35:       %{pypi_source azure-mgmt-loganalytics 10.0.0 zip}
Source36:       %{pypi_source azure-mgmt-managedservices 6.0.0 zip}
Source37:       %{pypi_source azure-mgmt-managementgroups 1.0.0 zip}
Source38:       %{pypi_source azure-mgmt-maps 2.0.0 zip}
Source39:       %{pypi_source azure-mgmt-marketplaceordering 1.1.0 zip}
Source40:       %{pypi_source azure-mgmt-media 3.1.0 zip}
Source41:       %{pypi_source azure-mgmt-monitor 2.0.0 zip}
Source42:       %{pypi_source azure-mgmt-msi 1.0.0 zip}
Source43:       %{pypi_source azure-mgmt-netapp 3.0.0 zip}
Source44:       %{pypi_source azure-mgmt-network 19.0.0 zip}
Source45:       %{pypi_source azure-mgmt-nspkg 3.0.2 zip}
Source46:       %{pypi_source azure-mgmt-policyinsights 1.0.0 zip}
Source47:       %{pypi_source azure-mgmt-privatedns 1.0.0 zip}
Source48:       %{pypi_source azure-mgmt-rdbms 8.0.0 zip}
Source49:       %{pypi_source azure-mgmt-recoveryservices 1.0.0 zip}
Source50:       %{pypi_source azure-mgmt-recoveryservicesbackup 0.11.0 zip}
Source51:       %{pypi_source azure-mgmt-redhatopenshift 1.0.0 zip}
Source52:       %{pypi_source azure-mgmt-redis 12.0.0 zip}
Source53:       %{pypi_source azure-mgmt-relay 1.0.0 zip}
Source54:       %{pypi_source azure-mgmt-reservations 1.0.0 zip}
Source55:       %{pypi_source azure-mgmt-resource 18.0.0 zip}
Source56:       %{pypi_source azure-mgmt-search 8.0.0 zip}
Source57:       %{pypi_source azure-mgmt-security 1.0.0 zip}
Source58:       %{pypi_source azure-mgmt-servicebus 6.0.0 zip}
Source59:       %{pypi_source azure-mgmt-sql 2.1.0 zip}
Source60:       %{pypi_source azure-mgmt-sqlvirtualmachine 0.5.0 zip}
Source61:       %{pypi_source azure-mgmt-storage 18.0.0 zip}
Source62:       %{pypi_source azure-mgmt-synapse 2.0.0 zip}
Source63:       %{pypi_source azure-mgmt-trafficmanager 0.51.0 zip}
Source64:       %{pypi_source azure-mgmt-web 3.0.0 zip}
Source65:       %{pypi_source azure-nspkg 3.0.2 zip}
Source66:       %{pypi_source azure-storage-common 2.1.0 tar.gz}


BuildArch:      noarch

Obsoletes:      python-azure-sdk == 5.0.0-4

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

BuildRequires:  tree

%if %{with check}
# DOOT
%endif

%description
Azure SDK for Python


%package mgmt-advisor
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Advisor

%description mgmt-advisor
Microsoft Azure Python SDK - Resource Management - Advisor

%package mgmt-apimanagement
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - API Management

%description mgmt-apimanagement
Microsoft Azure Python SDK - Resource Management - API Management

%package mgmt-appconfiguration
Version: 1.0.1
Summary: Microsoft Azure Python SDK - Resource Management - App Configuration

%description mgmt-appconfiguration
Microsoft Azure Python SDK - Resource Management - App Configuration

%package mgmt-applicationinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Application Insights

%description mgmt-applicationinsights
Microsoft Azure Python SDK - Resource Management - Application Insights

%package mgmt-authorization
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Authorization

%description mgmt-authorization
Microsoft Azure Python SDK - Resource Management - Authorization

%package mgmt-batch
Version: 15.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Batch

%description mgmt-batch
Microsoft Azure Python SDK - Resource Management - Batch

%package mgmt-batchai
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Batch AI

%description mgmt-batchai
Microsoft Azure Python SDK - Resource Management - Batch AI

%package mgmt-billing
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Billing

%description mgmt-billing
Microsoft Azure Python SDK - Resource Management - Billing

%package mgmt-botservice
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Bot Service

%description mgmt-botservice
Microsoft Azure Python SDK - Resource Management - Bot Service

%package mgmt-cdn
Version: 11.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Content Delivery Network

%description mgmt-cdn
Microsoft Azure Python SDK - Resource Management - Content Delivery Network

%package mgmt-cognitiveservices
Version: 11.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Cognitive Services

%description mgmt-cognitiveservices
Microsoft Azure Python SDK - Resource Management - Cognitive Services

%package mgmt-compute
Version: 21.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Compute

%description mgmt-compute
Microsoft Azure Python SDK - Resource Management - Compute

%package mgmt-consumption
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Consumption

%description mgmt-consumption
Microsoft Azure Python SDK - Resource Management - Consumption

%package mgmt-containerinstance
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Instances

%description mgmt-containerinstance
Microsoft Azure Python SDK - Resource Management - Container Instances

%package mgmt-containerregistry
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Registry

%description mgmt-containerregistry
Microsoft Azure Python SDK - Resource Management - Container Registry

%package mgmt-containerservice
Version: 15.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Service

%description mgmt-containerservice
Microsoft Azure Python SDK - Resource Management - Container Service

%package mgmt-core
Version: 1.2.2
Summary: Microsoft Azure Python SDK - Resource Management - Core

%description mgmt-core
Microsoft Azure Python SDK - Resource Management - Core

%package mgmt-cosmosdb
Version: 6.3.0
Summary: Microsoft Azure Python SDK - Resource Management - Cosmos DB

%description mgmt-cosmosdb
Microsoft Azure Python SDK - Resource Management - Cosmos DB

%package mgmt-databoxedge
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Box Edge

%description mgmt-databoxedge
Microsoft Azure Python SDK - Resource Management - Data Box Edge

%package mgmt-datalake-analytics
Version: 0.6.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Analytics

%description mgmt-datalake-analytics
Microsoft Azure Python SDK - Resource Management - Data Lake Analytics

%package mgmt-datalake-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Namespace Package

%description mgmt-datalake-nspkg
Microsoft Azure Python SDK - Resource Management - Data Lake Namespace Package

%package mgmt-datalake-store
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Storage

%description mgmt-datalake-store
Microsoft Azure Python SDK - Resource Management - Data Lake Storage

%package mgmt-datamigration
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Migration

%description mgmt-datamigration
Microsoft Azure Python SDK - Resource Management - Data Migration

%package mgmt-deploymentmanager
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Deployment Manager

%description mgmt-deploymentmanager
Microsoft Azure Python SDK - Resource Management - Deployment Manager

%package mgmt-devtestlabs
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DevTest Labs

%description mgmt-devtestlabs
Microsoft Azure Python SDK - Resource Management - DevTest Labs

%package mgmt-dns
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DNS

%description mgmt-dns
Microsoft Azure Python SDK - Resource Management - DNS

%package mgmt-eventgrid
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Event Grid

%description mgmt-eventgrid
Microsoft Azure Python SDK - Resource Management - Event Grid

%package mgmt-eventhub
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Event Hubs

%description mgmt-eventhub
Microsoft Azure Python SDK - Resource Management - Event Hubs

%package mgmt-hdinsight
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - HDInsight

%description mgmt-hdinsight
Microsoft Azure Python SDK - Resource Management - HDInsight

%package mgmt-imagebuilder
Version: 0.4.0
Summary: Microsoft Azure Python SDK - Resource Management - Image Builder

%description mgmt-imagebuilder
Microsoft Azure Python SDK - Resource Management - Image Builder

%package mgmt-iotcentral
Version: 4.1.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Central

%description mgmt-iotcentral
Microsoft Azure Python SDK - Resource Management - IoT Central

%package mgmt-iothub
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Hub

%description mgmt-iothub
Microsoft Azure Python SDK - Resource Management - IoT Hub

%package mgmt-iothubprovisioningservices
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Hub Provisioning Services

%description mgmt-iothubprovisioningservices
Microsoft Azure Python SDK - Resource Management - IoT Hub Provisioning Services

%package mgmt-keyvault
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - KeyVault

%description mgmt-keyvault
Microsoft Azure Python SDK - Resource Management - KeyVault

%package mgmt-kusto
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Kusto

%description mgmt-kusto
Microsoft Azure Python SDK - Resource Management - Kusto

%package mgmt-loganalytics
Version: 10.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Log Analytics

%description mgmt-loganalytics
Microsoft Azure Python SDK - Resource Management - Log Analytics

%package mgmt-managedservices
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Managed Services

%description mgmt-managedservices
Microsoft Azure Python SDK - Resource Management - Managed Services

%package mgmt-managementgroups
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Management Groups

%description mgmt-managementgroups
Microsoft Azure Python SDK - Resource Management - Management Groups

%package mgmt-maps
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Maps

%description mgmt-maps
Microsoft Azure Python SDK - Resource Management - Maps

%package mgmt-marketplaceordering
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Marketplace Ordering

%description mgmt-marketplaceordering
Microsoft Azure Python SDK - Resource Management - Marketplace Ordering

%package mgmt-media
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Media Services

%description mgmt-media
Microsoft Azure Python SDK - Resource Management - Media Services

%package mgmt-monitor
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Monitor

%description mgmt-monitor
Microsoft Azure Python SDK - Resource Management - Monitor

%package mgmt-msi
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Managed Service Identity

%description mgmt-msi
Microsoft Azure Python SDK - Resource Management - Managed Service Identity

%package mgmt-netapp
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Resource Management - NetApp

%description mgmt-netapp
Microsoft Azure Python SDK - Resource Management - NetApp

%package mgmt-network
Version: 19.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Network

%description mgmt-network
Microsoft Azure Python SDK - Resource Management - Network

%package mgmt-nspkg
Version: 3.0.2
Summary: Microsoft Azure Python SDK - Resource Management - Namespace Package

%description mgmt-nspkg
Microsoft Azure Python SDK - Resource Management - Namespace Package

%package mgmt-policyinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Policy Insights

%description mgmt-policyinsights
Microsoft Azure Python SDK - Resource Management - Policy Insights

%package mgmt-privatedns
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Private DNS

%description mgmt-privatedns
Microsoft Azure Python SDK - Resource Management - Private DNS

%package mgmt-rdbms
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Rdbms

%description mgmt-rdbms
Microsoft Azure Python SDK - Resource Management - Rdbms

%package mgmt-recoveryservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Recovery Services

%description mgmt-recoveryservices
Microsoft Azure Python SDK - Resource Management - Recovery Services

%package mgmt-recoveryservicesbackup
Version: 0.11.0
Summary: Microsoft Azure Python SDK - Resource Management - Recovery Services Backup

%description mgmt-recoveryservicesbackup
Microsoft Azure Python SDK - Resource Management - Recovery Services Backup

%package mgmt-redhatopenshift
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Red Hat OpenShift

%description mgmt-redhatopenshift
Microsoft Azure Python SDK - Resource Management - Red Hat OpenShift

%package mgmt-redis
Version: 12.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Redis

%description mgmt-redis
Microsoft Azure Python SDK - Resource Management - Redis

%package mgmt-relay
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Relay

%description mgmt-relay
Microsoft Azure Python SDK - Resource Management - Relay

%package mgmt-reservations
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Reservations

%description mgmt-reservations
Microsoft Azure Python SDK - Resource Management - Reservations

%package mgmt-resource
Version: 18.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resources

%description mgmt-resource
Microsoft Azure Python SDK - Resource Management - Resources

%package mgmt-search
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Search

%description mgmt-search
Microsoft Azure Python SDK - Resource Management - Search

%package mgmt-security
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Security

%description mgmt-security
Microsoft Azure Python SDK - Resource Management - Security

%package mgmt-servicebus
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Service Bus

%description mgmt-servicebus
Microsoft Azure Python SDK - Resource Management - Service Bus

%package mgmt-sql
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Resource Management - SQL

%description mgmt-sql
Microsoft Azure Python SDK - Resource Management - SQL

%package mgmt-sqlvirtualmachine
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine

%description mgmt-sqlvirtualmachine
Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine

%package mgmt-storage
Version: 18.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage

%description mgmt-storage
Microsoft Azure Python SDK - Resource Management - Storage

%package mgmt-synapse
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Synapse

%description mgmt-synapse
Microsoft Azure Python SDK - Resource Management - Synapse

%package mgmt-trafficmanager
Version: 0.51.0
Summary: Microsoft Azure Python SDK - Resource Management - Traffic Manager

%description mgmt-trafficmanager
Microsoft Azure Python SDK - Resource Management - Traffic Manager

%package mgmt-web
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Web

%description mgmt-web
Microsoft Azure Python SDK - Resource Management - Web

%package nspkg
Version: 3.0.2
Summary: Microsoft Azure Python SDK - Core Namespace Package

%description nspkg
Microsoft Azure Python SDK - Core Namespace Package

%package storage-common
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Common

%description storage-common
Microsoft Azure Python SDK - Storage - Common


%prep
# Create the base directory but skip any extractions for now.
%autosetup -n %{name}-%{version} -c -T
# Extract azure-mgmt-advisor 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 0
# Extract azure-mgmt-apimanagement 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 1
# Extract azure-mgmt-appconfiguration 1.0.1
%autosetup -n %{name}-%{version} -D -T -a 2
# Extract azure-mgmt-applicationinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 3
# Extract azure-mgmt-authorization 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 4
# Extract azure-mgmt-batch 15.0.0
%autosetup -n %{name}-%{version} -D -T -a 5
# Extract azure-mgmt-batchai 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 6
# Extract azure-mgmt-billing 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 7
# Extract azure-mgmt-botservice 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 8
# Extract azure-mgmt-cdn 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 9
# Extract azure-mgmt-cognitiveservices 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 10
# Extract azure-mgmt-compute 21.0.0
%autosetup -n %{name}-%{version} -D -T -a 11
# Extract azure-mgmt-consumption 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 12
# Extract azure-mgmt-containerinstance 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 13
# Extract azure-mgmt-containerregistry 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 14
# Extract azure-mgmt-containerservice 15.1.0
%autosetup -n %{name}-%{version} -D -T -a 15
# Extract azure-mgmt-core 1.2.2
%autosetup -n %{name}-%{version} -D -T -a 16
# Extract azure-mgmt-cosmosdb 6.3.0
%autosetup -n %{name}-%{version} -D -T -a 17
# Extract azure-mgmt-databoxedge 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 18
# Extract azure-mgmt-datalake-analytics 0.6.0
%autosetup -n %{name}-%{version} -D -T -a 19
# Extract azure-mgmt-datalake-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 20
# Extract azure-mgmt-datalake-store 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 21
# Extract azure-mgmt-datamigration 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 22
# Extract azure-mgmt-deploymentmanager 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 23
# Extract azure-mgmt-devtestlabs 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 24
# Extract azure-mgmt-dns 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 25
# Extract azure-mgmt-eventgrid 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 26
# Extract azure-mgmt-eventhub 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 27
# Extract azure-mgmt-hdinsight 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 28
# Extract azure-mgmt-imagebuilder 0.4.0
%autosetup -n %{name}-%{version} -D -T -a 29
# Extract azure-mgmt-iotcentral 4.1.0
%autosetup -n %{name}-%{version} -D -T -a 30
# Extract azure-mgmt-iothub 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 31
# Extract azure-mgmt-iothubprovisioningservices 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 32
# Extract azure-mgmt-keyvault 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 33
# Extract azure-mgmt-kusto 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 34
# Extract azure-mgmt-loganalytics 10.0.0
%autosetup -n %{name}-%{version} -D -T -a 35
# Extract azure-mgmt-managedservices 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 36
# Extract azure-mgmt-managementgroups 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 37
# Extract azure-mgmt-maps 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 38
# Extract azure-mgmt-marketplaceordering 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 39
# Extract azure-mgmt-media 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 40
# Extract azure-mgmt-monitor 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 41
# Extract azure-mgmt-msi 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 42
# Extract azure-mgmt-netapp 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 43
# Extract azure-mgmt-network 19.0.0
%autosetup -n %{name}-%{version} -D -T -a 44
# Extract azure-mgmt-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 45
# Extract azure-mgmt-policyinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 46
# Extract azure-mgmt-privatedns 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 47
# Extract azure-mgmt-rdbms 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 48
# Extract azure-mgmt-recoveryservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 49
# Extract azure-mgmt-recoveryservicesbackup 0.11.0
%autosetup -n %{name}-%{version} -D -T -a 50
# Extract azure-mgmt-redhatopenshift 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 51
# Extract azure-mgmt-redis 12.0.0
%autosetup -n %{name}-%{version} -D -T -a 52
# Extract azure-mgmt-relay 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 53
# Extract azure-mgmt-reservations 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 54
# Extract azure-mgmt-resource 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 55
# Extract azure-mgmt-search 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 56
# Extract azure-mgmt-security 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 57
# Extract azure-mgmt-servicebus 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 58
# Extract azure-mgmt-sql 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 59
# Extract azure-mgmt-sqlvirtualmachine 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 60
# Extract azure-mgmt-storage 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 61
# Extract azure-mgmt-synapse 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 62
# Extract azure-mgmt-trafficmanager 0.51.0
%autosetup -n %{name}-%{version} -D -T -a 63
# Extract azure-mgmt-web 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 64
# Extract azure-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 65
# Extract azure-storage-common 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 66

tree -d

%build
# Set the directory where we collect the wheels during each step of the loop.
BASE_WHEELDIR=$(pwd)/pyproject-wheeldir
mkdir -vp $BASE_WHEELDIR

# Get a list of python projects that we've extracted.
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)

# Loop over each project, build the wheel, and move the wheel into the correct
# place.
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %pyproject_wheel
        mv pyproject-wheeldir/* $BASE_WHEELDIR
    popd
done

%install
%pyproject_install

%if %{with check}
%check
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %pytest
    popd
done
%endif


%files mgmt-advisor
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/advisor
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_advisor-*.dist-info/


%files mgmt-apimanagement
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/apimanagement
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_apimanagement-*.dist-info/


%files mgmt-appconfiguration
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/appconfiguration
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_appconfiguration-*.dist-info/


%files mgmt-applicationinsights
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/applicationinsights
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_applicationinsights-*.dist-info/


%files mgmt-authorization
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/authorization
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_authorization-*.dist-info/


%files mgmt-batch
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/batch
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_batch-*.dist-info/


%files mgmt-batchai
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/batchai
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_batchai-*.dist-info/


%files mgmt-billing
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/billing
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_billing-*.dist-info/


%files mgmt-botservice
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/botservice
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_botservice-*.dist-info/


%files mgmt-cdn
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/cdn
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_cdn-*.dist-info/


%files mgmt-cognitiveservices
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/cognitiveservices
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_cognitiveservices-*.dist-info/


%files mgmt-compute
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/compute
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_compute-*.dist-info/


%files mgmt-consumption
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/consumption
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_consumption-*.dist-info/


%files mgmt-containerinstance
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/containerinstance
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_containerinstance-*.dist-info/


%files mgmt-containerregistry
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/containerregistry
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_containerregistry-*.dist-info/


%files mgmt-containerservice
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/containerservice
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_containerservice-*.dist-info/


%files mgmt-core
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/core
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_core-*.dist-info/
# Packaging base_init
%{python3_sitelib}/azure/__init__.py
# Packaging base_init_pycache
%{python3_sitelib}/azure/__pycache__/__init__*
# Packaging base_mgmt_init
%{python3_sitelib}/azure/mgmt/__init__.py
# Packaging base_mgmt_init_pycache
%{python3_sitelib}/azure/mgmt/__pycache__/__init__*


%files mgmt-cosmosdb
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/cosmosdb
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_cosmosdb-*.dist-info/


%files mgmt-databoxedge
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/databoxedge
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_databoxedge-*.dist-info/
# Packaging sitelib_datab
%{python3_sitelib}/azure/mgmt/datab


%files mgmt-datalake-analytics
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/datalake/analytics
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_datalake_analytics-*.dist-info/


%files mgmt-datalake-nspkg
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_datalake_nspkg-*.dist-info/
# Packaging base_init
%{python3_sitelib}/azure/mgmt/datalake/__init__.py
# Packaging base_init_pycache
%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__*


%files mgmt-datalake-store
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/datalake/store
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_datalake_store-*.dist-info/


%files mgmt-datamigration
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/datamigration
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_datamigration-*.dist-info/


%files mgmt-deploymentmanager
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/deploymentmanager
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_deploymentmanager-*.dist-info/


%files mgmt-devtestlabs
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/devtestlabs
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_devtestlabs-*.dist-info/


%files mgmt-dns
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/dns
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_dns-*.dist-info/


%files mgmt-eventgrid
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/eventgrid
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_eventgrid-*.dist-info/


%files mgmt-eventhub
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/eventhub
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_eventhub-*.dist-info/


%files mgmt-hdinsight
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/hdinsight
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_hdinsight-*.dist-info/


%files mgmt-imagebuilder
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/imagebuilder
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_imagebuilder-*.dist-info/


%files mgmt-iotcentral
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/iotcentral
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_iotcentral-*.dist-info/


%files mgmt-iothub
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/iothub
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_iothub-*.dist-info/


%files mgmt-iothubprovisioningservices
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/iothubprovisioningservices
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_iothubprovisioningservices-*.dist-info/


%files mgmt-keyvault
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/keyvault
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_keyvault-*.dist-info/


%files mgmt-kusto
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/kusto
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_kusto-*.dist-info/


%files mgmt-loganalytics
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/loganalytics
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_loganalytics-*.dist-info/


%files mgmt-managedservices
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/managedservices
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_managedservices-*.dist-info/


%files mgmt-managementgroups
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/managementgroups
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_managementgroups-*.dist-info/


%files mgmt-maps
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/maps
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_maps-*.dist-info/


%files mgmt-marketplaceordering
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/marketplaceordering
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_marketplaceordering-*.dist-info/


%files mgmt-media
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/media
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_media-*.dist-info/


%files mgmt-monitor
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/monitor
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_monitor-*.dist-info/


%files mgmt-msi
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/msi
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_msi-*.dist-info/


%files mgmt-netapp
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/netapp
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_netapp-*.dist-info/


%files mgmt-network
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/network
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_network-*.dist-info/


%files mgmt-nspkg
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_nspkg-*.dist-info/


%files mgmt-policyinsights
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/policyinsights
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_policyinsights-*.dist-info/


%files mgmt-privatedns
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/privatedns
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_privatedns-*.dist-info/


%files mgmt-rdbms
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/rdbms
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_rdbms-*.dist-info/


%files mgmt-recoveryservices
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/recoveryservices
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_recoveryservices-*.dist-info/


%files mgmt-recoveryservicesbackup
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/recoveryservicesbackup
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_recoveryservicesbackup-*.dist-info/


%files mgmt-redhatopenshift
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/redhatopenshift
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_redhatopenshift-*.dist-info/


%files mgmt-redis
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/redis
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_redis-*.dist-info/


%files mgmt-relay
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/relay
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_relay-*.dist-info/


%files mgmt-reservations
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/reservations
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_reservations-*.dist-info/


%files mgmt-resource
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/resource
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_resource-*.dist-info/


%files mgmt-search
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/search
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_search-*.dist-info/


%files mgmt-security
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/security
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_security-*.dist-info/


%files mgmt-servicebus
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/servicebus
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_servicebus-*.dist-info/


%files mgmt-sql
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/sql
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_sql-*.dist-info/


%files mgmt-sqlvirtualmachine
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/sqlvirtualmachine
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_sqlvirtualmachine-*.dist-info/


%files mgmt-storage
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/storage
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_storage-*.dist-info/


%files mgmt-synapse
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/synapse
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_synapse-*.dist-info/


%files mgmt-trafficmanager
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/trafficmanager
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_trafficmanager-*.dist-info/


%files mgmt-web
# Packaging sitelib
%{python3_sitelib}/azure/mgmt/web
# Packaging distinfo
%{python3_sitelib}/azure_mgmt_web-*.dist-info/


%files nspkg
# Packaging distinfo
%{python3_sitelib}/azure_nspkg-*.dist-info/


%files storage-common
# Packaging sitelib
%{python3_sitelib}/azure/storage/common
# Packaging distinfo
%{python3_sitelib}/azure_storage_common-*.dist-info/



%changelog
* Wed May 26 2021 Major Hayden - 0.0.1-1
- First package.