# Enable Python dependency generation
%{?python_enable_dependency_generator}


Name:           python-azure
Version:        20210527
Release:        1%{?dist}

Summary:        Azure SDK for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        %{pypi_source azure-ai-formrecognizer 3.1.0 zip}
Source1:        %{pypi_source azure-ai-nspkg 1.0.0 zip}
Source2:        %{pypi_source azure-ai-textanalytics 5.0.0 zip}
Source3:        %{pypi_source azure-appconfiguration 1.1.1 zip}
Source4:        %{pypi_source azure-applicationinsights 0.1.0 zip}
Source5:        %{pypi_source azure-batch 10.0.0 zip}
Source6:        %{pypi_source azure-cognitiveservices-anomalydetector 0.3.0 zip}
Source7:        %{pypi_source azure-cognitiveservices-formrecognizer 0.1.1 zip}
Source8:        %{pypi_source azure-cognitiveservices-knowledge-nspkg 3.0.0 zip}
Source9:        %{pypi_source azure-cognitiveservices-knowledge-qnamaker 0.3.0 zip}
Source10:       %{pypi_source azure-cognitiveservices-language-luis 0.7.0 zip}
Source11:       %{pypi_source azure-cognitiveservices-language-nspkg 3.0.1 zip}
Source12:       %{pypi_source azure-cognitiveservices-language-spellcheck 2.0.0 zip}
Source13:       %{pypi_source azure-cognitiveservices-language-textanalytics 0.2.0 zip}
Source14:       %{pypi_source azure-cognitiveservices-nspkg 3.0.1 zip}
Source15:       %{pypi_source azure-cognitiveservices-personalizer 0.1.0 zip}
Source16:       %{pypi_source azure-cognitiveservices-search-autosuggest 0.2.0 zip}
Source17:       %{pypi_source azure-cognitiveservices-search-customimagesearch 0.2.0 zip}
Source18:       %{pypi_source azure-cognitiveservices-search-customsearch 0.3.0 zip}
Source19:       %{pypi_source azure-cognitiveservices-search-entitysearch 2.0.0 zip}
Source20:       %{pypi_source azure-cognitiveservices-search-imagesearch 2.0.0 zip}
Source21:       %{pypi_source azure-cognitiveservices-search-newssearch 2.0.0 zip}
Source22:       %{pypi_source azure-cognitiveservices-search-nspkg 3.0.1 zip}
Source23:       %{pypi_source azure-cognitiveservices-search-videosearch 2.0.0 zip}
Source24:       %{pypi_source azure-cognitiveservices-search-visualsearch 0.2.0 zip}
Source25:       %{pypi_source azure-cognitiveservices-search-websearch 2.0.0 zip}
Source26:       %{pypi_source azure-cognitiveservices-vision-computervision 0.9.0 zip}
Source27:       %{pypi_source azure-cognitiveservices-vision-contentmoderator 1.0.0 zip}
Source28:       %{pypi_source azure-cognitiveservices-vision-customvision 3.1.0 zip}
Source29:       %{pypi_source azure-cognitiveservices-vision-face 0.5.0 zip}
Source30:       %{pypi_source azure-cognitiveservices-vision-nspkg 3.0.1 zip}
Source31:       %{pypi_source azure-common 1.1.27 zip}
Source32:       %{pypi_source azure-communication-chat 1.0.0 zip}
Source33:       %{pypi_source azure-communication-identity 1.0.0 zip}
Source34:       %{pypi_source azure-communication-phonenumbers 1.0.0 zip}
Source35:       %{pypi_source azure-communication-sms 1.0.0 zip}
Source36:       %{pypi_source azure-core 1.14.0 zip}
Source37:       %{pypi_source azure-cosmos 3.2.0 tar.gz}
Source38:       %{pypi_source azure-cosmosdb-table 1.0.6 tar.gz}
Source39:       %{pypi_source azure-data-nspkg 1.0.0 zip}
Source40:       %{pypi_source azure-datalake-store 0.0.51 tar.gz}
Source41:       %{pypi_source azure-digitaltwins-core 1.1.0 zip}
Source42:       %{pypi_source azure-digitaltwins-nspkg 1.0.0 zip}
Source43:       %{pypi_source azure-eventgrid 4.2.0 zip}
Source44:       %{pypi_source azure-eventhub 5.5.0 zip}
Source45:       %{pypi_source azure-graphrbac 0.61.1 zip}
Source46:       %{pypi_source azure-identity 1.6.0 zip}
Source47:       %{pypi_source azure-iot-device 2.6.0 tar.gz}
Source48:       %{pypi_source azure-iot-hub 2.4.0 tar.gz}
Source49:       %{pypi_source azure-keyvault 4.1.0 zip}
Source50:       %{pypi_source azure-keyvault-certificates 4.2.1 zip}
Source51:       %{pypi_source azure-keyvault-keys 4.3.1 zip}
Source52:       %{pypi_source azure-keyvault-nspkg 1.0.0 zip}
Source53:       %{pypi_source azure-keyvault-secrets 4.2.0 zip}
Source54:       %{pypi_source azure-kusto-data 2.0.0 tar.gz}
Source55:       %{pypi_source azure-loganalytics 0.1.0 zip}
Source56:       %{pypi_source azure-mgmt-advisor 9.0.0 zip}
Source57:       %{pypi_source azure-mgmt-alertsmanagement 1.0.0 zip}
Source58:       %{pypi_source azure-mgmt-apimanagement 2.0.0 zip}
Source59:       %{pypi_source azure-mgmt-appconfiguration 1.0.1 zip}
Source60:       %{pypi_source azure-mgmt-applicationinsights 1.0.0 zip}
Source61:       %{pypi_source azure-mgmt-appplatform 6.0.0 zip}
Source62:       %{pypi_source azure-mgmt-attestation 1.0.0 zip}
Source63:       %{pypi_source azure-mgmt-authorization 1.0.0 zip}
Source64:       %{pypi_source azure-mgmt-automation 1.0.0 zip}
Source65:       %{pypi_source azure-mgmt-avs 1.0.0 zip}
Source66:       %{pypi_source azure-mgmt-azurestack 1.0.0 zip}
Source67:       %{pypi_source azure-mgmt-azurestackhci 6.0.0 zip}
Source68:       %{pypi_source azure-mgmt-batch 15.0.0 zip}
Source69:       %{pypi_source azure-mgmt-batchai 2.0.0 zip}
Source70:       %{pypi_source azure-mgmt-billing 6.0.0 zip}
Source71:       %{pypi_source azure-mgmt-botservice 1.0.0 zip}
Source72:       %{pypi_source azure-mgmt-cdn 11.0.0 zip}
Source73:       %{pypi_source azure-mgmt-cognitiveservices 11.0.0 zip}
Source74:       %{pypi_source azure-mgmt-commerce 6.0.0 zip}
Source75:       %{pypi_source azure-mgmt-common 0.20.0 zip}
Source76:       %{pypi_source azure-mgmt-communication 1.0.0 zip}
Source77:       %{pypi_source azure-mgmt-compute 21.0.0 zip}
Source78:       %{pypi_source azure-mgmt-confluent 1.0.0 zip}
Source79:       %{pypi_source azure-mgmt-consumption 8.0.0 zip}
Source80:       %{pypi_source azure-mgmt-containerinstance 7.0.0 zip}
Source81:       %{pypi_source azure-mgmt-containerregistry 8.0.0 zip}
Source82:       %{pypi_source azure-mgmt-containerservice 15.1.0 zip}
Source83:       %{pypi_source azure-mgmt-core 1.2.2 zip}
Source84:       %{pypi_source azure-mgmt-cosmosdb 6.3.0 zip}
Source85:       %{pypi_source azure-mgmt-costmanagement 1.0.0 zip}
Source86:       %{pypi_source azure-mgmt-customproviders 1.0.0 zip}
Source87:       %{pypi_source azure-mgmt-databox 1.0.0 zip}
Source88:       %{pypi_source azure-mgmt-databoxedge 1.0.0 zip}
Source89:       %{pypi_source azure-mgmt-databricks 1.0.0 zip}
Source90:       %{pypi_source azure-mgmt-datadog 2.0.0 zip}
Source91:       %{pypi_source azure-mgmt-datafactory 1.1.0 zip}
Source92:       %{pypi_source azure-mgmt-datalake-analytics 0.6.0 zip}
Source93:       %{pypi_source azure-mgmt-datalake-nspkg 3.0.1 zip}
Source94:       %{pypi_source azure-mgmt-datalake-store 0.5.0 zip}
Source95:       %{pypi_source azure-mgmt-datamigration 9.0.0 zip}
Source96:       %{pypi_source azure-mgmt-datashare 1.0.0 zip}
Source97:       %{pypi_source azure-mgmt-deploymentmanager 1.0.0 zip}
Source98:       %{pypi_source azure-mgmt-devspaces 0.2.0 zip}
Source99:       %{pypi_source azure-mgmt-devtestlabs 9.0.0 zip}
Source100:      %{pypi_source azure-mgmt-digitaltwins 6.0.0 zip}
Source101:      %{pypi_source azure-mgmt-dns 8.0.0 zip}
Source102:      %{pypi_source azure-mgmt-edgegateway 0.1.0 zip}
Source103:      %{pypi_source azure-mgmt-eventgrid 9.0.0 zip}
Source104:      %{pypi_source azure-mgmt-eventhub 9.0.0 zip}
Source105:      %{pypi_source azure-mgmt-frontdoor 1.0.0 zip}
Source106:      %{pypi_source azure-mgmt-hanaonazure 1.0.0 zip}
Source107:      %{pypi_source azure-mgmt-hdinsight 7.0.0 zip}
Source108:      %{pypi_source azure-mgmt-healthcareapis 1.0.0 zip}
Source109:      %{pypi_source azure-mgmt-hybridcompute 7.0.0 zip}
Source110:      %{pypi_source azure-mgmt-hybridkubernetes 1.0.0 zip}
Source111:      %{pypi_source azure-mgmt-imagebuilder 0.4.0 zip}
Source112:      %{pypi_source azure-mgmt-iotcentral 4.1.0 zip}
Source113:      %{pypi_source azure-mgmt-iothub 2.0.0 zip}
Source114:      %{pypi_source azure-mgmt-iothubprovisioningservices 0.2.0 zip}
Source115:      %{pypi_source azure-mgmt-keyvault 9.0.0 zip}
Source116:      %{pypi_source azure-mgmt-kusto 2.0.0 zip}
Source117:      %{pypi_source azure-mgmt-labservices 1.0.0 zip}
Source118:      %{pypi_source azure-mgmt-loganalytics 10.0.0 zip}
Source119:      %{pypi_source azure-mgmt-logic 9.0.0 zip}
Source120:      %{pypi_source azure-mgmt-machinelearningcompute 0.4.1 zip}
Source121:      %{pypi_source azure-mgmt-machinelearningservices 1.0.0 zip}
Source122:      %{pypi_source azure-mgmt-maintenance 2.0.0 zip}
Source123:      %{pypi_source azure-mgmt-managedservices 6.0.0 zip}
Source124:      %{pypi_source azure-mgmt-managementgroups 1.0.0 zip}
Source125:      %{pypi_source azure-mgmt-managementpartner 1.0.0 zip}
Source126:      %{pypi_source azure-mgmt-maps 2.0.0 zip}
Source127:      %{pypi_source azure-mgmt-marketplaceordering 1.1.0 zip}
Source128:      %{pypi_source azure-mgmt-media 3.1.0 zip}
Source129:      %{pypi_source azure-mgmt-mixedreality 1.0.0 zip}
Source130:      %{pypi_source azure-mgmt-monitor 2.0.0 zip}
Source131:      %{pypi_source azure-mgmt-msi 1.0.0 zip}
Source132:      %{pypi_source azure-mgmt-netapp 3.0.0 zip}
Source133:      %{pypi_source azure-mgmt-network 19.0.0 zip}
Source134:      %{pypi_source azure-mgmt-notificationhubs 7.0.0 zip}
Source135:      %{pypi_source azure-mgmt-nspkg 3.0.2 zip}
Source136:      %{pypi_source azure-mgmt-operationsmanagement 1.0.0 zip}
Source137:      %{pypi_source azure-mgmt-peering 1.0.0 zip}
Source138:      %{pypi_source azure-mgmt-policyinsights 1.0.0 zip}
Source139:      %{pypi_source azure-mgmt-powerbidedicated 1.0.0 zip}
Source140:      %{pypi_source azure-mgmt-powerbiembedded 2.0.0 zip}
Source141:      %{pypi_source azure-mgmt-privatedns 1.0.0 zip}
Source142:      %{pypi_source azure-mgmt-rdbms 8.0.0 zip}
Source143:      %{pypi_source azure-mgmt-recoveryservices 1.0.0 zip}
Source144:      %{pypi_source azure-mgmt-recoveryservicesbackup 0.11.0 zip}
Source145:      %{pypi_source azure-mgmt-redhatopenshift 1.0.0 zip}
Source146:      %{pypi_source azure-mgmt-redis 12.0.0 zip}
Source147:      %{pypi_source azure-mgmt-relay 1.0.0 zip}
Source148:      %{pypi_source azure-mgmt-reservations 1.0.0 zip}
Source149:      %{pypi_source azure-mgmt-resource 18.0.0 zip}
Source150:      %{pypi_source azure-mgmt-resourcegraph 8.0.0 zip}
Source151:      %{pypi_source azure-mgmt-resourcemover 1.0.0 zip}
Source152:      %{pypi_source azure-mgmt-scheduler 2.0.0 zip}
Source153:      %{pypi_source azure-mgmt-search 8.0.0 zip}
Source154:      %{pypi_source azure-mgmt-security 1.0.0 zip}
Source155:      %{pypi_source azure-mgmt-serialconsole 1.0.0 zip}
Source156:      %{pypi_source azure-mgmt-servermanager 2.0.0 zip}
Source157:      %{pypi_source azure-mgmt-servicebus 6.0.0 zip}
Source158:      %{pypi_source azure-mgmt-sql 2.1.0 zip}
Source159:      %{pypi_source azure-mgmt-sqlvirtualmachine 0.5.0 zip}
Source160:      %{pypi_source azure-mgmt-storage 18.0.0 zip}
Source161:      %{pypi_source azure-mgmt-storagecache 0.5.0 zip}
Source162:      %{pypi_source azure-mgmt-storageimportexport 0.1.0 zip}
Source163:      %{pypi_source azure-mgmt-storagesync 1.0.0 zip}
Source164:      %{pypi_source azure-mgmt-subscription 1.0.0 zip}
Source165:      %{pypi_source azure-mgmt-support 6.0.0 zip}
Source166:      %{pypi_source azure-mgmt-synapse 2.0.0 zip}
Source167:      %{pypi_source azure-mgmt-timeseriesinsights 1.0.0 zip}
Source168:      %{pypi_source azure-mgmt-trafficmanager 0.51.0 zip}
Source169:      %{pypi_source azure-mgmt-vmwarecloudsimple 0.2.0 zip}
Source170:      %{pypi_source azure-mgmt-web 3.0.0 zip}
Source171:      %{pypi_source azure-nspkg 3.0.2 zip}
Source172:      %{pypi_source azure-search-documents 11.1.0 zip}
Source173:      %{pypi_source azure-search-nspkg 1.0.0 zip}
Source174:      %{pypi_source azure-servicebus 7.2.0 zip}
Source175:      %{pypi_source azure-servicefabric 8.0.0.0 zip}
Source176:      %{pypi_source azure-storage-blob 2.1.0 tar.gz}
Source177:      %{pypi_source azure-storage-common 2.1.0 tar.gz}
Source178:      %{pypi_source azure-storage-file 2.1.0 tar.gz}
Source179:      %{pypi_source azure-storage-file-datalake 12.3.1 zip}
Source180:      %{pypi_source azure-storage-file-share 12.4.2 zip}
Source181:      %{pypi_source azure-storage-nspkg 3.1.0 tar.gz}
Source182:      %{pypi_source azure-storage-queue 2.1.0 tar.gz}
Source183:      %{pypi_source azure-synapse 0.1.1 zip}
Source184:      %{pypi_source azure-synapse-nspkg 1.0.0 zip}
Source185:      %{pypi_source azure-template 0.0.17 zip}


BuildArch:      noarch

Obsoletes:      python-azure-sdk == 5.0.0-4

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Azure SDK for Python


%package ai-formrecognizer
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Form Recognizer

%description ai-formrecognizer
Microsoft Azure Python SDK - Form Recognizer

%package ai-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Text Analytics Namespace Package

%description ai-nspkg
Microsoft Azure Python SDK - Text Analytics Namespace Package

%package ai-textanalytics
Version: 5.0.0
Summary: Microsoft Azure Python SDK - Text Analytics

%description ai-textanalytics
Microsoft Azure Python SDK - Text Analytics

%package appconfiguration
Version: 1.1.1
Summary: Microsoft Azure Python SDK - App Configuration

%description appconfiguration
Microsoft Azure Python SDK - App Configuration

%package applicationinsights
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Application Insights

%description applicationinsights
Microsoft Azure Python SDK - Application Insights

%package batch
Version: 10.0.0
Summary: Microsoft Azure Python SDK - Batch

%description batch
Microsoft Azure Python SDK - Batch

%package cognitiveservices-anomalydetector
Version: 0.3.0
Summary: Microsoft Azure Python SDK - Anomaly Detector

%description cognitiveservices-anomalydetector
Microsoft Azure Python SDK - Anomaly Detector

%package cognitiveservices-formrecognizer
Version: 0.1.1
Summary: Microsoft Azure Python SDK - Form Recognizer

%description cognitiveservices-formrecognizer
Microsoft Azure Python SDK - Form Recognizer

%package cognitiveservices-knowledge-nspkg
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Cognitive Services Knowledge Namespace Package

%description cognitiveservices-knowledge-nspkg
Microsoft Azure Python SDK - Cognitive Services Knowledge Namespace Package

%package cognitiveservices-knowledge-qnamaker
Version: 0.3.0
Summary: Microsoft Azure Python SDK - QnA Maker

%description cognitiveservices-knowledge-qnamaker
Microsoft Azure Python SDK - QnA Maker

%package cognitiveservices-language-luis
Version: 0.7.0
Summary: Microsoft Azure Python SDK - LUIS

%description cognitiveservices-language-luis
Microsoft Azure Python SDK - LUIS

%package cognitiveservices-language-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Language Namespace Package

%description cognitiveservices-language-nspkg
Microsoft Azure Python SDK - Cognitive Services Language Namespace Package

%package cognitiveservices-language-spellcheck
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Spell Check

%description cognitiveservices-language-spellcheck
Microsoft Azure Python SDK - Spell Check

%package cognitiveservices-language-textanalytics
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Text Analytics

%description cognitiveservices-language-textanalytics
Microsoft Azure Python SDK - Text Analytics

%package cognitiveservices-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Namespace Package

%description cognitiveservices-nspkg
Microsoft Azure Python SDK - Cognitive Services Namespace Package

%package cognitiveservices-personalizer
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Personalizer

%description cognitiveservices-personalizer
Microsoft Azure Python SDK - Personalizer

%package cognitiveservices-search-autosuggest
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Autosuggest

%description cognitiveservices-search-autosuggest
Microsoft Azure Python SDK - Autosuggest

%package cognitiveservices-search-customimagesearch
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Custom Image Search

%description cognitiveservices-search-customimagesearch
Microsoft Azure Python SDK - Custom Image Search

%package cognitiveservices-search-customsearch
Version: 0.3.0
Summary: Microsoft Azure Python SDK - Custom Search

%description cognitiveservices-search-customsearch
Microsoft Azure Python SDK - Custom Search

%package cognitiveservices-search-entitysearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Entity Search

%description cognitiveservices-search-entitysearch
Microsoft Azure Python SDK - Entity Search

%package cognitiveservices-search-imagesearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Image Search

%description cognitiveservices-search-imagesearch
Microsoft Azure Python SDK - Image Search

%package cognitiveservices-search-newssearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - News Search

%description cognitiveservices-search-newssearch
Microsoft Azure Python SDK - News Search

%package cognitiveservices-search-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Search Namespace Package

%description cognitiveservices-search-nspkg
Microsoft Azure Python SDK - Cognitive Services Search Namespace Package

%package cognitiveservices-search-videosearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Video Search

%description cognitiveservices-search-videosearch
Microsoft Azure Python SDK - Video Search

%package cognitiveservices-search-visualsearch
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Visual Search

%description cognitiveservices-search-visualsearch
Microsoft Azure Python SDK - Visual Search

%package cognitiveservices-search-websearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Web Search

%description cognitiveservices-search-websearch
Microsoft Azure Python SDK - Web Search

%package cognitiveservices-vision-computervision
Version: 0.9.0
Summary: Microsoft Azure Python SDK - Computer Vision

%description cognitiveservices-vision-computervision
Microsoft Azure Python SDK - Computer Vision

%package cognitiveservices-vision-contentmoderator
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Content Moderator

%description cognitiveservices-vision-contentmoderator
Microsoft Azure Python SDK - Content Moderator

%package cognitiveservices-vision-customvision
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Custom Vision

%description cognitiveservices-vision-customvision
Microsoft Azure Python SDK - Custom Vision

%package cognitiveservices-vision-face
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Face

%description cognitiveservices-vision-face
Microsoft Azure Python SDK - Face

%package cognitiveservices-vision-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Vision Namespace Package

%description cognitiveservices-vision-nspkg
Microsoft Azure Python SDK - Cognitive Services Vision Namespace Package

%package common
Version: 1.1.27
Summary: Microsoft Azure Python SDK - Common

%description common
Microsoft Azure Python SDK - Common

%package communication-chat
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Chat

%description communication-chat
Microsoft Azure Python SDK - Communication Chat

%package communication-identity
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Identity

%description communication-identity
Microsoft Azure Python SDK - Communication Identity

%package communication-phonenumbers
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Phone Numbers

%description communication-phonenumbers
Microsoft Azure Python SDK - Communication Phone Numbers

%package communication-sms
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Sms

%description communication-sms
Microsoft Azure Python SDK - Communication Sms

%package core
Version: 1.14.0
Summary: Microsoft Azure Python SDK - Core

%description core
Microsoft Azure Python SDK - Core

%package cosmos
Version: 3.2.0
Summary: Microsoft Azure Python SDK - Cosmos DB

%description cosmos
Microsoft Azure Python SDK - Cosmos DB

%package cosmosdb-table
Version: 1.0.6
Summary: Microsoft Azure Python SDK - Tables

%description cosmosdb-table
Microsoft Azure Python SDK - Tables

%package data-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Data Namespace Package

%description data-nspkg
Microsoft Azure Python SDK - Data Namespace Package

%package datalake-store
Version: 0.0.51
Summary: Microsoft Azure Python SDK - Data Lake Storage

%description datalake-store
Microsoft Azure Python SDK - Data Lake Storage

%package digitaltwins-core
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Digital Twins - Core

%description digitaltwins-core
Microsoft Azure Python SDK - Digital Twins - Core

%package digitaltwins-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Digital Twins Namespace Package

%description digitaltwins-nspkg
Microsoft Azure Python SDK - Digital Twins Namespace Package

%package eventgrid
Version: 4.2.0
Summary: Microsoft Azure Python SDK - Event Grid

%description eventgrid
Microsoft Azure Python SDK - Event Grid

%package eventhub
Version: 5.5.0
Summary: Microsoft Azure Python SDK - Event Hubs

%description eventhub
Microsoft Azure Python SDK - Event Hubs

%package graphrbac
Version: 0.61.1
Summary: Microsoft Azure Python SDK - Graph RBAC

%description graphrbac
Microsoft Azure Python SDK - Graph RBAC

%package identity
Version: 1.6.0
Summary: Microsoft Azure Python SDK - Identity

%description identity
Microsoft Azure Python SDK - Identity

%package iot-device
Version: 2.6.0
Summary: Microsoft Azure Python SDK - IoT Device

%description iot-device
Microsoft Azure Python SDK - IoT Device

%package iot-hub
Version: 2.4.0
Summary: Microsoft Azure Python SDK - IoT Hub

%description iot-hub
Microsoft Azure Python SDK - IoT Hub

%package keyvault
Version: 4.1.0
Summary: Microsoft Azure Python SDK - Key Vault

%description keyvault
Microsoft Azure Python SDK - Key Vault

%package keyvault-certificates
Version: 4.2.1
Summary: Microsoft Azure Python SDK - Key Vault - Certificates

%description keyvault-certificates
Microsoft Azure Python SDK - Key Vault - Certificates

%package keyvault-keys
Version: 4.3.1
Summary: Microsoft Azure Python SDK - Key Vault - Keys

%description keyvault-keys
Microsoft Azure Python SDK - Key Vault - Keys

%package keyvault-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Key Vault Namespace Package

%description keyvault-nspkg
Microsoft Azure Python SDK - Key Vault Namespace Package

%package keyvault-secrets
Version: 4.2.0
Summary: Microsoft Azure Python SDK - Key Vault - Secrets

%description keyvault-secrets
Microsoft Azure Python SDK - Key Vault - Secrets

%package kusto-data
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Kusto Data

%description kusto-data
Microsoft Azure Python SDK - Kusto Data

%package loganalytics
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Log Analytics

%description loganalytics
Microsoft Azure Python SDK - Log Analytics

%package mgmt-advisor
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Advisor

%description mgmt-advisor
Microsoft Azure Python SDK - Resource Management - Advisor

%package mgmt-alertsmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Alerts Management

%description mgmt-alertsmanagement
Microsoft Azure Python SDK - Resource Management - Alerts Management

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

%package mgmt-appplatform
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - App Platform

%description mgmt-appplatform
Microsoft Azure Python SDK - Resource Management - App Platform

%package mgmt-attestation
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Attestation

%description mgmt-attestation
Microsoft Azure Python SDK - Resource Management - Attestation

%package mgmt-authorization
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Authorization

%description mgmt-authorization
Microsoft Azure Python SDK - Resource Management - Authorization

%package mgmt-automation
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Automation

%description mgmt-automation
Microsoft Azure Python SDK - Resource Management - Automation

%package mgmt-avs
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure VMware Solution

%description mgmt-avs
Microsoft Azure Python SDK - Resource Management - Azure VMware Solution

%package mgmt-azurestack
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure Stack

%description mgmt-azurestack
Microsoft Azure Python SDK - Resource Management - Azure Stack

%package mgmt-azurestackhci
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure Stack HCI

%description mgmt-azurestackhci
Microsoft Azure Python SDK - Resource Management - Azure Stack HCI

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

%package mgmt-commerce
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Commerce

%description mgmt-commerce
Microsoft Azure Python SDK - Resource Management - Commerce

%package mgmt-common
Version: 0.20.0
Summary: Microsoft Azure Python SDK - Resource Management - Common

%description mgmt-common
Microsoft Azure Python SDK - Resource Management - Common

%package mgmt-communication
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Communication

%description mgmt-communication
Microsoft Azure Python SDK - Resource Management - Communication

%package mgmt-compute
Version: 21.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Compute

%description mgmt-compute
Microsoft Azure Python SDK - Resource Management - Compute

%package mgmt-confluent
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Confluent

%description mgmt-confluent
Microsoft Azure Python SDK - Resource Management - Confluent

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

%package mgmt-costmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Cost Management

%description mgmt-costmanagement
Microsoft Azure Python SDK - Resource Management - Cost Management

%package mgmt-customproviders
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Custom Providers

%description mgmt-customproviders
Microsoft Azure Python SDK - Resource Management - Custom Providers

%package mgmt-databox
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Box

%description mgmt-databox
Microsoft Azure Python SDK - Resource Management - Data Box

%package mgmt-databoxedge
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Box Edge

%description mgmt-databoxedge
Microsoft Azure Python SDK - Resource Management - Data Box Edge

%package mgmt-databricks
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Databricks

%description mgmt-databricks
Microsoft Azure Python SDK - Resource Management - Databricks

%package mgmt-datadog
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Datadog

%description mgmt-datadog
Microsoft Azure Python SDK - Resource Management - Datadog

%package mgmt-datafactory
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Factory

%description mgmt-datafactory
Microsoft Azure Python SDK - Resource Management - Data Factory

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

%package mgmt-datashare
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Share

%description mgmt-datashare
Microsoft Azure Python SDK - Resource Management - Data Share

%package mgmt-deploymentmanager
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Deployment Manager

%description mgmt-deploymentmanager
Microsoft Azure Python SDK - Resource Management - Deployment Manager

%package mgmt-devspaces
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - Dev Spaces

%description mgmt-devspaces
Microsoft Azure Python SDK - Resource Management - Dev Spaces

%package mgmt-devtestlabs
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DevTest Labs

%description mgmt-devtestlabs
Microsoft Azure Python SDK - Resource Management - DevTest Labs

%package mgmt-digitaltwins
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Digital Twins

%description mgmt-digitaltwins
Microsoft Azure Python SDK - Resource Management - Digital Twins

%package mgmt-dns
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DNS

%description mgmt-dns
Microsoft Azure Python SDK - Resource Management - DNS

%package mgmt-edgegateway
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Edge Gateway

%description mgmt-edgegateway
Microsoft Azure Python SDK - Resource Management - Edge Gateway

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

%package mgmt-frontdoor
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Frontdoor

%description mgmt-frontdoor
Microsoft Azure Python SDK - Resource Management - Frontdoor

%package mgmt-hanaonazure
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - HANA on Azure

%description mgmt-hanaonazure
Microsoft Azure Python SDK - Resource Management - HANA on Azure

%package mgmt-hdinsight
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - HDInsight

%description mgmt-hdinsight
Microsoft Azure Python SDK - Resource Management - HDInsight

%package mgmt-healthcareapis
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Healthcare APIs

%description mgmt-healthcareapis
Microsoft Azure Python SDK - Resource Management - Healthcare APIs

%package mgmt-hybridcompute
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Hybrid Compute

%description mgmt-hybridcompute
Microsoft Azure Python SDK - Resource Management - Hybrid Compute

%package mgmt-hybridkubernetes
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Hybrid Kubernetes

%description mgmt-hybridkubernetes
Microsoft Azure Python SDK - Resource Management - Hybrid Kubernetes

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

%package mgmt-labservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Lab Services

%description mgmt-labservices
Microsoft Azure Python SDK - Resource Management - Lab Services

%package mgmt-loganalytics
Version: 10.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Log Analytics

%description mgmt-loganalytics
Microsoft Azure Python SDK - Resource Management - Log Analytics

%package mgmt-logic
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Logic Apps

%description mgmt-logic
Microsoft Azure Python SDK - Resource Management - Logic Apps

%package mgmt-machinelearningcompute
Version: 0.4.1
Summary: Microsoft Azure Python SDK - Resource Management - Machine Learning Compute

%description mgmt-machinelearningcompute
Microsoft Azure Python SDK - Resource Management - Machine Learning Compute

%package mgmt-machinelearningservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Machine Learning Services

%description mgmt-machinelearningservices
Microsoft Azure Python SDK - Resource Management - Machine Learning Services

%package mgmt-maintenance
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Maintenance

%description mgmt-maintenance
Microsoft Azure Python SDK - Resource Management - Maintenance

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

%package mgmt-managementpartner
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Management Partner

%description mgmt-managementpartner
Microsoft Azure Python SDK - Resource Management - Management Partner

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

%package mgmt-mixedreality
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Mixed Reality

%description mgmt-mixedreality
Microsoft Azure Python SDK - Resource Management - Mixed Reality

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

%package mgmt-notificationhubs
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Notification Hubs

%description mgmt-notificationhubs
Microsoft Azure Python SDK - Resource Management - Notification Hubs

%package mgmt-nspkg
Version: 3.0.2
Summary: Microsoft Azure Python SDK - Resource Management - Namespace Package

%description mgmt-nspkg
Microsoft Azure Python SDK - Resource Management - Namespace Package

%package mgmt-operationsmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Operations Management

%description mgmt-operationsmanagement
Microsoft Azure Python SDK - Resource Management - Operations Management

%package mgmt-peering
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Peering

%description mgmt-peering
Microsoft Azure Python SDK - Resource Management - Peering

%package mgmt-policyinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Policy Insights

%description mgmt-policyinsights
Microsoft Azure Python SDK - Resource Management - Policy Insights

%package mgmt-powerbidedicated
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Power BI Dedicated

%description mgmt-powerbidedicated
Microsoft Azure Python SDK - Resource Management - Power BI Dedicated

%package mgmt-powerbiembedded
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Power BI Embedded

%description mgmt-powerbiembedded
Microsoft Azure Python SDK - Resource Management - Power BI Embedded

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

%package mgmt-resourcegraph
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resource Graph

%description mgmt-resourcegraph
Microsoft Azure Python SDK - Resource Management - Resource Graph

%package mgmt-resourcemover
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resource Mover

%description mgmt-resourcemover
Microsoft Azure Python SDK - Resource Management - Resource Mover

%package mgmt-scheduler
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Scheduler

%description mgmt-scheduler
Microsoft Azure Python SDK - Resource Management - Scheduler

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

%package mgmt-serialconsole
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Serial Console

%description mgmt-serialconsole
Microsoft Azure Python SDK - Resource Management - Serial Console

%package mgmt-servermanager
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Server Manager

%description mgmt-servermanager
Microsoft Azure Python SDK - Resource Management - Server Manager

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

%package mgmt-storagecache
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Cache

%description mgmt-storagecache
Microsoft Azure Python SDK - Resource Management - Storage Cache

%package mgmt-storageimportexport
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Import Export

%description mgmt-storageimportexport
Microsoft Azure Python SDK - Resource Management - Storage Import Export

%package mgmt-storagesync
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Sync

%description mgmt-storagesync
Microsoft Azure Python SDK - Resource Management - Storage Sync

%package mgmt-subscription
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Subscription

%description mgmt-subscription
Microsoft Azure Python SDK - Resource Management - Subscription

%package mgmt-support
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Support

%description mgmt-support
Microsoft Azure Python SDK - Resource Management - Support

%package mgmt-synapse
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Synapse

%description mgmt-synapse
Microsoft Azure Python SDK - Resource Management - Synapse

%package mgmt-timeseriesinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Time Series Insights

%description mgmt-timeseriesinsights
Microsoft Azure Python SDK - Resource Management - Time Series Insights

%package mgmt-trafficmanager
Version: 0.51.0
Summary: Microsoft Azure Python SDK - Resource Management - Traffic Manager

%description mgmt-trafficmanager
Microsoft Azure Python SDK - Resource Management - Traffic Manager

%package mgmt-vmwarecloudsimple
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - VM Ware Cloud Simple

%description mgmt-vmwarecloudsimple
Microsoft Azure Python SDK - Resource Management - VM Ware Cloud Simple

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

%package search-documents
Version: 11.1.0
Summary: Microsoft Azure Python SDK - Cognitive Search

%description search-documents
Microsoft Azure Python SDK - Cognitive Search

%package search-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Search Namespace Package

%description search-nspkg
Microsoft Azure Python SDK - Search Namespace Package

%package servicebus
Version: 7.2.0
Summary: Microsoft Azure Python SDK - Service Bus

%description servicebus
Microsoft Azure Python SDK - Service Bus

%package servicefabric
Version: 8.0.0.0
Summary: Microsoft Azure Python SDK - Service Fabric

%description servicefabric
Microsoft Azure Python SDK - Service Fabric

%package storage-blob
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Blobs

%description storage-blob
Microsoft Azure Python SDK - Storage - Blobs

%package storage-common
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Common

%description storage-common
Microsoft Azure Python SDK - Storage - Common

%package storage-file
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Files Shares

%description storage-file
Microsoft Azure Python SDK - Storage - Files Shares

%package storage-file-datalake
Version: 12.3.1
Summary: Microsoft Azure Python SDK - Storage - Files Data Lake

%description storage-file-datalake
Microsoft Azure Python SDK - Storage - Files Data Lake

%package storage-file-share
Version: 12.4.2
Summary: Microsoft Azure Python SDK - Storage - Files Shares

%description storage-file-share
Microsoft Azure Python SDK - Storage - Files Shares

%package storage-nspkg
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Storage Namespace Package

%description storage-nspkg
Microsoft Azure Python SDK - Storage Namespace Package

%package storage-queue
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Queues

%description storage-queue
Microsoft Azure Python SDK - Storage - Queues

%package synapse
Version: 0.1.1
Summary: Microsoft Azure Python SDK - Synapse

%description synapse
Microsoft Azure Python SDK - Synapse

%package synapse-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Synapse Namespace Package

%description synapse-nspkg
Microsoft Azure Python SDK - Synapse Namespace Package

%package template
Version: 0.0.17
Summary: Microsoft Azure Python SDK - Template

%description template
Microsoft Azure Python SDK - Template


%prep
# Create the base directory but skip any extractions for now.
%autosetup -n %{name}-%{version} -c -T
# Extract azure-ai-formrecognizer 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 0
# Extract azure-ai-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 1
# Extract azure-ai-textanalytics 5.0.0
%autosetup -n %{name}-%{version} -D -T -a 2
# Extract azure-appconfiguration 1.1.1
%autosetup -n %{name}-%{version} -D -T -a 3
# Extract azure-applicationinsights 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 4
# Extract azure-batch 10.0.0
%autosetup -n %{name}-%{version} -D -T -a 5
# Extract azure-cognitiveservices-anomalydetector 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 6
# Extract azure-cognitiveservices-formrecognizer 0.1.1
%autosetup -n %{name}-%{version} -D -T -a 7
# Extract azure-cognitiveservices-knowledge-nspkg 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 8
# Extract azure-cognitiveservices-knowledge-qnamaker 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 9
# Extract azure-cognitiveservices-language-luis 0.7.0
%autosetup -n %{name}-%{version} -D -T -a 10
# Extract azure-cognitiveservices-language-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 11
# Extract azure-cognitiveservices-language-spellcheck 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 12
# Extract azure-cognitiveservices-language-textanalytics 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 13
# Extract azure-cognitiveservices-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 14
# Extract azure-cognitiveservices-personalizer 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 15
# Extract azure-cognitiveservices-search-autosuggest 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 16
# Extract azure-cognitiveservices-search-customimagesearch 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 17
# Extract azure-cognitiveservices-search-customsearch 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 18
# Extract azure-cognitiveservices-search-entitysearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 19
# Extract azure-cognitiveservices-search-imagesearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 20
# Extract azure-cognitiveservices-search-newssearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 21
# Extract azure-cognitiveservices-search-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 22
# Extract azure-cognitiveservices-search-videosearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 23
# Extract azure-cognitiveservices-search-visualsearch 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 24
# Extract azure-cognitiveservices-search-websearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 25
# Extract azure-cognitiveservices-vision-computervision 0.9.0
%autosetup -n %{name}-%{version} -D -T -a 26
# Extract azure-cognitiveservices-vision-contentmoderator 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 27
# Extract azure-cognitiveservices-vision-customvision 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 28
# Extract azure-cognitiveservices-vision-face 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 29
# Extract azure-cognitiveservices-vision-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 30
# Extract azure-common 1.1.27
%autosetup -n %{name}-%{version} -D -T -a 31
# Extract azure-communication-chat 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 32
# Extract azure-communication-identity 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 33
# Extract azure-communication-phonenumbers 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 34
# Extract azure-communication-sms 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 35
# Extract azure-core 1.14.0
%autosetup -n %{name}-%{version} -D -T -a 36
# Extract azure-cosmos 3.2.0
%autosetup -n %{name}-%{version} -D -T -a 37
# Extract azure-cosmosdb-table 1.0.6
%autosetup -n %{name}-%{version} -D -T -a 38
# Extract azure-data-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 39
# Extract azure-datalake-store 0.0.51
%autosetup -n %{name}-%{version} -D -T -a 40
# Extract azure-digitaltwins-core 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 41
# Extract azure-digitaltwins-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 42
# Extract azure-eventgrid 4.2.0
%autosetup -n %{name}-%{version} -D -T -a 43
# Extract azure-eventhub 5.5.0
%autosetup -n %{name}-%{version} -D -T -a 44
# Extract azure-graphrbac 0.61.1
%autosetup -n %{name}-%{version} -D -T -a 45
# Extract azure-identity 1.6.0
%autosetup -n %{name}-%{version} -D -T -a 46
# Extract azure-iot-device 2.6.0
%autosetup -n %{name}-%{version} -D -T -a 47
# Extract azure-iot-hub 2.4.0
%autosetup -n %{name}-%{version} -D -T -a 48
# Extract azure-keyvault 4.1.0
%autosetup -n %{name}-%{version} -D -T -a 49
# Extract azure-keyvault-certificates 4.2.1
%autosetup -n %{name}-%{version} -D -T -a 50
# Extract azure-keyvault-keys 4.3.1
%autosetup -n %{name}-%{version} -D -T -a 51
# Extract azure-keyvault-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 52
# Extract azure-keyvault-secrets 4.2.0
%autosetup -n %{name}-%{version} -D -T -a 53
# Extract azure-kusto-data 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 54
# Extract azure-loganalytics 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 55
# Extract azure-mgmt-advisor 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 56
# Extract azure-mgmt-alertsmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 57
# Extract azure-mgmt-apimanagement 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 58
# Extract azure-mgmt-appconfiguration 1.0.1
%autosetup -n %{name}-%{version} -D -T -a 59
# Extract azure-mgmt-applicationinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 60
# Extract azure-mgmt-appplatform 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 61
# Extract azure-mgmt-attestation 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 62
# Extract azure-mgmt-authorization 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 63
# Extract azure-mgmt-automation 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 64
# Extract azure-mgmt-avs 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 65
# Extract azure-mgmt-azurestack 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 66
# Extract azure-mgmt-azurestackhci 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 67
# Extract azure-mgmt-batch 15.0.0
%autosetup -n %{name}-%{version} -D -T -a 68
# Extract azure-mgmt-batchai 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 69
# Extract azure-mgmt-billing 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 70
# Extract azure-mgmt-botservice 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 71
# Extract azure-mgmt-cdn 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 72
# Extract azure-mgmt-cognitiveservices 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 73
# Extract azure-mgmt-commerce 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 74
# Extract azure-mgmt-common 0.20.0
%autosetup -n %{name}-%{version} -D -T -a 75
# Extract azure-mgmt-communication 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 76
# Extract azure-mgmt-compute 21.0.0
%autosetup -n %{name}-%{version} -D -T -a 77
# Extract azure-mgmt-confluent 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 78
# Extract azure-mgmt-consumption 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 79
# Extract azure-mgmt-containerinstance 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 80
# Extract azure-mgmt-containerregistry 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 81
# Extract azure-mgmt-containerservice 15.1.0
%autosetup -n %{name}-%{version} -D -T -a 82
# Extract azure-mgmt-core 1.2.2
%autosetup -n %{name}-%{version} -D -T -a 83
# Extract azure-mgmt-cosmosdb 6.3.0
%autosetup -n %{name}-%{version} -D -T -a 84
# Extract azure-mgmt-costmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 85
# Extract azure-mgmt-customproviders 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 86
# Extract azure-mgmt-databox 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 87
# Extract azure-mgmt-databoxedge 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 88
# Extract azure-mgmt-databricks 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 89
# Extract azure-mgmt-datadog 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 90
# Extract azure-mgmt-datafactory 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 91
# Extract azure-mgmt-datalake-analytics 0.6.0
%autosetup -n %{name}-%{version} -D -T -a 92
# Extract azure-mgmt-datalake-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 93
# Extract azure-mgmt-datalake-store 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 94
# Extract azure-mgmt-datamigration 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 95
# Extract azure-mgmt-datashare 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 96
# Extract azure-mgmt-deploymentmanager 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 97
# Extract azure-mgmt-devspaces 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 98
# Extract azure-mgmt-devtestlabs 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 99
# Extract azure-mgmt-digitaltwins 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 100
# Extract azure-mgmt-dns 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 101
# Extract azure-mgmt-edgegateway 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 102
# Extract azure-mgmt-eventgrid 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 103
# Extract azure-mgmt-eventhub 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 104
# Extract azure-mgmt-frontdoor 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 105
# Extract azure-mgmt-hanaonazure 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 106
# Extract azure-mgmt-hdinsight 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 107
# Extract azure-mgmt-healthcareapis 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 108
# Extract azure-mgmt-hybridcompute 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 109
# Extract azure-mgmt-hybridkubernetes 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 110
# Extract azure-mgmt-imagebuilder 0.4.0
%autosetup -n %{name}-%{version} -D -T -a 111
# Extract azure-mgmt-iotcentral 4.1.0
%autosetup -n %{name}-%{version} -D -T -a 112
# Extract azure-mgmt-iothub 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 113
# Extract azure-mgmt-iothubprovisioningservices 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 114
# Extract azure-mgmt-keyvault 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 115
# Extract azure-mgmt-kusto 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 116
# Extract azure-mgmt-labservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 117
# Extract azure-mgmt-loganalytics 10.0.0
%autosetup -n %{name}-%{version} -D -T -a 118
# Extract azure-mgmt-logic 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 119
# Extract azure-mgmt-machinelearningcompute 0.4.1
%autosetup -n %{name}-%{version} -D -T -a 120
# Extract azure-mgmt-machinelearningservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 121
# Extract azure-mgmt-maintenance 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 122
# Extract azure-mgmt-managedservices 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 123
# Extract azure-mgmt-managementgroups 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 124
# Extract azure-mgmt-managementpartner 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 125
# Extract azure-mgmt-maps 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 126
# Extract azure-mgmt-marketplaceordering 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 127
# Extract azure-mgmt-media 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 128
# Extract azure-mgmt-mixedreality 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 129
# Extract azure-mgmt-monitor 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 130
# Extract azure-mgmt-msi 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 131
# Extract azure-mgmt-netapp 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 132
# Extract azure-mgmt-network 19.0.0
%autosetup -n %{name}-%{version} -D -T -a 133
# Extract azure-mgmt-notificationhubs 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 134
# Extract azure-mgmt-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 135
# Extract azure-mgmt-operationsmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 136
# Extract azure-mgmt-peering 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 137
# Extract azure-mgmt-policyinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 138
# Extract azure-mgmt-powerbidedicated 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 139
# Extract azure-mgmt-powerbiembedded 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 140
# Extract azure-mgmt-privatedns 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 141
# Extract azure-mgmt-rdbms 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 142
# Extract azure-mgmt-recoveryservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 143
# Extract azure-mgmt-recoveryservicesbackup 0.11.0
%autosetup -n %{name}-%{version} -D -T -a 144
# Extract azure-mgmt-redhatopenshift 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 145
# Extract azure-mgmt-redis 12.0.0
%autosetup -n %{name}-%{version} -D -T -a 146
# Extract azure-mgmt-relay 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 147
# Extract azure-mgmt-reservations 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 148
# Extract azure-mgmt-resource 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 149
# Extract azure-mgmt-resourcegraph 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 150
# Extract azure-mgmt-resourcemover 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 151
# Extract azure-mgmt-scheduler 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 152
# Extract azure-mgmt-search 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 153
# Extract azure-mgmt-security 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 154
# Extract azure-mgmt-serialconsole 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 155
# Extract azure-mgmt-servermanager 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 156
# Extract azure-mgmt-servicebus 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 157
# Extract azure-mgmt-sql 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 158
# Extract azure-mgmt-sqlvirtualmachine 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 159
# Extract azure-mgmt-storage 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 160
# Extract azure-mgmt-storagecache 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 161
# Extract azure-mgmt-storageimportexport 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 162
# Extract azure-mgmt-storagesync 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 163
# Extract azure-mgmt-subscription 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 164
# Extract azure-mgmt-support 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 165
# Extract azure-mgmt-synapse 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 166
# Extract azure-mgmt-timeseriesinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 167
# Extract azure-mgmt-trafficmanager 0.51.0
%autosetup -n %{name}-%{version} -D -T -a 168
# Extract azure-mgmt-vmwarecloudsimple 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 169
# Extract azure-mgmt-web 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 170
# Extract azure-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 171
# Extract azure-search-documents 11.1.0
%autosetup -n %{name}-%{version} -D -T -a 172
# Extract azure-search-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 173
# Extract azure-servicebus 7.2.0
%autosetup -n %{name}-%{version} -D -T -a 174
# Extract azure-servicefabric 8.0.0.0
%autosetup -n %{name}-%{version} -D -T -a 175
# Extract azure-storage-blob 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 176
# Extract azure-storage-common 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 177
# Extract azure-storage-file 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 178
# Extract azure-storage-file-datalake 12.3.1
%autosetup -n %{name}-%{version} -D -T -a 179
# Extract azure-storage-file-share 12.4.2
%autosetup -n %{name}-%{version} -D -T -a 180
# Extract azure-storage-nspkg 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 181
# Extract azure-storage-queue 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 182
# Extract azure-synapse 0.1.1
%autosetup -n %{name}-%{version} -D -T -a 183
# Extract azure-synapse-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 184
# Extract azure-template 0.0.17
%autosetup -n %{name}-%{version} -D -T -a 185


%build
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %py3_build
    popd
done

%install
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %py3_install
    popd
done

rm -rf %{buildroot}%{python3_sitelib}/{doc,samples,tests}

%files
%{python3_sitelib}/azure/__init__.py
%{python3_sitelib}/azure/__pycache__/__init__*



%files ai-formrecognizer
%{python3_sitelib}/azure/ai/formrecognizer
%{python3_sitelib}/azure_ai_formrecognizer-*.egg-info/


%files ai-nspkg
%{python3_sitelib}/azure_ai_nspkg-*.egg-info/


%files ai-textanalytics
%{python3_sitelib}/azure/ai/textanalytics
%{python3_sitelib}/azure_ai_textanalytics-*.egg-info/


%files appconfiguration
%{python3_sitelib}/azure/appconfiguration
%{python3_sitelib}/azure_appconfiguration-*.egg-info/


%files applicationinsights
%{python3_sitelib}/azure/applicationinsights
%{python3_sitelib}/azure_applicationinsights-*.egg-info/


%files batch
%{python3_sitelib}/azure/batch
%{python3_sitelib}/azure_batch-*.egg-info/


%files cognitiveservices-anomalydetector
%{python3_sitelib}/azure/cognitiveservices/anomalydetector
%{python3_sitelib}/azure_cognitiveservices_anomalydetector-*.egg-info/


%files cognitiveservices-formrecognizer
%{python3_sitelib}/azure/cognitiveservices/formrecognizer
%{python3_sitelib}/azure_cognitiveservices_formrecognizer-*.egg-info/


%files cognitiveservices-knowledge-nspkg
%{python3_sitelib}/azure_cognitiveservices_knowledge_nspkg-*.egg-info/


%files cognitiveservices-knowledge-qnamaker
%{python3_sitelib}/azure/cognitiveservices/knowledge/qnamaker
%{python3_sitelib}/azure_cognitiveservices_knowledge_qnamaker-*.egg-info/


%files cognitiveservices-language-luis
%{python3_sitelib}/azure/cognitiveservices/language/luis
%{python3_sitelib}/azure_cognitiveservices_language_luis-*.egg-info/


%files cognitiveservices-language-nspkg
%{python3_sitelib}/azure_cognitiveservices_language_nspkg-*.egg-info/


%files cognitiveservices-language-spellcheck
%{python3_sitelib}/azure/cognitiveservices/language/spellcheck
%{python3_sitelib}/azure_cognitiveservices_language_spellcheck-*.egg-info/


%files cognitiveservices-language-textanalytics
%{python3_sitelib}/azure/cognitiveservices/language/textanalytics
%{python3_sitelib}/azure_cognitiveservices_language_textanalytics-*.egg-info/


%files cognitiveservices-nspkg
%{python3_sitelib}/azure_cognitiveservices_nspkg-*.egg-info/


%files cognitiveservices-personalizer
%{python3_sitelib}/azure/cognitiveservices/personalizer
%{python3_sitelib}/azure_cognitiveservices_personalizer-*.egg-info/


%files cognitiveservices-search-autosuggest
%{python3_sitelib}/azure/cognitiveservices/search/autosuggest
%{python3_sitelib}/azure_cognitiveservices_search_autosuggest-*.egg-info/


%files cognitiveservices-search-customimagesearch
%{python3_sitelib}/azure/cognitiveservices/search/customimagesearch
%{python3_sitelib}/azure_cognitiveservices_search_customimagesearch-*.egg-info/


%files cognitiveservices-search-customsearch
%{python3_sitelib}/azure/cognitiveservices/search/customsearch
%{python3_sitelib}/azure_cognitiveservices_search_customsearch-*.egg-info/


%files cognitiveservices-search-entitysearch
%{python3_sitelib}/azure/cognitiveservices/search/entitysearch
%{python3_sitelib}/azure_cognitiveservices_search_entitysearch-*.egg-info/


%files cognitiveservices-search-imagesearch
%{python3_sitelib}/azure/cognitiveservices/search/imagesearch
%{python3_sitelib}/azure_cognitiveservices_search_imagesearch-*.egg-info/


%files cognitiveservices-search-newssearch
%{python3_sitelib}/azure/cognitiveservices/search/newssearch
%{python3_sitelib}/azure_cognitiveservices_search_newssearch-*.egg-info/


%files cognitiveservices-search-nspkg
%{python3_sitelib}/azure_cognitiveservices_search_nspkg-*.egg-info/


%files cognitiveservices-search-videosearch
%{python3_sitelib}/azure/cognitiveservices/search/videosearch
%{python3_sitelib}/azure_cognitiveservices_search_videosearch-*.egg-info/


%files cognitiveservices-search-visualsearch
%{python3_sitelib}/azure/cognitiveservices/search/visualsearch
%{python3_sitelib}/azure_cognitiveservices_search_visualsearch-*.egg-info/


%files cognitiveservices-search-websearch
%{python3_sitelib}/azure/cognitiveservices/search/websearch
%{python3_sitelib}/azure_cognitiveservices_search_websearch-*.egg-info/


%files cognitiveservices-vision-computervision
%{python3_sitelib}/azure/cognitiveservices/vision/computervision
%{python3_sitelib}/azure_cognitiveservices_vision_computervision-*.egg-info/


%files cognitiveservices-vision-contentmoderator
%{python3_sitelib}/azure/cognitiveservices/vision/contentmoderator
%{python3_sitelib}/azure_cognitiveservices_vision_contentmoderator-*.egg-info/


%files cognitiveservices-vision-customvision
%{python3_sitelib}/azure/cognitiveservices/vision/customvision
%{python3_sitelib}/azure_cognitiveservices_vision_customvision-*.egg-info/


%files cognitiveservices-vision-face
%{python3_sitelib}/azure/cognitiveservices/vision/face
%{python3_sitelib}/azure_cognitiveservices_vision_face-*.egg-info/


%files cognitiveservices-vision-nspkg
%{python3_sitelib}/azure_cognitiveservices_vision_nspkg-*.egg-info/


%files common
%{python3_sitelib}/azure/common
%{python3_sitelib}/azure_common-*.egg-info/
%{python3_sitelib}/azure/profiles/__init__.py
%{python3_sitelib}/azure/profiles/__pycache__/__init__*
%{python3_sitelib}/azure/profiles/multiapiclient.py
%{python3_sitelib}/azure/profiles/__pycache__/multiapiclient*.pyc


%files communication-chat
%{python3_sitelib}/azure/communication/chat
%{python3_sitelib}/azure_communication_chat-*.egg-info/


%files communication-identity
%{python3_sitelib}/azure/communication/identity
%{python3_sitelib}/azure_communication_identity-*.egg-info/


%files communication-phonenumbers
%{python3_sitelib}/azure/communication/phonenumbers
%{python3_sitelib}/azure_communication_phonenumbers-*.egg-info/


%files communication-sms
%{python3_sitelib}/azure/communication/sms
%{python3_sitelib}/azure_communication_sms-*.egg-info/


%files core
%{python3_sitelib}/azure/core
%{python3_sitelib}/azure_core-*.egg-info/


%files cosmos
%{python3_sitelib}/azure/cosmos
%{python3_sitelib}/azure_cosmos-*.egg-info/


%files cosmosdb-table
%{python3_sitelib}/azure/cosmosdb/table
%{python3_sitelib}/azure_cosmosdb_table-*.egg-info/


%files data-nspkg
%{python3_sitelib}/azure_data_nspkg-*.egg-info/
%{python3_sitelib}/azure/data/__init__.py
%{python3_sitelib}/azure/data/__pycache__/__init__*


%files datalake-store
%{python3_sitelib}/azure/datalake/store
%{python3_sitelib}/azure_datalake_store-*.egg-info/
%{python3_sitelib}/azure/datalake/__init__.py
%{python3_sitelib}/azure/datalake/__pycache__/__init__*


%files digitaltwins-core
%{python3_sitelib}/azure/digitaltwins/core
%{python3_sitelib}/azure_digitaltwins_core-*.egg-info/


%files digitaltwins-nspkg
%{python3_sitelib}/azure_digitaltwins_nspkg-*.egg-info/
%{python3_sitelib}/azure/digitaltwins/__init__.py
%{python3_sitelib}/azure/digitaltwins/__pycache__/__init__*


%files eventgrid
%{python3_sitelib}/azure/eventgrid
%{python3_sitelib}/azure_eventgrid-*.egg-info/


%files eventhub
%{python3_sitelib}/azure/eventhub
%{python3_sitelib}/azure_eventhub-*.egg-info/


%files graphrbac
%{python3_sitelib}/azure/graphrbac
%{python3_sitelib}/azure_graphrbac-*.egg-info/


%files identity
%{python3_sitelib}/azure/identity
%{python3_sitelib}/azure_identity-*.egg-info/


%files iot-device
%{python3_sitelib}/azure/iot/device
%{python3_sitelib}/azure_iot_device-*.egg-info/


%files iot-hub
%{python3_sitelib}/azure/iot/hub
%{python3_sitelib}/azure_iot_hub-*.egg-info/


%files keyvault
%{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure_keyvault-*.egg-info/


%files keyvault-certificates
%{python3_sitelib}/azure/keyvault/certificates
%{python3_sitelib}/azure_keyvault_certificates-*.egg-info/


%files keyvault-keys
%{python3_sitelib}/azure/keyvault/keys
%{python3_sitelib}/azure_keyvault_keys-*.egg-info/


%files keyvault-nspkg
%{python3_sitelib}/azure_keyvault_nspkg-*.egg-info/


%files keyvault-secrets
%{python3_sitelib}/azure/keyvault/secrets
%{python3_sitelib}/azure_keyvault_secrets-*.egg-info/


%files kusto-data
%{python3_sitelib}/azure/kusto/data
%{python3_sitelib}/azure_kusto_data-*.egg-info/
%{python3_sitelib}/azure/kusto/__init__.py
%{python3_sitelib}/azure/kusto/__pycache__/__init__*
%{python3_sitelib}/azure_kusto_data-*.pth


%files loganalytics
%{python3_sitelib}/azure/loganalytics
%{python3_sitelib}/azure_loganalytics-*.egg-info/


%files mgmt-advisor
%{python3_sitelib}/azure/mgmt/advisor
%{python3_sitelib}/azure_mgmt_advisor-*.egg-info/


%files mgmt-alertsmanagement
%{python3_sitelib}/azure/mgmt/alertsmanagement
%{python3_sitelib}/azure_mgmt_alertsmanagement-*.egg-info/


%files mgmt-apimanagement
%{python3_sitelib}/azure/mgmt/apimanagement
%{python3_sitelib}/azure_mgmt_apimanagement-*.egg-info/


%files mgmt-appconfiguration
%{python3_sitelib}/azure/mgmt/appconfiguration
%{python3_sitelib}/azure_mgmt_appconfiguration-*.egg-info/


%files mgmt-applicationinsights
%{python3_sitelib}/azure/mgmt/applicationinsights
%{python3_sitelib}/azure_mgmt_applicationinsights-*.egg-info/


%files mgmt-appplatform
%{python3_sitelib}/azure/mgmt/appplatform
%{python3_sitelib}/azure_mgmt_appplatform-*.egg-info/


%files mgmt-attestation
%{python3_sitelib}/azure/mgmt/attestation
%{python3_sitelib}/azure_mgmt_attestation-*.egg-info/


%files mgmt-authorization
%{python3_sitelib}/azure/mgmt/authorization
%{python3_sitelib}/azure_mgmt_authorization-*.egg-info/


%files mgmt-automation
%{python3_sitelib}/azure/mgmt/automation
%{python3_sitelib}/azure_mgmt_automation-*.egg-info/


%files mgmt-avs
%{python3_sitelib}/azure/mgmt/avs
%{python3_sitelib}/azure_mgmt_avs-*.egg-info/


%files mgmt-azurestack
%{python3_sitelib}/azure/mgmt/azurestack
%{python3_sitelib}/azure_mgmt_azurestack-*.egg-info/


%files mgmt-azurestackhci
%{python3_sitelib}/azure/mgmt/azurestackhci
%{python3_sitelib}/azure_mgmt_azurestackhci-*.egg-info/


%files mgmt-batch
%{python3_sitelib}/azure/mgmt/batch
%{python3_sitelib}/azure_mgmt_batch-*.egg-info/


%files mgmt-batchai
%{python3_sitelib}/azure/mgmt/batchai
%{python3_sitelib}/azure_mgmt_batchai-*.egg-info/


%files mgmt-billing
%{python3_sitelib}/azure/mgmt/billing
%{python3_sitelib}/azure_mgmt_billing-*.egg-info/


%files mgmt-botservice
%{python3_sitelib}/azure/mgmt/botservice
%{python3_sitelib}/azure_mgmt_botservice-*.egg-info/


%files mgmt-cdn
%{python3_sitelib}/azure/mgmt/cdn
%{python3_sitelib}/azure_mgmt_cdn-*.egg-info/


%files mgmt-cognitiveservices
%{python3_sitelib}/azure/mgmt/cognitiveservices
%{python3_sitelib}/azure_mgmt_cognitiveservices-*.egg-info/


%files mgmt-commerce
%{python3_sitelib}/azure/mgmt/commerce
%{python3_sitelib}/azure_mgmt_commerce-*.egg-info/


%files mgmt-common
%{python3_sitelib}/azure/mgmt/common
%{python3_sitelib}/azure_mgmt_common-*.egg-info/


%files mgmt-communication
%{python3_sitelib}/azure/mgmt/communication
%{python3_sitelib}/azure_mgmt_communication-*.egg-info/


%files mgmt-compute
%{python3_sitelib}/azure/mgmt/compute
%{python3_sitelib}/azure_mgmt_compute-*.egg-info/


%files mgmt-confluent
%{python3_sitelib}/azure/mgmt/confluent
%{python3_sitelib}/azure_mgmt_confluent-*.egg-info/


%files mgmt-consumption
%{python3_sitelib}/azure/mgmt/consumption
%{python3_sitelib}/azure_mgmt_consumption-*.egg-info/


%files mgmt-containerinstance
%{python3_sitelib}/azure/mgmt/containerinstance
%{python3_sitelib}/azure_mgmt_containerinstance-*.egg-info/


%files mgmt-containerregistry
%{python3_sitelib}/azure/mgmt/containerregistry
%{python3_sitelib}/azure_mgmt_containerregistry-*.egg-info/


%files mgmt-containerservice
%{python3_sitelib}/azure/mgmt/containerservice
%{python3_sitelib}/azure_mgmt_containerservice-*.egg-info/


%files mgmt-core
%{python3_sitelib}/azure/mgmt/core
%{python3_sitelib}/azure_mgmt_core-*.egg-info/
%{python3_sitelib}/azure/mgmt/__init__.py
%{python3_sitelib}/azure/mgmt/__pycache__/__init__*


%files mgmt-cosmosdb
%{python3_sitelib}/azure/mgmt/cosmosdb
%{python3_sitelib}/azure_mgmt_cosmosdb-*.egg-info/
%{python3_sitelib}/azure/cosmosdb/__init__.py
%{python3_sitelib}/azure/cosmosdb/__pycache__/__init__*


%files mgmt-costmanagement
%{python3_sitelib}/azure/mgmt/costmanagement
%{python3_sitelib}/azure_mgmt_costmanagement-*.egg-info/


%files mgmt-customproviders
%{python3_sitelib}/azure/mgmt/customproviders
%{python3_sitelib}/azure_mgmt_customproviders-*.egg-info/


%files mgmt-databox
%{python3_sitelib}/azure/mgmt/databox
%{python3_sitelib}/azure_mgmt_databox-*.egg-info/


%files mgmt-databoxedge
%{python3_sitelib}/azure/mgmt/databoxedge
%{python3_sitelib}/azure_mgmt_databoxedge-*.egg-info/
%{python3_sitelib}/azure/mgmt/datab


%files mgmt-databricks
%{python3_sitelib}/azure/mgmt/databricks
%{python3_sitelib}/azure_mgmt_databricks-*.egg-info/


%files mgmt-datadog
%{python3_sitelib}/azure/mgmt/datadog
%{python3_sitelib}/azure_mgmt_datadog-*.egg-info/


%files mgmt-datafactory
%{python3_sitelib}/azure/mgmt/datafactory
%{python3_sitelib}/azure_mgmt_datafactory-*.egg-info/


%files mgmt-datalake-analytics
%{python3_sitelib}/azure/mgmt/datalake/analytics
%{python3_sitelib}/azure_mgmt_datalake_analytics-*.egg-info/
%{python3_sitelib}/azure/mgmt/datalake/__init__.py
%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__*


%files mgmt-datalake-nspkg
%{python3_sitelib}/azure_mgmt_datalake_nspkg-*.egg-info/


%files mgmt-datalake-store
%{python3_sitelib}/azure/mgmt/datalake/store
%{python3_sitelib}/azure_mgmt_datalake_store-*.egg-info/


%files mgmt-datamigration
%{python3_sitelib}/azure/mgmt/datamigration
%{python3_sitelib}/azure_mgmt_datamigration-*.egg-info/


%files mgmt-datashare
%{python3_sitelib}/azure/mgmt/datashare
%{python3_sitelib}/azure_mgmt_datashare-*.egg-info/


%files mgmt-deploymentmanager
%{python3_sitelib}/azure/mgmt/deploymentmanager
%{python3_sitelib}/azure_mgmt_deploymentmanager-*.egg-info/


%files mgmt-devspaces
%{python3_sitelib}/azure/mgmt/devspaces
%{python3_sitelib}/azure_mgmt_devspaces-*.egg-info/


%files mgmt-devtestlabs
%{python3_sitelib}/azure/mgmt/devtestlabs
%{python3_sitelib}/azure_mgmt_devtestlabs-*.egg-info/


%files mgmt-digitaltwins
%{python3_sitelib}/azure/mgmt/digitaltwins
%{python3_sitelib}/azure_mgmt_digitaltwins-*.egg-info/


%files mgmt-dns
%{python3_sitelib}/azure/mgmt/dns
%{python3_sitelib}/azure_mgmt_dns-*.egg-info/


%files mgmt-edgegateway
%{python3_sitelib}/azure/mgmt/edgegateway
%{python3_sitelib}/azure_mgmt_edgegateway-*.egg-info/


%files mgmt-eventgrid
%{python3_sitelib}/azure/mgmt/eventgrid
%{python3_sitelib}/azure_mgmt_eventgrid-*.egg-info/


%files mgmt-eventhub
%{python3_sitelib}/azure/mgmt/eventhub
%{python3_sitelib}/azure_mgmt_eventhub-*.egg-info/


%files mgmt-frontdoor
%{python3_sitelib}/azure/mgmt/frontdoor
%{python3_sitelib}/azure_mgmt_frontdoor-*.egg-info/


%files mgmt-hanaonazure
%{python3_sitelib}/azure/mgmt/hanaonazure
%{python3_sitelib}/azure_mgmt_hanaonazure-*.egg-info/


%files mgmt-hdinsight
%{python3_sitelib}/azure/mgmt/hdinsight
%{python3_sitelib}/azure_mgmt_hdinsight-*.egg-info/


%files mgmt-healthcareapis
%{python3_sitelib}/azure/mgmt/healthcareapis
%{python3_sitelib}/azure_mgmt_healthcareapis-*.egg-info/


%files mgmt-hybridcompute
%{python3_sitelib}/azure/mgmt/hybridcompute
%{python3_sitelib}/azure_mgmt_hybridcompute-*.egg-info/


%files mgmt-hybridkubernetes
%{python3_sitelib}/azure/mgmt/hybridkubernetes
%{python3_sitelib}/azure_mgmt_hybridkubernetes-*.egg-info/


%files mgmt-imagebuilder
%{python3_sitelib}/azure/mgmt/imagebuilder
%{python3_sitelib}/azure_mgmt_imagebuilder-*.egg-info/


%files mgmt-iotcentral
%{python3_sitelib}/azure/mgmt/iotcentral
%{python3_sitelib}/azure_mgmt_iotcentral-*.egg-info/


%files mgmt-iothub
%{python3_sitelib}/azure/mgmt/iothub
%{python3_sitelib}/azure_mgmt_iothub-*.egg-info/


%files mgmt-iothubprovisioningservices
%{python3_sitelib}/azure/mgmt/iothubprovisioningservices
%{python3_sitelib}/azure_mgmt_iothubprovisioningservices-*.egg-info/


%files mgmt-keyvault
%{python3_sitelib}/azure/mgmt/keyvault
%{python3_sitelib}/azure_mgmt_keyvault-*.egg-info/


%files mgmt-kusto
%{python3_sitelib}/azure/mgmt/kusto
%{python3_sitelib}/azure_mgmt_kusto-*.egg-info/


%files mgmt-labservices
%{python3_sitelib}/azure/mgmt/labservices
%{python3_sitelib}/azure_mgmt_labservices-*.egg-info/


%files mgmt-loganalytics
%{python3_sitelib}/azure/mgmt/loganalytics
%{python3_sitelib}/azure_mgmt_loganalytics-*.egg-info/


%files mgmt-logic
%{python3_sitelib}/azure/mgmt/logic
%{python3_sitelib}/azure_mgmt_logic-*.egg-info/


%files mgmt-machinelearningcompute
%{python3_sitelib}/azure/mgmt/machinelearningcompute
%{python3_sitelib}/azure_mgmt_machinelearningcompute-*.egg-info/


%files mgmt-machinelearningservices
%{python3_sitelib}/azure/mgmt/machinelearningservices
%{python3_sitelib}/azure_mgmt_machinelearningservices-*.egg-info/


%files mgmt-maintenance
%{python3_sitelib}/azure/mgmt/maintenance
%{python3_sitelib}/azure_mgmt_maintenance-*.egg-info/


%files mgmt-managedservices
%{python3_sitelib}/azure/mgmt/managedservices
%{python3_sitelib}/azure_mgmt_managedservices-*.egg-info/


%files mgmt-managementgroups
%{python3_sitelib}/azure/mgmt/managementgroups
%{python3_sitelib}/azure_mgmt_managementgroups-*.egg-info/


%files mgmt-managementpartner
%{python3_sitelib}/azure/mgmt/managementpartner
%{python3_sitelib}/azure_mgmt_managementpartner-*.egg-info/


%files mgmt-maps
%{python3_sitelib}/azure/mgmt/maps
%{python3_sitelib}/azure_mgmt_maps-*.egg-info/


%files mgmt-marketplaceordering
%{python3_sitelib}/azure/mgmt/marketplaceordering
%{python3_sitelib}/azure_mgmt_marketplaceordering-*.egg-info/


%files mgmt-media
%{python3_sitelib}/azure/mgmt/media
%{python3_sitelib}/azure_mgmt_media-*.egg-info/


%files mgmt-mixedreality
%{python3_sitelib}/azure/mgmt/mixedreality
%{python3_sitelib}/azure_mgmt_mixedreality-*.egg-info/


%files mgmt-monitor
%{python3_sitelib}/azure/mgmt/monitor
%{python3_sitelib}/azure_mgmt_monitor-*.egg-info/


%files mgmt-msi
%{python3_sitelib}/azure/mgmt/msi
%{python3_sitelib}/azure_mgmt_msi-*.egg-info/


%files mgmt-netapp
%{python3_sitelib}/azure/mgmt/netapp
%{python3_sitelib}/azure_mgmt_netapp-*.egg-info/


%files mgmt-network
%{python3_sitelib}/azure/mgmt/network
%{python3_sitelib}/azure_mgmt_network-*.egg-info/


%files mgmt-notificationhubs
%{python3_sitelib}/azure/mgmt/notificationhubs
%{python3_sitelib}/azure_mgmt_notificationhubs-*.egg-info/


%files mgmt-nspkg
%{python3_sitelib}/azure_mgmt_nspkg-*.egg-info/


%files mgmt-operationsmanagement
%{python3_sitelib}/azure/mgmt/operationsmanagement
%{python3_sitelib}/azure_mgmt_operationsmanagement-*.egg-info/


%files mgmt-peering
%{python3_sitelib}/azure/mgmt/peering
%{python3_sitelib}/azure_mgmt_peering-*.egg-info/


%files mgmt-policyinsights
%{python3_sitelib}/azure/mgmt/policyinsights
%{python3_sitelib}/azure_mgmt_policyinsights-*.egg-info/


%files mgmt-powerbidedicated
%{python3_sitelib}/azure/mgmt/powerbidedicated
%{python3_sitelib}/azure_mgmt_powerbidedicated-*.egg-info/


%files mgmt-powerbiembedded
%{python3_sitelib}/azure/mgmt/powerbiembedded
%{python3_sitelib}/azure_mgmt_powerbiembedded-*.egg-info/


%files mgmt-privatedns
%{python3_sitelib}/azure/mgmt/privatedns
%{python3_sitelib}/azure_mgmt_privatedns-*.egg-info/


%files mgmt-rdbms
%{python3_sitelib}/azure/mgmt/rdbms
%{python3_sitelib}/azure_mgmt_rdbms-*.egg-info/


%files mgmt-recoveryservices
%{python3_sitelib}/azure/mgmt/recoveryservices
%{python3_sitelib}/azure_mgmt_recoveryservices-*.egg-info/


%files mgmt-recoveryservicesbackup
%{python3_sitelib}/azure/mgmt/recoveryservicesbackup
%{python3_sitelib}/azure_mgmt_recoveryservicesbackup-*.egg-info/


%files mgmt-redhatopenshift
%{python3_sitelib}/azure/mgmt/redhatopenshift
%{python3_sitelib}/azure_mgmt_redhatopenshift-*.egg-info/


%files mgmt-redis
%{python3_sitelib}/azure/mgmt/redis
%{python3_sitelib}/azure_mgmt_redis-*.egg-info/


%files mgmt-relay
%{python3_sitelib}/azure/mgmt/relay
%{python3_sitelib}/azure_mgmt_relay-*.egg-info/


%files mgmt-reservations
%{python3_sitelib}/azure/mgmt/reservations
%{python3_sitelib}/azure_mgmt_reservations-*.egg-info/


%files mgmt-resource
%{python3_sitelib}/azure/mgmt/resource
%{python3_sitelib}/azure_mgmt_resource-*.egg-info/


%files mgmt-resourcegraph
%{python3_sitelib}/azure/mgmt/resourcegraph
%{python3_sitelib}/azure_mgmt_resourcegraph-*.egg-info/


%files mgmt-resourcemover
%{python3_sitelib}/azure/mgmt/resourcemover
%{python3_sitelib}/azure_mgmt_resourcemover-*.egg-info/


%files mgmt-scheduler
%{python3_sitelib}/azure/mgmt/scheduler
%{python3_sitelib}/azure_mgmt_scheduler-*.egg-info/


%files mgmt-search
%{python3_sitelib}/azure/mgmt/search
%{python3_sitelib}/azure_mgmt_search-*.egg-info/


%files mgmt-security
%{python3_sitelib}/azure/mgmt/security
%{python3_sitelib}/azure_mgmt_security-*.egg-info/


%files mgmt-serialconsole
%{python3_sitelib}/azure/mgmt/serialconsole
%{python3_sitelib}/azure_mgmt_serialconsole-*.egg-info/


%files mgmt-servermanager
%{python3_sitelib}/azure/mgmt/servermanager
%{python3_sitelib}/azure_mgmt_servermanager-*.egg-info/


%files mgmt-servicebus
%{python3_sitelib}/azure/mgmt/servicebus
%{python3_sitelib}/azure_mgmt_servicebus-*.egg-info/


%files mgmt-sql
%{python3_sitelib}/azure/mgmt/sql
%{python3_sitelib}/azure_mgmt_sql-*.egg-info/


%files mgmt-sqlvirtualmachine
%{python3_sitelib}/azure/mgmt/sqlvirtualmachine
%{python3_sitelib}/azure_mgmt_sqlvirtualmachine-*.egg-info/


%files mgmt-storage
%{python3_sitelib}/azure/mgmt/storage
%{python3_sitelib}/azure_mgmt_storage-*.egg-info/


%files mgmt-storagecache
%{python3_sitelib}/azure/mgmt/storagecache
%{python3_sitelib}/azure_mgmt_storagecache-*.egg-info/


%files mgmt-storageimportexport
%{python3_sitelib}/azure/mgmt/storageimportexport
%{python3_sitelib}/azure_mgmt_storageimportexport-*.egg-info/


%files mgmt-storagesync
%{python3_sitelib}/azure/mgmt/storagesync
%{python3_sitelib}/azure_mgmt_storagesync-*.egg-info/


%files mgmt-subscription
%{python3_sitelib}/azure/mgmt/subscription
%{python3_sitelib}/azure_mgmt_subscription-*.egg-info/


%files mgmt-support
%{python3_sitelib}/azure/mgmt/support
%{python3_sitelib}/azure_mgmt_support-*.egg-info/


%files mgmt-synapse
%{python3_sitelib}/azure/mgmt/synapse
%{python3_sitelib}/azure_mgmt_synapse-*.egg-info/


%files mgmt-timeseriesinsights
%{python3_sitelib}/azure/mgmt/timeseriesinsights
%{python3_sitelib}/azure_mgmt_timeseriesinsights-*.egg-info/


%files mgmt-trafficmanager
%{python3_sitelib}/azure/mgmt/trafficmanager
%{python3_sitelib}/azure_mgmt_trafficmanager-*.egg-info/


%files mgmt-vmwarecloudsimple
%{python3_sitelib}/azure/mgmt/vmwarecloudsimple
%{python3_sitelib}/azure_mgmt_vmwarecloudsimple-*.egg-info/


%files mgmt-web
%{python3_sitelib}/azure/mgmt/web
%{python3_sitelib}/azure_mgmt_web-*.egg-info/


%files nspkg
%{python3_sitelib}/azure_nspkg-*.egg-info/


%files search-documents
%{python3_sitelib}/azure/search/documents
%{python3_sitelib}/azure_search_documents-*.egg-info/


%files search-nspkg
%{python3_sitelib}/azure_search_nspkg-*.egg-info/


%files servicebus
%{python3_sitelib}/azure/servicebus
%{python3_sitelib}/azure_servicebus-*.egg-info/


%files servicefabric
%{python3_sitelib}/azure/servicefabric
%{python3_sitelib}/azure_servicefabric-*.egg-info/


%files storage-blob
%{python3_sitelib}/azure/storage/blob
%{python3_sitelib}/azure_storage_blob-*.egg-info/


%files storage-common
%{python3_sitelib}/azure/storage/common
%{python3_sitelib}/azure_storage_common-*.egg-info/


%files storage-file
%{python3_sitelib}/azure/storage/file
%{python3_sitelib}/azure_storage_file-*.egg-info/


%files storage-file-datalake
%{python3_sitelib}/azure/storage/filedatalake
%{python3_sitelib}/azure_storage_file_datalake-*.egg-info/


%files storage-file-share
%{python3_sitelib}/azure/storage/fileshare
%{python3_sitelib}/azure_storage_file_share-*.egg-info/


%files storage-nspkg
%{python3_sitelib}/azure_storage_nspkg-*.egg-info/
%{python3_sitelib}/azure/storage/__init__.py
%{python3_sitelib}/azure/storage/__pycache__/__init__*


%files storage-queue
%{python3_sitelib}/azure/storage/queue
%{python3_sitelib}/azure_storage_queue-*.egg-info/


%files synapse
%{python3_sitelib}/azure/synapse
%{python3_sitelib}/azure_synapse-*.egg-info/


%files synapse-nspkg
%{python3_sitelib}/azure_synapse_nspkg-*.egg-info/


%files template
%{python3_sitelib}/azure/template
%{python3_sitelib}/azure_template-*.egg-info/



%changelog
* Thu May 27 2021 Major Hayden - 20210527-1
- First package.