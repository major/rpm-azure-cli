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
Source0:        %{pypi_source azure-ai-textanalytics 5.0.0 zip}
Source1:        %{pypi_source azure-appconfiguration 1.1.1 zip}
Source2:        %{pypi_source azure-applicationinsights 0.1.0 zip}
Source3:        %{pypi_source azure-batch 10.0.0 zip}
Source4:        %{pypi_source azure-cognitiveservices-anomalydetector 0.3.0 zip}
Source5:        %{pypi_source azure-cognitiveservices-formrecognizer 0.1.1 zip}
Source6:        %{pypi_source azure-cognitiveservices-knowledge-nspkg 3.0.0 zip}
Source7:        %{pypi_source azure-cognitiveservices-knowledge-qnamaker 0.3.0 zip}
Source8:        %{pypi_source azure-cognitiveservices-language-luis 0.7.0 zip}
Source9:        %{pypi_source azure-cognitiveservices-language-nspkg 3.0.1 zip}
Source10:       %{pypi_source azure-cognitiveservices-language-spellcheck 2.0.0 zip}
Source11:       %{pypi_source azure-cognitiveservices-language-textanalytics 0.2.0 zip}
Source12:       %{pypi_source azure-cognitiveservices-nspkg 3.0.1 zip}
Source13:       %{pypi_source azure-cognitiveservices-personalizer 0.1.0 zip}
Source14:       %{pypi_source azure-cognitiveservices-search-autosuggest 0.2.0 zip}
Source15:       %{pypi_source azure-cognitiveservices-search-customimagesearch 0.2.0 zip}
Source16:       %{pypi_source azure-cognitiveservices-search-customsearch 0.3.0 zip}
Source17:       %{pypi_source azure-cognitiveservices-search-entitysearch 2.0.0 zip}
Source18:       %{pypi_source azure-cognitiveservices-search-imagesearch 2.0.0 zip}
Source19:       %{pypi_source azure-cognitiveservices-search-newssearch 2.0.0 zip}
Source20:       %{pypi_source azure-cognitiveservices-search-nspkg 3.0.1 zip}
Source21:       %{pypi_source azure-cognitiveservices-search-videosearch 2.0.0 zip}
Source22:       %{pypi_source azure-cognitiveservices-search-visualsearch 0.2.0 zip}
Source23:       %{pypi_source azure-cognitiveservices-search-websearch 2.0.0 zip}
Source24:       %{pypi_source azure-cognitiveservices-vision-computervision 0.9.0 zip}
Source25:       %{pypi_source azure-cognitiveservices-vision-contentmoderator 1.0.0 zip}
Source26:       %{pypi_source azure-cognitiveservices-vision-customvision 3.1.0 zip}
Source27:       %{pypi_source azure-cognitiveservices-vision-face 0.5.0 zip}
Source28:       %{pypi_source azure-cognitiveservices-vision-nspkg 3.0.1 zip}
Source29:       %{pypi_source azure-common 1.1.27 zip}
Source30:       %{pypi_source azure-communication-chat 1.0.0 zip}
Source31:       %{pypi_source azure-communication-identity 1.0.0 zip}
Source32:       %{pypi_source azure-communication-phonenumbers 1.0.0 zip}
Source33:       %{pypi_source azure-communication-sms 1.0.0 zip}
Source34:       %{pypi_source azure-core 1.14.0 zip}
Source35:       %{pypi_source azure-cosmos 3.2.0 tar.gz}
Source36:       %{pypi_source azure-cosmosdb-table 1.0.6 tar.gz}
Source37:       %{pypi_source azure-data-nspkg 1.0.0 zip}
Source38:       %{pypi_source azure-datalake-store 0.0.51 tar.gz}
Source39:       %{pypi_source azure-digitaltwins-core 1.1.0 zip}
Source40:       %{pypi_source azure-digitaltwins-nspkg 1.0.0 zip}
Source41:       %{pypi_source azure-eventgrid 4.2.0 zip}
Source42:       %{pypi_source azure-eventhub 5.5.0 zip}
Source43:       %{pypi_source azure-graphrbac 0.61.1 zip}
Source44:       %{pypi_source azure-identity 1.6.0 zip}
Source45:       %{pypi_source azure-iot-device 2.6.0 tar.gz}
Source46:       %{pypi_source azure-iot-hub 2.4.0 tar.gz}
Source47:       %{pypi_source azure-keyvault 4.1.0 zip}
Source48:       %{pypi_source azure-keyvault-certificates 4.2.1 zip}
Source49:       %{pypi_source azure-keyvault-keys 4.3.1 zip}
Source50:       %{pypi_source azure-keyvault-nspkg 1.0.0 zip}
Source51:       %{pypi_source azure-keyvault-secrets 4.2.0 zip}
Source52:       %{pypi_source azure-kusto-data 2.0.0 tar.gz}
Source53:       %{pypi_source azure-loganalytics 0.1.0 zip}
Source54:       %{pypi_source azure-mgmt-advisor 9.0.0 zip}
Source55:       %{pypi_source azure-mgmt-alertsmanagement 1.0.0 zip}
Source56:       %{pypi_source azure-mgmt-apimanagement 2.0.0 zip}
Source57:       %{pypi_source azure-mgmt-appconfiguration 1.0.1 zip}
Source58:       %{pypi_source azure-mgmt-applicationinsights 1.0.0 zip}
Source59:       %{pypi_source azure-mgmt-appplatform 6.0.0 zip}
Source60:       %{pypi_source azure-mgmt-attestation 1.0.0 zip}
Source61:       %{pypi_source azure-mgmt-authorization 1.0.0 zip}
Source62:       %{pypi_source azure-mgmt-automation 1.0.0 zip}
Source63:       %{pypi_source azure-mgmt-avs 1.0.0 zip}
Source64:       %{pypi_source azure-mgmt-azurestack 1.0.0 zip}
Source65:       %{pypi_source azure-mgmt-azurestackhci 6.0.0 zip}
Source66:       %{pypi_source azure-mgmt-batch 15.0.0 zip}
Source67:       %{pypi_source azure-mgmt-batchai 2.0.0 zip}
Source68:       %{pypi_source azure-mgmt-billing 6.0.0 zip}
Source69:       %{pypi_source azure-mgmt-botservice 1.0.0 zip}
Source70:       %{pypi_source azure-mgmt-cdn 11.0.0 zip}
Source71:       %{pypi_source azure-mgmt-cognitiveservices 11.0.0 zip}
Source72:       %{pypi_source azure-mgmt-commerce 6.0.0 zip}
Source73:       %{pypi_source azure-mgmt-common 0.20.0 zip}
Source74:       %{pypi_source azure-mgmt-communication 1.0.0 zip}
Source75:       %{pypi_source azure-mgmt-compute 21.0.0 zip}
Source76:       %{pypi_source azure-mgmt-confluent 1.0.0 zip}
Source77:       %{pypi_source azure-mgmt-consumption 8.0.0 zip}
Source78:       %{pypi_source azure-mgmt-containerinstance 7.0.0 zip}
Source79:       %{pypi_source azure-mgmt-containerregistry 8.0.0 zip}
Source80:       %{pypi_source azure-mgmt-containerservice 15.1.0 zip}
Source81:       %{pypi_source azure-mgmt-core 1.2.2 zip}
Source82:       %{pypi_source azure-mgmt-cosmosdb 6.3.0 zip}
Source83:       %{pypi_source azure-mgmt-costmanagement 1.0.0 zip}
Source84:       %{pypi_source azure-mgmt-customproviders 1.0.0 zip}
Source85:       %{pypi_source azure-mgmt-databox 1.0.0 zip}
Source86:       %{pypi_source azure-mgmt-databoxedge 1.0.0 zip}
Source87:       %{pypi_source azure-mgmt-databricks 1.0.0 zip}
Source88:       %{pypi_source azure-mgmt-datadog 2.0.0 zip}
Source89:       %{pypi_source azure-mgmt-datafactory 1.1.0 zip}
Source90:       %{pypi_source azure-mgmt-datalake-analytics 0.6.0 zip}
Source91:       %{pypi_source azure-mgmt-datalake-nspkg 3.0.1 zip}
Source92:       %{pypi_source azure-mgmt-datalake-store 0.5.0 zip}
Source93:       %{pypi_source azure-mgmt-datamigration 9.0.0 zip}
Source94:       %{pypi_source azure-mgmt-datashare 1.0.0 zip}
Source95:       %{pypi_source azure-mgmt-deploymentmanager 1.0.0 zip}
Source96:       %{pypi_source azure-mgmt-devspaces 0.2.0 zip}
Source97:       %{pypi_source azure-mgmt-devtestlabs 9.0.0 zip}
Source98:       %{pypi_source azure-mgmt-digitaltwins 6.0.0 zip}
Source99:       %{pypi_source azure-mgmt-dns 8.0.0 zip}
Source100:      %{pypi_source azure-mgmt-edgegateway 0.1.0 zip}
Source101:      %{pypi_source azure-mgmt-eventgrid 9.0.0 zip}
Source102:      %{pypi_source azure-mgmt-eventhub 9.0.0 zip}
Source103:      %{pypi_source azure-mgmt-frontdoor 1.0.0 zip}
Source104:      %{pypi_source azure-mgmt-hanaonazure 1.0.0 zip}
Source105:      %{pypi_source azure-mgmt-hdinsight 7.0.0 zip}
Source106:      %{pypi_source azure-mgmt-healthcareapis 1.0.0 zip}
Source107:      %{pypi_source azure-mgmt-hybridcompute 7.0.0 zip}
Source108:      %{pypi_source azure-mgmt-hybridkubernetes 1.0.0 zip}
Source109:      %{pypi_source azure-mgmt-imagebuilder 0.4.0 zip}
Source110:      %{pypi_source azure-mgmt-iotcentral 4.1.0 zip}
Source111:      %{pypi_source azure-mgmt-iothub 2.0.0 zip}
Source112:      %{pypi_source azure-mgmt-iothubprovisioningservices 0.2.0 zip}
Source113:      %{pypi_source azure-mgmt-keyvault 9.0.0 zip}
Source114:      %{pypi_source azure-mgmt-kusto 2.0.0 zip}
Source115:      %{pypi_source azure-mgmt-labservices 1.0.0 zip}
Source116:      %{pypi_source azure-mgmt-loganalytics 10.0.0 zip}
Source117:      %{pypi_source azure-mgmt-logic 9.0.0 zip}
Source118:      %{pypi_source azure-mgmt-machinelearningcompute 0.4.1 zip}
Source119:      %{pypi_source azure-mgmt-machinelearningservices 1.0.0 zip}
Source120:      %{pypi_source azure-mgmt-maintenance 2.0.0 zip}
Source121:      %{pypi_source azure-mgmt-managedservices 6.0.0 zip}
Source122:      %{pypi_source azure-mgmt-managementgroups 1.0.0 zip}
Source123:      %{pypi_source azure-mgmt-managementpartner 1.0.0 zip}
Source124:      %{pypi_source azure-mgmt-maps 2.0.0 zip}
Source125:      %{pypi_source azure-mgmt-marketplaceordering 1.1.0 zip}
Source126:      %{pypi_source azure-mgmt-media 3.1.0 zip}
Source127:      %{pypi_source azure-mgmt-mixedreality 1.0.0 zip}
Source128:      %{pypi_source azure-mgmt-monitor 2.0.0 zip}
Source129:      %{pypi_source azure-mgmt-msi 1.0.0 zip}
Source130:      %{pypi_source azure-mgmt-netapp 3.0.0 zip}
Source131:      %{pypi_source azure-mgmt-network 19.0.0 zip}
Source132:      %{pypi_source azure-mgmt-notificationhubs 7.0.0 zip}
Source133:      %{pypi_source azure-mgmt-nspkg 3.0.2 zip}
Source134:      %{pypi_source azure-mgmt-operationsmanagement 1.0.0 zip}
Source135:      %{pypi_source azure-mgmt-peering 1.0.0 zip}
Source136:      %{pypi_source azure-mgmt-policyinsights 1.0.0 zip}
Source137:      %{pypi_source azure-mgmt-powerbidedicated 1.0.0 zip}
Source138:      %{pypi_source azure-mgmt-powerbiembedded 2.0.0 zip}
Source139:      %{pypi_source azure-mgmt-privatedns 1.0.0 zip}
Source140:      %{pypi_source azure-mgmt-rdbms 8.0.0 zip}
Source141:      %{pypi_source azure-mgmt-recoveryservices 1.0.0 zip}
Source142:      %{pypi_source azure-mgmt-recoveryservicesbackup 0.12.0 zip}
Source143:      %{pypi_source azure-mgmt-redhatopenshift 1.0.0 zip}
Source144:      %{pypi_source azure-mgmt-redis 12.0.0 zip}
Source145:      %{pypi_source azure-mgmt-relay 1.0.0 zip}
Source146:      %{pypi_source azure-mgmt-reservations 1.0.0 zip}
Source147:      %{pypi_source azure-mgmt-resource 18.0.0 zip}
Source148:      %{pypi_source azure-mgmt-resourcegraph 8.0.0 zip}
Source149:      %{pypi_source azure-mgmt-resourcemover 1.0.0 zip}
Source150:      %{pypi_source azure-mgmt-scheduler 2.0.0 zip}
Source151:      %{pypi_source azure-mgmt-search 8.0.0 zip}
Source152:      %{pypi_source azure-mgmt-security 1.0.0 zip}
Source153:      %{pypi_source azure-mgmt-serialconsole 1.0.0 zip}
Source154:      %{pypi_source azure-mgmt-servermanager 2.0.0 zip}
Source155:      %{pypi_source azure-mgmt-servicebus 6.0.0 zip}
Source156:      %{pypi_source azure-mgmt-sql 2.1.0 zip}
Source157:      %{pypi_source azure-mgmt-sqlvirtualmachine 0.5.0 zip}
Source158:      %{pypi_source azure-mgmt-storage 18.0.0 zip}
Source159:      %{pypi_source azure-mgmt-storagecache 0.5.0 zip}
Source160:      %{pypi_source azure-mgmt-storageimportexport 0.1.0 zip}
Source161:      %{pypi_source azure-mgmt-storagesync 1.0.0 zip}
Source162:      %{pypi_source azure-mgmt-subscription 1.0.0 zip}
Source163:      %{pypi_source azure-mgmt-support 6.0.0 zip}
Source164:      %{pypi_source azure-mgmt-synapse 2.0.0 zip}
Source165:      %{pypi_source azure-mgmt-timeseriesinsights 1.0.0 zip}
Source166:      %{pypi_source azure-mgmt-trafficmanager 0.51.0 zip}
Source167:      %{pypi_source azure-mgmt-vmwarecloudsimple 0.2.0 zip}
Source168:      %{pypi_source azure-mgmt-web 3.0.0 zip}
Source169:      %{pypi_source azure-nspkg 3.0.2 zip}
Source170:      %{pypi_source azure-search-documents 11.1.0 zip}
Source171:      %{pypi_source azure-search-nspkg 1.0.0 zip}
Source172:      %{pypi_source azure-servicebus 7.2.0 zip}
Source173:      %{pypi_source azure-servicefabric 8.0.0.0 zip}
Source174:      %{pypi_source azure-storage-blob 2.1.0 tar.gz}
Source175:      %{pypi_source azure-storage-common 2.1.0 tar.gz}
Source176:      %{pypi_source azure-storage-file 2.1.0 tar.gz}
Source177:      %{pypi_source azure-storage-file-datalake 12.3.1 zip}
Source178:      %{pypi_source azure-storage-file-share 12.4.2 zip}
Source179:      %{pypi_source azure-storage-nspkg 3.1.0 tar.gz}
Source180:      %{pypi_source azure-storage-queue 2.1.0 tar.gz}
Source181:      %{pypi_source azure-synapse 0.1.1 zip}
Source182:      %{pypi_source azure-synapse-nspkg 1.0.0 zip}
Source183:      %{pypi_source azure-template 0.0.17 zip}


BuildArch:      noarch

Obsoletes:      python-azure-sdk == 5.0.0-4

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

%if %{with check}
# DOOT
%endif

%description
Azure SDK for Python


%package -n python%{python3_pkgversion}-azure-ai-textanalytics
Version: 5.0.0
Summary: Microsoft Azure Python SDK - Text Analytics

%description -n python%{python3_pkgversion}-azure-ai-textanalytics
Microsoft Azure Python SDK - Text Analytics

%package -n python%{python3_pkgversion}-azure-appconfiguration
Version: 1.1.1
Summary: Microsoft Azure Python SDK - App Configuration

%description -n python%{python3_pkgversion}-azure-appconfiguration
Microsoft Azure Python SDK - App Configuration

%package -n python%{python3_pkgversion}-azure-applicationinsights
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Application Insights

%description -n python%{python3_pkgversion}-azure-applicationinsights
Microsoft Azure Python SDK - Application Insights

%package -n python%{python3_pkgversion}-azure-batch
Version: 10.0.0
Summary: Microsoft Azure Python SDK - Batch

%description -n python%{python3_pkgversion}-azure-batch
Microsoft Azure Python SDK - Batch

%package -n python%{python3_pkgversion}-azure-cognitiveservices-anomalydetector
Version: 0.3.0
Summary: Microsoft Azure Python SDK - Anomaly Detector

%description -n python%{python3_pkgversion}-azure-cognitiveservices-anomalydetector
Microsoft Azure Python SDK - Anomaly Detector

%package -n python%{python3_pkgversion}-azure-cognitiveservices-formrecognizer
Version: 0.1.1
Summary: Microsoft Azure Python SDK - Form Recognizer

%description -n python%{python3_pkgversion}-azure-cognitiveservices-formrecognizer
Microsoft Azure Python SDK - Form Recognizer

%package -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-nspkg
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Cognitive Services Knowledge Namespace Package

%description -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-nspkg
Microsoft Azure Python SDK - Cognitive Services Knowledge Namespace Package

%package -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-qnamaker
Version: 0.3.0
Summary: Microsoft Azure Python SDK - QnA Maker

%description -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-qnamaker
Microsoft Azure Python SDK - QnA Maker

%package -n python%{python3_pkgversion}-azure-cognitiveservices-language-luis
Version: 0.7.0
Summary: Microsoft Azure Python SDK - LUIS

%description -n python%{python3_pkgversion}-azure-cognitiveservices-language-luis
Microsoft Azure Python SDK - LUIS

%package -n python%{python3_pkgversion}-azure-cognitiveservices-language-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Language Namespace Package

%description -n python%{python3_pkgversion}-azure-cognitiveservices-language-nspkg
Microsoft Azure Python SDK - Cognitive Services Language Namespace Package

%package -n python%{python3_pkgversion}-azure-cognitiveservices-language-spellcheck
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Spell Check

%description -n python%{python3_pkgversion}-azure-cognitiveservices-language-spellcheck
Microsoft Azure Python SDK - Spell Check

%package -n python%{python3_pkgversion}-azure-cognitiveservices-language-textanalytics
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Text Analytics

%description -n python%{python3_pkgversion}-azure-cognitiveservices-language-textanalytics
Microsoft Azure Python SDK - Text Analytics

%package -n python%{python3_pkgversion}-azure-cognitiveservices-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Namespace Package

%description -n python%{python3_pkgversion}-azure-cognitiveservices-nspkg
Microsoft Azure Python SDK - Cognitive Services Namespace Package

%package -n python%{python3_pkgversion}-azure-cognitiveservices-personalizer
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Personalizer

%description -n python%{python3_pkgversion}-azure-cognitiveservices-personalizer
Microsoft Azure Python SDK - Personalizer

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-autosuggest
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Autosuggest

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-autosuggest
Microsoft Azure Python SDK - Autosuggest

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-customimagesearch
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Custom Image Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-customimagesearch
Microsoft Azure Python SDK - Custom Image Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-customsearch
Version: 0.3.0
Summary: Microsoft Azure Python SDK - Custom Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-customsearch
Microsoft Azure Python SDK - Custom Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-entitysearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Entity Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-entitysearch
Microsoft Azure Python SDK - Entity Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-imagesearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Image Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-imagesearch
Microsoft Azure Python SDK - Image Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-newssearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - News Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-newssearch
Microsoft Azure Python SDK - News Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Search Namespace Package

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-nspkg
Microsoft Azure Python SDK - Cognitive Services Search Namespace Package

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-videosearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Video Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-videosearch
Microsoft Azure Python SDK - Video Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-visualsearch
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Visual Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-visualsearch
Microsoft Azure Python SDK - Visual Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-search-websearch
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Web Search

%description -n python%{python3_pkgversion}-azure-cognitiveservices-search-websearch
Microsoft Azure Python SDK - Web Search

%package -n python%{python3_pkgversion}-azure-cognitiveservices-vision-computervision
Version: 0.9.0
Summary: Microsoft Azure Python SDK - Computer Vision

%description -n python%{python3_pkgversion}-azure-cognitiveservices-vision-computervision
Microsoft Azure Python SDK - Computer Vision

%package -n python%{python3_pkgversion}-azure-cognitiveservices-vision-contentmoderator
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Content Moderator

%description -n python%{python3_pkgversion}-azure-cognitiveservices-vision-contentmoderator
Microsoft Azure Python SDK - Content Moderator

%package -n python%{python3_pkgversion}-azure-cognitiveservices-vision-customvision
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Custom Vision

%description -n python%{python3_pkgversion}-azure-cognitiveservices-vision-customvision
Microsoft Azure Python SDK - Custom Vision

%package -n python%{python3_pkgversion}-azure-cognitiveservices-vision-face
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Face

%description -n python%{python3_pkgversion}-azure-cognitiveservices-vision-face
Microsoft Azure Python SDK - Face

%package -n python%{python3_pkgversion}-azure-cognitiveservices-vision-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Cognitive Services Vision Namespace Package

%description -n python%{python3_pkgversion}-azure-cognitiveservices-vision-nspkg
Microsoft Azure Python SDK - Cognitive Services Vision Namespace Package

%package -n python%{python3_pkgversion}-azure-common
Version: 1.1.27
Summary: Microsoft Azure Python SDK - Common

%description -n python%{python3_pkgversion}-azure-common
Microsoft Azure Python SDK - Common

%package -n python%{python3_pkgversion}-azure-communication-chat
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Chat

%description -n python%{python3_pkgversion}-azure-communication-chat
Microsoft Azure Python SDK - Communication Chat

%package -n python%{python3_pkgversion}-azure-communication-identity
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Identity

%description -n python%{python3_pkgversion}-azure-communication-identity
Microsoft Azure Python SDK - Communication Identity

%package -n python%{python3_pkgversion}-azure-communication-phonenumbers
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Phone Numbers

%description -n python%{python3_pkgversion}-azure-communication-phonenumbers
Microsoft Azure Python SDK - Communication Phone Numbers

%package -n python%{python3_pkgversion}-azure-communication-sms
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Communication Sms

%description -n python%{python3_pkgversion}-azure-communication-sms
Microsoft Azure Python SDK - Communication Sms

%package -n python%{python3_pkgversion}-azure-core
Version: 1.14.0
Summary: Microsoft Azure Python SDK - Core

%description -n python%{python3_pkgversion}-azure-core
Microsoft Azure Python SDK - Core

%package -n python%{python3_pkgversion}-azure-cosmos
Version: 3.2.0
Summary: Microsoft Azure Python SDK - Cosmos DB

%description -n python%{python3_pkgversion}-azure-cosmos
Microsoft Azure Python SDK - Cosmos DB

%package -n python%{python3_pkgversion}-azure-cosmosdb-table
Version: 1.0.6
Summary: Microsoft Azure Python SDK - Tables

%description -n python%{python3_pkgversion}-azure-cosmosdb-table
Microsoft Azure Python SDK - Tables

%package -n python%{python3_pkgversion}-azure-data-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Data Namespace Package

%description -n python%{python3_pkgversion}-azure-data-nspkg
Microsoft Azure Python SDK - Data Namespace Package

%package -n python%{python3_pkgversion}-azure-datalake-store
Version: 0.0.51
Summary: Microsoft Azure Python SDK - Data Lake Storage

%description -n python%{python3_pkgversion}-azure-datalake-store
Microsoft Azure Python SDK - Data Lake Storage

%package -n python%{python3_pkgversion}-azure-digitaltwins-core
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Digital Twins - Core

%description -n python%{python3_pkgversion}-azure-digitaltwins-core
Microsoft Azure Python SDK - Digital Twins - Core

%package -n python%{python3_pkgversion}-azure-digitaltwins-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Digital Twins Namespace Package

%description -n python%{python3_pkgversion}-azure-digitaltwins-nspkg
Microsoft Azure Python SDK - Digital Twins Namespace Package

%package -n python%{python3_pkgversion}-azure-eventgrid
Version: 4.2.0
Summary: Microsoft Azure Python SDK - Event Grid

%description -n python%{python3_pkgversion}-azure-eventgrid
Microsoft Azure Python SDK - Event Grid

%package -n python%{python3_pkgversion}-azure-eventhub
Version: 5.5.0
Summary: Microsoft Azure Python SDK - Event Hubs

%description -n python%{python3_pkgversion}-azure-eventhub
Microsoft Azure Python SDK - Event Hubs

%package -n python%{python3_pkgversion}-azure-graphrbac
Version: 0.61.1
Summary: Microsoft Azure Python SDK - Graph RBAC

%description -n python%{python3_pkgversion}-azure-graphrbac
Microsoft Azure Python SDK - Graph RBAC

%package -n python%{python3_pkgversion}-azure-identity
Version: 1.6.0
Summary: Microsoft Azure Python SDK - Identity

%description -n python%{python3_pkgversion}-azure-identity
Microsoft Azure Python SDK - Identity

%package -n python%{python3_pkgversion}-azure-iot-device
Version: 2.6.0
Summary: Microsoft Azure Python SDK - IoT Device

%description -n python%{python3_pkgversion}-azure-iot-device
Microsoft Azure Python SDK - IoT Device

%package -n python%{python3_pkgversion}-azure-iot-hub
Version: 2.4.0
Summary: Microsoft Azure Python SDK - IoT Hub

%description -n python%{python3_pkgversion}-azure-iot-hub
Microsoft Azure Python SDK - IoT Hub

%package -n python%{python3_pkgversion}-azure-keyvault
Version: 4.1.0
Summary: Microsoft Azure Python SDK - Key Vault

%description -n python%{python3_pkgversion}-azure-keyvault
Microsoft Azure Python SDK - Key Vault

%package -n python%{python3_pkgversion}-azure-keyvault-certificates
Version: 4.2.1
Summary: Microsoft Azure Python SDK - Key Vault - Certificates

%description -n python%{python3_pkgversion}-azure-keyvault-certificates
Microsoft Azure Python SDK - Key Vault - Certificates

%package -n python%{python3_pkgversion}-azure-keyvault-keys
Version: 4.3.1
Summary: Microsoft Azure Python SDK - Key Vault - Keys

%description -n python%{python3_pkgversion}-azure-keyvault-keys
Microsoft Azure Python SDK - Key Vault - Keys

%package -n python%{python3_pkgversion}-azure-keyvault-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Key Vault Namespace Package

%description -n python%{python3_pkgversion}-azure-keyvault-nspkg
Microsoft Azure Python SDK - Key Vault Namespace Package

%package -n python%{python3_pkgversion}-azure-keyvault-secrets
Version: 4.2.0
Summary: Microsoft Azure Python SDK - Key Vault - Secrets

%description -n python%{python3_pkgversion}-azure-keyvault-secrets
Microsoft Azure Python SDK - Key Vault - Secrets

%package -n python%{python3_pkgversion}-azure-kusto-data
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Kusto Data

%description -n python%{python3_pkgversion}-azure-kusto-data
Microsoft Azure Python SDK - Kusto Data

%package -n python%{python3_pkgversion}-azure-loganalytics
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Log Analytics

%description -n python%{python3_pkgversion}-azure-loganalytics
Microsoft Azure Python SDK - Log Analytics

%package -n python%{python3_pkgversion}-azure-mgmt-advisor
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Advisor

%description -n python%{python3_pkgversion}-azure-mgmt-advisor
Microsoft Azure Python SDK - Resource Management - Advisor

%package -n python%{python3_pkgversion}-azure-mgmt-alertsmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Alerts Management

%description -n python%{python3_pkgversion}-azure-mgmt-alertsmanagement
Microsoft Azure Python SDK - Resource Management - Alerts Management

%package -n python%{python3_pkgversion}-azure-mgmt-apimanagement
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - API Management

%description -n python%{python3_pkgversion}-azure-mgmt-apimanagement
Microsoft Azure Python SDK - Resource Management - API Management

%package -n python%{python3_pkgversion}-azure-mgmt-appconfiguration
Version: 1.0.1
Summary: Microsoft Azure Python SDK - Resource Management - App Configuration

%description -n python%{python3_pkgversion}-azure-mgmt-appconfiguration
Microsoft Azure Python SDK - Resource Management - App Configuration

%package -n python%{python3_pkgversion}-azure-mgmt-applicationinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Application Insights

%description -n python%{python3_pkgversion}-azure-mgmt-applicationinsights
Microsoft Azure Python SDK - Resource Management - Application Insights

%package -n python%{python3_pkgversion}-azure-mgmt-appplatform
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - App Platform

%description -n python%{python3_pkgversion}-azure-mgmt-appplatform
Microsoft Azure Python SDK - Resource Management - App Platform

%package -n python%{python3_pkgversion}-azure-mgmt-attestation
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Attestation

%description -n python%{python3_pkgversion}-azure-mgmt-attestation
Microsoft Azure Python SDK - Resource Management - Attestation

%package -n python%{python3_pkgversion}-azure-mgmt-authorization
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Authorization

%description -n python%{python3_pkgversion}-azure-mgmt-authorization
Microsoft Azure Python SDK - Resource Management - Authorization

%package -n python%{python3_pkgversion}-azure-mgmt-automation
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Automation

%description -n python%{python3_pkgversion}-azure-mgmt-automation
Microsoft Azure Python SDK - Resource Management - Automation

%package -n python%{python3_pkgversion}-azure-mgmt-avs
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure VMware Solution

%description -n python%{python3_pkgversion}-azure-mgmt-avs
Microsoft Azure Python SDK - Resource Management - Azure VMware Solution

%package -n python%{python3_pkgversion}-azure-mgmt-azurestack
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure Stack

%description -n python%{python3_pkgversion}-azure-mgmt-azurestack
Microsoft Azure Python SDK - Resource Management - Azure Stack

%package -n python%{python3_pkgversion}-azure-mgmt-azurestackhci
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Azure Stack HCI

%description -n python%{python3_pkgversion}-azure-mgmt-azurestackhci
Microsoft Azure Python SDK - Resource Management - Azure Stack HCI

%package -n python%{python3_pkgversion}-azure-mgmt-batch
Version: 15.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Batch

%description -n python%{python3_pkgversion}-azure-mgmt-batch
Microsoft Azure Python SDK - Resource Management - Batch

%package -n python%{python3_pkgversion}-azure-mgmt-batchai
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Batch AI

%description -n python%{python3_pkgversion}-azure-mgmt-batchai
Microsoft Azure Python SDK - Resource Management - Batch AI

%package -n python%{python3_pkgversion}-azure-mgmt-billing
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Billing

%description -n python%{python3_pkgversion}-azure-mgmt-billing
Microsoft Azure Python SDK - Resource Management - Billing

%package -n python%{python3_pkgversion}-azure-mgmt-botservice
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Bot Service

%description -n python%{python3_pkgversion}-azure-mgmt-botservice
Microsoft Azure Python SDK - Resource Management - Bot Service

%package -n python%{python3_pkgversion}-azure-mgmt-cdn
Version: 11.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Content Delivery Network

%description -n python%{python3_pkgversion}-azure-mgmt-cdn
Microsoft Azure Python SDK - Resource Management - Content Delivery Network

%package -n python%{python3_pkgversion}-azure-mgmt-cognitiveservices
Version: 11.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Cognitive Services

%description -n python%{python3_pkgversion}-azure-mgmt-cognitiveservices
Microsoft Azure Python SDK - Resource Management - Cognitive Services

%package -n python%{python3_pkgversion}-azure-mgmt-commerce
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Commerce

%description -n python%{python3_pkgversion}-azure-mgmt-commerce
Microsoft Azure Python SDK - Resource Management - Commerce

%package -n python%{python3_pkgversion}-azure-mgmt-common
Version: 0.20.0
Summary: Microsoft Azure Python SDK - Resource Management - Common

%description -n python%{python3_pkgversion}-azure-mgmt-common
Microsoft Azure Python SDK - Resource Management - Common

%package -n python%{python3_pkgversion}-azure-mgmt-communication
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Communication

%description -n python%{python3_pkgversion}-azure-mgmt-communication
Microsoft Azure Python SDK - Resource Management - Communication

%package -n python%{python3_pkgversion}-azure-mgmt-compute
Version: 21.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Compute

%description -n python%{python3_pkgversion}-azure-mgmt-compute
Microsoft Azure Python SDK - Resource Management - Compute

%package -n python%{python3_pkgversion}-azure-mgmt-confluent
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Confluent

%description -n python%{python3_pkgversion}-azure-mgmt-confluent
Microsoft Azure Python SDK - Resource Management - Confluent

%package -n python%{python3_pkgversion}-azure-mgmt-consumption
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Consumption

%description -n python%{python3_pkgversion}-azure-mgmt-consumption
Microsoft Azure Python SDK - Resource Management - Consumption

%package -n python%{python3_pkgversion}-azure-mgmt-containerinstance
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Instances

%description -n python%{python3_pkgversion}-azure-mgmt-containerinstance
Microsoft Azure Python SDK - Resource Management - Container Instances

%package -n python%{python3_pkgversion}-azure-mgmt-containerregistry
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Registry

%description -n python%{python3_pkgversion}-azure-mgmt-containerregistry
Microsoft Azure Python SDK - Resource Management - Container Registry

%package -n python%{python3_pkgversion}-azure-mgmt-containerservice
Version: 15.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Container Service

%description -n python%{python3_pkgversion}-azure-mgmt-containerservice
Microsoft Azure Python SDK - Resource Management - Container Service

%package -n python%{python3_pkgversion}-azure-mgmt-core
Version: 1.2.2
Summary: Microsoft Azure Python SDK - Resource Management - Core

%description -n python%{python3_pkgversion}-azure-mgmt-core
Microsoft Azure Python SDK - Resource Management - Core

%package -n python%{python3_pkgversion}-azure-mgmt-cosmosdb
Version: 6.3.0
Summary: Microsoft Azure Python SDK - Resource Management - Cosmos DB

%description -n python%{python3_pkgversion}-azure-mgmt-cosmosdb
Microsoft Azure Python SDK - Resource Management - Cosmos DB

%package -n python%{python3_pkgversion}-azure-mgmt-costmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Cost Management

%description -n python%{python3_pkgversion}-azure-mgmt-costmanagement
Microsoft Azure Python SDK - Resource Management - Cost Management

%package -n python%{python3_pkgversion}-azure-mgmt-customproviders
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Custom Providers

%description -n python%{python3_pkgversion}-azure-mgmt-customproviders
Microsoft Azure Python SDK - Resource Management - Custom Providers

%package -n python%{python3_pkgversion}-azure-mgmt-databox
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Box

%description -n python%{python3_pkgversion}-azure-mgmt-databox
Microsoft Azure Python SDK - Resource Management - Data Box

%package -n python%{python3_pkgversion}-azure-mgmt-databoxedge
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Box Edge

%description -n python%{python3_pkgversion}-azure-mgmt-databoxedge
Microsoft Azure Python SDK - Resource Management - Data Box Edge

%package -n python%{python3_pkgversion}-azure-mgmt-databricks
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Databricks

%description -n python%{python3_pkgversion}-azure-mgmt-databricks
Microsoft Azure Python SDK - Resource Management - Databricks

%package -n python%{python3_pkgversion}-azure-mgmt-datadog
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Datadog

%description -n python%{python3_pkgversion}-azure-mgmt-datadog
Microsoft Azure Python SDK - Resource Management - Datadog

%package -n python%{python3_pkgversion}-azure-mgmt-datafactory
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Factory

%description -n python%{python3_pkgversion}-azure-mgmt-datafactory
Microsoft Azure Python SDK - Resource Management - Data Factory

%package -n python%{python3_pkgversion}-azure-mgmt-datalake-analytics
Version: 0.6.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Analytics

%description -n python%{python3_pkgversion}-azure-mgmt-datalake-analytics
Microsoft Azure Python SDK - Resource Management - Data Lake Analytics

%package -n python%{python3_pkgversion}-azure-mgmt-datalake-nspkg
Version: 3.0.1
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Namespace Package

%description -n python%{python3_pkgversion}-azure-mgmt-datalake-nspkg
Microsoft Azure Python SDK - Resource Management - Data Lake Namespace Package

%package -n python%{python3_pkgversion}-azure-mgmt-datalake-store
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Lake Storage

%description -n python%{python3_pkgversion}-azure-mgmt-datalake-store
Microsoft Azure Python SDK - Resource Management - Data Lake Storage

%package -n python%{python3_pkgversion}-azure-mgmt-datamigration
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Migration

%description -n python%{python3_pkgversion}-azure-mgmt-datamigration
Microsoft Azure Python SDK - Resource Management - Data Migration

%package -n python%{python3_pkgversion}-azure-mgmt-datashare
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Data Share

%description -n python%{python3_pkgversion}-azure-mgmt-datashare
Microsoft Azure Python SDK - Resource Management - Data Share

%package -n python%{python3_pkgversion}-azure-mgmt-deploymentmanager
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Deployment Manager

%description -n python%{python3_pkgversion}-azure-mgmt-deploymentmanager
Microsoft Azure Python SDK - Resource Management - Deployment Manager

%package -n python%{python3_pkgversion}-azure-mgmt-devspaces
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - Dev Spaces

%description -n python%{python3_pkgversion}-azure-mgmt-devspaces
Microsoft Azure Python SDK - Resource Management - Dev Spaces

%package -n python%{python3_pkgversion}-azure-mgmt-devtestlabs
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DevTest Labs

%description -n python%{python3_pkgversion}-azure-mgmt-devtestlabs
Microsoft Azure Python SDK - Resource Management - DevTest Labs

%package -n python%{python3_pkgversion}-azure-mgmt-digitaltwins
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Digital Twins

%description -n python%{python3_pkgversion}-azure-mgmt-digitaltwins
Microsoft Azure Python SDK - Resource Management - Digital Twins

%package -n python%{python3_pkgversion}-azure-mgmt-dns
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - DNS

%description -n python%{python3_pkgversion}-azure-mgmt-dns
Microsoft Azure Python SDK - Resource Management - DNS

%package -n python%{python3_pkgversion}-azure-mgmt-edgegateway
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Edge Gateway

%description -n python%{python3_pkgversion}-azure-mgmt-edgegateway
Microsoft Azure Python SDK - Resource Management - Edge Gateway

%package -n python%{python3_pkgversion}-azure-mgmt-eventgrid
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Event Grid

%description -n python%{python3_pkgversion}-azure-mgmt-eventgrid
Microsoft Azure Python SDK - Resource Management - Event Grid

%package -n python%{python3_pkgversion}-azure-mgmt-eventhub
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Event Hubs

%description -n python%{python3_pkgversion}-azure-mgmt-eventhub
Microsoft Azure Python SDK - Resource Management - Event Hubs

%package -n python%{python3_pkgversion}-azure-mgmt-frontdoor
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Frontdoor

%description -n python%{python3_pkgversion}-azure-mgmt-frontdoor
Microsoft Azure Python SDK - Resource Management - Frontdoor

%package -n python%{python3_pkgversion}-azure-mgmt-hanaonazure
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - HANA on Azure

%description -n python%{python3_pkgversion}-azure-mgmt-hanaonazure
Microsoft Azure Python SDK - Resource Management - HANA on Azure

%package -n python%{python3_pkgversion}-azure-mgmt-hdinsight
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - HDInsight

%description -n python%{python3_pkgversion}-azure-mgmt-hdinsight
Microsoft Azure Python SDK - Resource Management - HDInsight

%package -n python%{python3_pkgversion}-azure-mgmt-healthcareapis
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Healthcare APIs

%description -n python%{python3_pkgversion}-azure-mgmt-healthcareapis
Microsoft Azure Python SDK - Resource Management - Healthcare APIs

%package -n python%{python3_pkgversion}-azure-mgmt-hybridcompute
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Hybrid Compute

%description -n python%{python3_pkgversion}-azure-mgmt-hybridcompute
Microsoft Azure Python SDK - Resource Management - Hybrid Compute

%package -n python%{python3_pkgversion}-azure-mgmt-hybridkubernetes
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Hybrid Kubernetes

%description -n python%{python3_pkgversion}-azure-mgmt-hybridkubernetes
Microsoft Azure Python SDK - Resource Management - Hybrid Kubernetes

%package -n python%{python3_pkgversion}-azure-mgmt-imagebuilder
Version: 0.4.0
Summary: Microsoft Azure Python SDK - Resource Management - Image Builder

%description -n python%{python3_pkgversion}-azure-mgmt-imagebuilder
Microsoft Azure Python SDK - Resource Management - Image Builder

%package -n python%{python3_pkgversion}-azure-mgmt-iotcentral
Version: 4.1.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Central

%description -n python%{python3_pkgversion}-azure-mgmt-iotcentral
Microsoft Azure Python SDK - Resource Management - IoT Central

%package -n python%{python3_pkgversion}-azure-mgmt-iothub
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Hub

%description -n python%{python3_pkgversion}-azure-mgmt-iothub
Microsoft Azure Python SDK - Resource Management - IoT Hub

%package -n python%{python3_pkgversion}-azure-mgmt-iothubprovisioningservices
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - IoT Hub Provisioning Services

%description -n python%{python3_pkgversion}-azure-mgmt-iothubprovisioningservices
Microsoft Azure Python SDK - Resource Management - IoT Hub Provisioning Services

%package -n python%{python3_pkgversion}-azure-mgmt-keyvault
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - KeyVault

%description -n python%{python3_pkgversion}-azure-mgmt-keyvault
Microsoft Azure Python SDK - Resource Management - KeyVault

%package -n python%{python3_pkgversion}-azure-mgmt-kusto
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Kusto

%description -n python%{python3_pkgversion}-azure-mgmt-kusto
Microsoft Azure Python SDK - Resource Management - Kusto

%package -n python%{python3_pkgversion}-azure-mgmt-labservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Lab Services

%description -n python%{python3_pkgversion}-azure-mgmt-labservices
Microsoft Azure Python SDK - Resource Management - Lab Services

%package -n python%{python3_pkgversion}-azure-mgmt-loganalytics
Version: 10.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Log Analytics

%description -n python%{python3_pkgversion}-azure-mgmt-loganalytics
Microsoft Azure Python SDK - Resource Management - Log Analytics

%package -n python%{python3_pkgversion}-azure-mgmt-logic
Version: 9.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Logic Apps

%description -n python%{python3_pkgversion}-azure-mgmt-logic
Microsoft Azure Python SDK - Resource Management - Logic Apps

%package -n python%{python3_pkgversion}-azure-mgmt-machinelearningcompute
Version: 0.4.1
Summary: Microsoft Azure Python SDK - Resource Management - Machine Learning Compute

%description -n python%{python3_pkgversion}-azure-mgmt-machinelearningcompute
Microsoft Azure Python SDK - Resource Management - Machine Learning Compute

%package -n python%{python3_pkgversion}-azure-mgmt-machinelearningservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Machine Learning Services

%description -n python%{python3_pkgversion}-azure-mgmt-machinelearningservices
Microsoft Azure Python SDK - Resource Management - Machine Learning Services

%package -n python%{python3_pkgversion}-azure-mgmt-maintenance
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Maintenance

%description -n python%{python3_pkgversion}-azure-mgmt-maintenance
Microsoft Azure Python SDK - Resource Management - Maintenance

%package -n python%{python3_pkgversion}-azure-mgmt-managedservices
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Managed Services

%description -n python%{python3_pkgversion}-azure-mgmt-managedservices
Microsoft Azure Python SDK - Resource Management - Managed Services

%package -n python%{python3_pkgversion}-azure-mgmt-managementgroups
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Management Groups

%description -n python%{python3_pkgversion}-azure-mgmt-managementgroups
Microsoft Azure Python SDK - Resource Management - Management Groups

%package -n python%{python3_pkgversion}-azure-mgmt-managementpartner
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Management Partner

%description -n python%{python3_pkgversion}-azure-mgmt-managementpartner
Microsoft Azure Python SDK - Resource Management - Management Partner

%package -n python%{python3_pkgversion}-azure-mgmt-maps
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Maps

%description -n python%{python3_pkgversion}-azure-mgmt-maps
Microsoft Azure Python SDK - Resource Management - Maps

%package -n python%{python3_pkgversion}-azure-mgmt-marketplaceordering
Version: 1.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Marketplace Ordering

%description -n python%{python3_pkgversion}-azure-mgmt-marketplaceordering
Microsoft Azure Python SDK - Resource Management - Marketplace Ordering

%package -n python%{python3_pkgversion}-azure-mgmt-media
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Media Services

%description -n python%{python3_pkgversion}-azure-mgmt-media
Microsoft Azure Python SDK - Resource Management - Media Services

%package -n python%{python3_pkgversion}-azure-mgmt-mixedreality
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Mixed Reality

%description -n python%{python3_pkgversion}-azure-mgmt-mixedreality
Microsoft Azure Python SDK - Resource Management - Mixed Reality

%package -n python%{python3_pkgversion}-azure-mgmt-monitor
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Monitor

%description -n python%{python3_pkgversion}-azure-mgmt-monitor
Microsoft Azure Python SDK - Resource Management - Monitor

%package -n python%{python3_pkgversion}-azure-mgmt-msi
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Managed Service Identity

%description -n python%{python3_pkgversion}-azure-mgmt-msi
Microsoft Azure Python SDK - Resource Management - Managed Service Identity

%package -n python%{python3_pkgversion}-azure-mgmt-netapp
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Resource Management - NetApp

%description -n python%{python3_pkgversion}-azure-mgmt-netapp
Microsoft Azure Python SDK - Resource Management - NetApp

%package -n python%{python3_pkgversion}-azure-mgmt-network
Version: 19.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Network

%description -n python%{python3_pkgversion}-azure-mgmt-network
Microsoft Azure Python SDK - Resource Management - Network

%package -n python%{python3_pkgversion}-azure-mgmt-notificationhubs
Version: 7.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Notification Hubs

%description -n python%{python3_pkgversion}-azure-mgmt-notificationhubs
Microsoft Azure Python SDK - Resource Management - Notification Hubs

%package -n python%{python3_pkgversion}-azure-mgmt-nspkg
Version: 3.0.2
Summary: Microsoft Azure Python SDK - Resource Management - Namespace Package

%description -n python%{python3_pkgversion}-azure-mgmt-nspkg
Microsoft Azure Python SDK - Resource Management - Namespace Package

%package -n python%{python3_pkgversion}-azure-mgmt-operationsmanagement
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Operations Management

%description -n python%{python3_pkgversion}-azure-mgmt-operationsmanagement
Microsoft Azure Python SDK - Resource Management - Operations Management

%package -n python%{python3_pkgversion}-azure-mgmt-peering
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Peering

%description -n python%{python3_pkgversion}-azure-mgmt-peering
Microsoft Azure Python SDK - Resource Management - Peering

%package -n python%{python3_pkgversion}-azure-mgmt-policyinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Policy Insights

%description -n python%{python3_pkgversion}-azure-mgmt-policyinsights
Microsoft Azure Python SDK - Resource Management - Policy Insights

%package -n python%{python3_pkgversion}-azure-mgmt-powerbidedicated
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Power BI Dedicated

%description -n python%{python3_pkgversion}-azure-mgmt-powerbidedicated
Microsoft Azure Python SDK - Resource Management - Power BI Dedicated

%package -n python%{python3_pkgversion}-azure-mgmt-powerbiembedded
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Power BI Embedded

%description -n python%{python3_pkgversion}-azure-mgmt-powerbiembedded
Microsoft Azure Python SDK - Resource Management - Power BI Embedded

%package -n python%{python3_pkgversion}-azure-mgmt-privatedns
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Private DNS

%description -n python%{python3_pkgversion}-azure-mgmt-privatedns
Microsoft Azure Python SDK - Resource Management - Private DNS

%package -n python%{python3_pkgversion}-azure-mgmt-rdbms
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Rdbms

%description -n python%{python3_pkgversion}-azure-mgmt-rdbms
Microsoft Azure Python SDK - Resource Management - Rdbms

%package -n python%{python3_pkgversion}-azure-mgmt-recoveryservices
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Recovery Services

%description -n python%{python3_pkgversion}-azure-mgmt-recoveryservices
Microsoft Azure Python SDK - Resource Management - Recovery Services

%package -n python%{python3_pkgversion}-azure-mgmt-recoveryservicesbackup
Version: 0.12.0
Summary: Microsoft Azure Python SDK - Resource Management - Recovery Services Backup

%description -n python%{python3_pkgversion}-azure-mgmt-recoveryservicesbackup
Microsoft Azure Python SDK - Resource Management - Recovery Services Backup

%package -n python%{python3_pkgversion}-azure-mgmt-redhatopenshift
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Red Hat OpenShift

%description -n python%{python3_pkgversion}-azure-mgmt-redhatopenshift
Microsoft Azure Python SDK - Resource Management - Red Hat OpenShift

%package -n python%{python3_pkgversion}-azure-mgmt-redis
Version: 12.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Redis

%description -n python%{python3_pkgversion}-azure-mgmt-redis
Microsoft Azure Python SDK - Resource Management - Redis

%package -n python%{python3_pkgversion}-azure-mgmt-relay
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Relay

%description -n python%{python3_pkgversion}-azure-mgmt-relay
Microsoft Azure Python SDK - Resource Management - Relay

%package -n python%{python3_pkgversion}-azure-mgmt-reservations
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Reservations

%description -n python%{python3_pkgversion}-azure-mgmt-reservations
Microsoft Azure Python SDK - Resource Management - Reservations

%package -n python%{python3_pkgversion}-azure-mgmt-resource
Version: 18.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resources

%description -n python%{python3_pkgversion}-azure-mgmt-resource
Microsoft Azure Python SDK - Resource Management - Resources

%package -n python%{python3_pkgversion}-azure-mgmt-resourcegraph
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resource Graph

%description -n python%{python3_pkgversion}-azure-mgmt-resourcegraph
Microsoft Azure Python SDK - Resource Management - Resource Graph

%package -n python%{python3_pkgversion}-azure-mgmt-resourcemover
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Resource Mover

%description -n python%{python3_pkgversion}-azure-mgmt-resourcemover
Microsoft Azure Python SDK - Resource Management - Resource Mover

%package -n python%{python3_pkgversion}-azure-mgmt-scheduler
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Scheduler

%description -n python%{python3_pkgversion}-azure-mgmt-scheduler
Microsoft Azure Python SDK - Resource Management - Scheduler

%package -n python%{python3_pkgversion}-azure-mgmt-search
Version: 8.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Search

%description -n python%{python3_pkgversion}-azure-mgmt-search
Microsoft Azure Python SDK - Resource Management - Search

%package -n python%{python3_pkgversion}-azure-mgmt-security
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Security

%description -n python%{python3_pkgversion}-azure-mgmt-security
Microsoft Azure Python SDK - Resource Management - Security

%package -n python%{python3_pkgversion}-azure-mgmt-serialconsole
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Serial Console

%description -n python%{python3_pkgversion}-azure-mgmt-serialconsole
Microsoft Azure Python SDK - Resource Management - Serial Console

%package -n python%{python3_pkgversion}-azure-mgmt-servermanager
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Server Manager

%description -n python%{python3_pkgversion}-azure-mgmt-servermanager
Microsoft Azure Python SDK - Resource Management - Server Manager

%package -n python%{python3_pkgversion}-azure-mgmt-servicebus
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Service Bus

%description -n python%{python3_pkgversion}-azure-mgmt-servicebus
Microsoft Azure Python SDK - Resource Management - Service Bus

%package -n python%{python3_pkgversion}-azure-mgmt-sql
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Resource Management - SQL

%description -n python%{python3_pkgversion}-azure-mgmt-sql
Microsoft Azure Python SDK - Resource Management - SQL

%package -n python%{python3_pkgversion}-azure-mgmt-sqlvirtualmachine
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine

%description -n python%{python3_pkgversion}-azure-mgmt-sqlvirtualmachine
Microsoft Azure Python SDK - Resource Management - SQL Virtual Machine

%package -n python%{python3_pkgversion}-azure-mgmt-storage
Version: 18.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage

%description -n python%{python3_pkgversion}-azure-mgmt-storage
Microsoft Azure Python SDK - Resource Management - Storage

%package -n python%{python3_pkgversion}-azure-mgmt-storagecache
Version: 0.5.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Cache

%description -n python%{python3_pkgversion}-azure-mgmt-storagecache
Microsoft Azure Python SDK - Resource Management - Storage Cache

%package -n python%{python3_pkgversion}-azure-mgmt-storageimportexport
Version: 0.1.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Import Export

%description -n python%{python3_pkgversion}-azure-mgmt-storageimportexport
Microsoft Azure Python SDK - Resource Management - Storage Import Export

%package -n python%{python3_pkgversion}-azure-mgmt-storagesync
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Storage Sync

%description -n python%{python3_pkgversion}-azure-mgmt-storagesync
Microsoft Azure Python SDK - Resource Management - Storage Sync

%package -n python%{python3_pkgversion}-azure-mgmt-subscription
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Subscription

%description -n python%{python3_pkgversion}-azure-mgmt-subscription
Microsoft Azure Python SDK - Resource Management - Subscription

%package -n python%{python3_pkgversion}-azure-mgmt-support
Version: 6.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Support

%description -n python%{python3_pkgversion}-azure-mgmt-support
Microsoft Azure Python SDK - Resource Management - Support

%package -n python%{python3_pkgversion}-azure-mgmt-synapse
Version: 2.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Synapse

%description -n python%{python3_pkgversion}-azure-mgmt-synapse
Microsoft Azure Python SDK - Resource Management - Synapse

%package -n python%{python3_pkgversion}-azure-mgmt-timeseriesinsights
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Time Series Insights

%description -n python%{python3_pkgversion}-azure-mgmt-timeseriesinsights
Microsoft Azure Python SDK - Resource Management - Time Series Insights

%package -n python%{python3_pkgversion}-azure-mgmt-trafficmanager
Version: 0.51.0
Summary: Microsoft Azure Python SDK - Resource Management - Traffic Manager

%description -n python%{python3_pkgversion}-azure-mgmt-trafficmanager
Microsoft Azure Python SDK - Resource Management - Traffic Manager

%package -n python%{python3_pkgversion}-azure-mgmt-vmwarecloudsimple
Version: 0.2.0
Summary: Microsoft Azure Python SDK - Resource Management - VM Ware Cloud Simple

%description -n python%{python3_pkgversion}-azure-mgmt-vmwarecloudsimple
Microsoft Azure Python SDK - Resource Management - VM Ware Cloud Simple

%package -n python%{python3_pkgversion}-azure-mgmt-web
Version: 3.0.0
Summary: Microsoft Azure Python SDK - Resource Management - Web

%description -n python%{python3_pkgversion}-azure-mgmt-web
Microsoft Azure Python SDK - Resource Management - Web

%package -n python%{python3_pkgversion}-azure-nspkg
Version: 3.0.2
Summary: Microsoft Azure Python SDK - Core Namespace Package

%description -n python%{python3_pkgversion}-azure-nspkg
Microsoft Azure Python SDK - Core Namespace Package

%package -n python%{python3_pkgversion}-azure-search-documents
Version: 11.1.0
Summary: Microsoft Azure Python SDK - Cognitive Search

%description -n python%{python3_pkgversion}-azure-search-documents
Microsoft Azure Python SDK - Cognitive Search

%package -n python%{python3_pkgversion}-azure-search-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Search Namespace Package

%description -n python%{python3_pkgversion}-azure-search-nspkg
Microsoft Azure Python SDK - Search Namespace Package

%package -n python%{python3_pkgversion}-azure-servicebus
Version: 7.2.0
Summary: Microsoft Azure Python SDK - Service Bus

%description -n python%{python3_pkgversion}-azure-servicebus
Microsoft Azure Python SDK - Service Bus

%package -n python%{python3_pkgversion}-azure-servicefabric
Version: 8.0.0.0
Summary: Microsoft Azure Python SDK - Service Fabric

%description -n python%{python3_pkgversion}-azure-servicefabric
Microsoft Azure Python SDK - Service Fabric

%package -n python%{python3_pkgversion}-azure-storage-blob
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Blobs

%description -n python%{python3_pkgversion}-azure-storage-blob
Microsoft Azure Python SDK - Storage - Blobs

%package -n python%{python3_pkgversion}-azure-storage-common
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Common

%description -n python%{python3_pkgversion}-azure-storage-common
Microsoft Azure Python SDK - Storage - Common

%package -n python%{python3_pkgversion}-azure-storage-file
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Files Shares

%description -n python%{python3_pkgversion}-azure-storage-file
Microsoft Azure Python SDK - Storage - Files Shares

%package -n python%{python3_pkgversion}-azure-storage-file-datalake
Version: 12.3.1
Summary: Microsoft Azure Python SDK - Storage - Files Data Lake

%description -n python%{python3_pkgversion}-azure-storage-file-datalake
Microsoft Azure Python SDK - Storage - Files Data Lake

%package -n python%{python3_pkgversion}-azure-storage-file-share
Version: 12.4.2
Summary: Microsoft Azure Python SDK - Storage - Files Shares

%description -n python%{python3_pkgversion}-azure-storage-file-share
Microsoft Azure Python SDK - Storage - Files Shares

%package -n python%{python3_pkgversion}-azure-storage-nspkg
Version: 3.1.0
Summary: Microsoft Azure Python SDK - Storage Namespace Package

%description -n python%{python3_pkgversion}-azure-storage-nspkg
Microsoft Azure Python SDK - Storage Namespace Package

%package -n python%{python3_pkgversion}-azure-storage-queue
Version: 2.1.0
Summary: Microsoft Azure Python SDK - Storage - Queues

%description -n python%{python3_pkgversion}-azure-storage-queue
Microsoft Azure Python SDK - Storage - Queues

%package -n python%{python3_pkgversion}-azure-synapse
Version: 0.1.1
Summary: Microsoft Azure Python SDK - Synapse

%description -n python%{python3_pkgversion}-azure-synapse
Microsoft Azure Python SDK - Synapse

%package -n python%{python3_pkgversion}-azure-synapse-nspkg
Version: 1.0.0
Summary: Microsoft Azure Python SDK - Synapse Namespace Package

%description -n python%{python3_pkgversion}-azure-synapse-nspkg
Microsoft Azure Python SDK - Synapse Namespace Package

%package -n python%{python3_pkgversion}-azure-template
Version: 0.0.17
Summary: Microsoft Azure Python SDK - Template

%description -n python%{python3_pkgversion}-azure-template
Microsoft Azure Python SDK - Template


%prep
# Create the base directory but skip any extractions for now.
%autosetup -n %{name}-%{version} -c -T
# Extract azure-ai-textanalytics 5.0.0
%autosetup -n %{name}-%{version} -D -T -a 0
# Extract azure-appconfiguration 1.1.1
%autosetup -n %{name}-%{version} -D -T -a 1
# Extract azure-applicationinsights 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 2
# Extract azure-batch 10.0.0
%autosetup -n %{name}-%{version} -D -T -a 3
# Extract azure-cognitiveservices-anomalydetector 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 4
# Extract azure-cognitiveservices-formrecognizer 0.1.1
%autosetup -n %{name}-%{version} -D -T -a 5
# Extract azure-cognitiveservices-knowledge-nspkg 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 6
# Extract azure-cognitiveservices-knowledge-qnamaker 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 7
# Extract azure-cognitiveservices-language-luis 0.7.0
%autosetup -n %{name}-%{version} -D -T -a 8
# Extract azure-cognitiveservices-language-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 9
# Extract azure-cognitiveservices-language-spellcheck 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 10
# Extract azure-cognitiveservices-language-textanalytics 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 11
# Extract azure-cognitiveservices-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 12
# Extract azure-cognitiveservices-personalizer 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 13
# Extract azure-cognitiveservices-search-autosuggest 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 14
# Extract azure-cognitiveservices-search-customimagesearch 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 15
# Extract azure-cognitiveservices-search-customsearch 0.3.0
%autosetup -n %{name}-%{version} -D -T -a 16
# Extract azure-cognitiveservices-search-entitysearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 17
# Extract azure-cognitiveservices-search-imagesearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 18
# Extract azure-cognitiveservices-search-newssearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 19
# Extract azure-cognitiveservices-search-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 20
# Extract azure-cognitiveservices-search-videosearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 21
# Extract azure-cognitiveservices-search-visualsearch 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 22
# Extract azure-cognitiveservices-search-websearch 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 23
# Extract azure-cognitiveservices-vision-computervision 0.9.0
%autosetup -n %{name}-%{version} -D -T -a 24
# Extract azure-cognitiveservices-vision-contentmoderator 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 25
# Extract azure-cognitiveservices-vision-customvision 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 26
# Extract azure-cognitiveservices-vision-face 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 27
# Extract azure-cognitiveservices-vision-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 28
# Extract azure-common 1.1.27
%autosetup -n %{name}-%{version} -D -T -a 29
# Extract azure-communication-chat 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 30
# Extract azure-communication-identity 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 31
# Extract azure-communication-phonenumbers 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 32
# Extract azure-communication-sms 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 33
# Extract azure-core 1.14.0
%autosetup -n %{name}-%{version} -D -T -a 34
# Extract azure-cosmos 3.2.0
%autosetup -n %{name}-%{version} -D -T -a 35
# Extract azure-cosmosdb-table 1.0.6
%autosetup -n %{name}-%{version} -D -T -a 36
# Extract azure-data-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 37
# Extract azure-datalake-store 0.0.51
%autosetup -n %{name}-%{version} -D -T -a 38
# Extract azure-digitaltwins-core 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 39
# Extract azure-digitaltwins-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 40
# Extract azure-eventgrid 4.2.0
%autosetup -n %{name}-%{version} -D -T -a 41
# Extract azure-eventhub 5.5.0
%autosetup -n %{name}-%{version} -D -T -a 42
# Extract azure-graphrbac 0.61.1
%autosetup -n %{name}-%{version} -D -T -a 43
# Extract azure-identity 1.6.0
%autosetup -n %{name}-%{version} -D -T -a 44
# Extract azure-iot-device 2.6.0
%autosetup -n %{name}-%{version} -D -T -a 45
# Extract azure-iot-hub 2.4.0
%autosetup -n %{name}-%{version} -D -T -a 46
# Extract azure-keyvault 4.1.0
%autosetup -n %{name}-%{version} -D -T -a 47
# Extract azure-keyvault-certificates 4.2.1
%autosetup -n %{name}-%{version} -D -T -a 48
# Extract azure-keyvault-keys 4.3.1
%autosetup -n %{name}-%{version} -D -T -a 49
# Extract azure-keyvault-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 50
# Extract azure-keyvault-secrets 4.2.0
%autosetup -n %{name}-%{version} -D -T -a 51
# Extract azure-kusto-data 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 52
# Extract azure-loganalytics 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 53
# Extract azure-mgmt-advisor 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 54
# Extract azure-mgmt-alertsmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 55
# Extract azure-mgmt-apimanagement 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 56
# Extract azure-mgmt-appconfiguration 1.0.1
%autosetup -n %{name}-%{version} -D -T -a 57
# Extract azure-mgmt-applicationinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 58
# Extract azure-mgmt-appplatform 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 59
# Extract azure-mgmt-attestation 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 60
# Extract azure-mgmt-authorization 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 61
# Extract azure-mgmt-automation 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 62
# Extract azure-mgmt-avs 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 63
# Extract azure-mgmt-azurestack 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 64
# Extract azure-mgmt-azurestackhci 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 65
# Extract azure-mgmt-batch 15.0.0
%autosetup -n %{name}-%{version} -D -T -a 66
# Extract azure-mgmt-batchai 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 67
# Extract azure-mgmt-billing 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 68
# Extract azure-mgmt-botservice 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 69
# Extract azure-mgmt-cdn 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 70
# Extract azure-mgmt-cognitiveservices 11.0.0
%autosetup -n %{name}-%{version} -D -T -a 71
# Extract azure-mgmt-commerce 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 72
# Extract azure-mgmt-common 0.20.0
%autosetup -n %{name}-%{version} -D -T -a 73
# Extract azure-mgmt-communication 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 74
# Extract azure-mgmt-compute 21.0.0
%autosetup -n %{name}-%{version} -D -T -a 75
# Extract azure-mgmt-confluent 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 76
# Extract azure-mgmt-consumption 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 77
# Extract azure-mgmt-containerinstance 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 78
# Extract azure-mgmt-containerregistry 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 79
# Extract azure-mgmt-containerservice 15.1.0
%autosetup -n %{name}-%{version} -D -T -a 80
# Extract azure-mgmt-core 1.2.2
%autosetup -n %{name}-%{version} -D -T -a 81
# Extract azure-mgmt-cosmosdb 6.3.0
%autosetup -n %{name}-%{version} -D -T -a 82
# Extract azure-mgmt-costmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 83
# Extract azure-mgmt-customproviders 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 84
# Extract azure-mgmt-databox 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 85
# Extract azure-mgmt-databoxedge 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 86
# Extract azure-mgmt-databricks 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 87
# Extract azure-mgmt-datadog 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 88
# Extract azure-mgmt-datafactory 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 89
# Extract azure-mgmt-datalake-analytics 0.6.0
%autosetup -n %{name}-%{version} -D -T -a 90
# Extract azure-mgmt-datalake-nspkg 3.0.1
%autosetup -n %{name}-%{version} -D -T -a 91
# Extract azure-mgmt-datalake-store 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 92
# Extract azure-mgmt-datamigration 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 93
# Extract azure-mgmt-datashare 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 94
# Extract azure-mgmt-deploymentmanager 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 95
# Extract azure-mgmt-devspaces 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 96
# Extract azure-mgmt-devtestlabs 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 97
# Extract azure-mgmt-digitaltwins 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 98
# Extract azure-mgmt-dns 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 99
# Extract azure-mgmt-edgegateway 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 100
# Extract azure-mgmt-eventgrid 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 101
# Extract azure-mgmt-eventhub 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 102
# Extract azure-mgmt-frontdoor 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 103
# Extract azure-mgmt-hanaonazure 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 104
# Extract azure-mgmt-hdinsight 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 105
# Extract azure-mgmt-healthcareapis 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 106
# Extract azure-mgmt-hybridcompute 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 107
# Extract azure-mgmt-hybridkubernetes 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 108
# Extract azure-mgmt-imagebuilder 0.4.0
%autosetup -n %{name}-%{version} -D -T -a 109
# Extract azure-mgmt-iotcentral 4.1.0
%autosetup -n %{name}-%{version} -D -T -a 110
# Extract azure-mgmt-iothub 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 111
# Extract azure-mgmt-iothubprovisioningservices 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 112
# Extract azure-mgmt-keyvault 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 113
# Extract azure-mgmt-kusto 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 114
# Extract azure-mgmt-labservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 115
# Extract azure-mgmt-loganalytics 10.0.0
%autosetup -n %{name}-%{version} -D -T -a 116
# Extract azure-mgmt-logic 9.0.0
%autosetup -n %{name}-%{version} -D -T -a 117
# Extract azure-mgmt-machinelearningcompute 0.4.1
%autosetup -n %{name}-%{version} -D -T -a 118
# Extract azure-mgmt-machinelearningservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 119
# Extract azure-mgmt-maintenance 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 120
# Extract azure-mgmt-managedservices 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 121
# Extract azure-mgmt-managementgroups 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 122
# Extract azure-mgmt-managementpartner 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 123
# Extract azure-mgmt-maps 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 124
# Extract azure-mgmt-marketplaceordering 1.1.0
%autosetup -n %{name}-%{version} -D -T -a 125
# Extract azure-mgmt-media 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 126
# Extract azure-mgmt-mixedreality 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 127
# Extract azure-mgmt-monitor 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 128
# Extract azure-mgmt-msi 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 129
# Extract azure-mgmt-netapp 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 130
# Extract azure-mgmt-network 19.0.0
%autosetup -n %{name}-%{version} -D -T -a 131
# Extract azure-mgmt-notificationhubs 7.0.0
%autosetup -n %{name}-%{version} -D -T -a 132
# Extract azure-mgmt-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 133
# Extract azure-mgmt-operationsmanagement 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 134
# Extract azure-mgmt-peering 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 135
# Extract azure-mgmt-policyinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 136
# Extract azure-mgmt-powerbidedicated 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 137
# Extract azure-mgmt-powerbiembedded 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 138
# Extract azure-mgmt-privatedns 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 139
# Extract azure-mgmt-rdbms 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 140
# Extract azure-mgmt-recoveryservices 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 141
# Extract azure-mgmt-recoveryservicesbackup 0.12.0
%autosetup -n %{name}-%{version} -D -T -a 142
# Extract azure-mgmt-redhatopenshift 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 143
# Extract azure-mgmt-redis 12.0.0
%autosetup -n %{name}-%{version} -D -T -a 144
# Extract azure-mgmt-relay 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 145
# Extract azure-mgmt-reservations 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 146
# Extract azure-mgmt-resource 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 147
# Extract azure-mgmt-resourcegraph 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 148
# Extract azure-mgmt-resourcemover 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 149
# Extract azure-mgmt-scheduler 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 150
# Extract azure-mgmt-search 8.0.0
%autosetup -n %{name}-%{version} -D -T -a 151
# Extract azure-mgmt-security 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 152
# Extract azure-mgmt-serialconsole 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 153
# Extract azure-mgmt-servermanager 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 154
# Extract azure-mgmt-servicebus 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 155
# Extract azure-mgmt-sql 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 156
# Extract azure-mgmt-sqlvirtualmachine 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 157
# Extract azure-mgmt-storage 18.0.0
%autosetup -n %{name}-%{version} -D -T -a 158
# Extract azure-mgmt-storagecache 0.5.0
%autosetup -n %{name}-%{version} -D -T -a 159
# Extract azure-mgmt-storageimportexport 0.1.0
%autosetup -n %{name}-%{version} -D -T -a 160
# Extract azure-mgmt-storagesync 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 161
# Extract azure-mgmt-subscription 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 162
# Extract azure-mgmt-support 6.0.0
%autosetup -n %{name}-%{version} -D -T -a 163
# Extract azure-mgmt-synapse 2.0.0
%autosetup -n %{name}-%{version} -D -T -a 164
# Extract azure-mgmt-timeseriesinsights 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 165
# Extract azure-mgmt-trafficmanager 0.51.0
%autosetup -n %{name}-%{version} -D -T -a 166
# Extract azure-mgmt-vmwarecloudsimple 0.2.0
%autosetup -n %{name}-%{version} -D -T -a 167
# Extract azure-mgmt-web 3.0.0
%autosetup -n %{name}-%{version} -D -T -a 168
# Extract azure-nspkg 3.0.2
%autosetup -n %{name}-%{version} -D -T -a 169
# Extract azure-search-documents 11.1.0
%autosetup -n %{name}-%{version} -D -T -a 170
# Extract azure-search-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 171
# Extract azure-servicebus 7.2.0
%autosetup -n %{name}-%{version} -D -T -a 172
# Extract azure-servicefabric 8.0.0.0
%autosetup -n %{name}-%{version} -D -T -a 173
# Extract azure-storage-blob 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 174
# Extract azure-storage-common 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 175
# Extract azure-storage-file 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 176
# Extract azure-storage-file-datalake 12.3.1
%autosetup -n %{name}-%{version} -D -T -a 177
# Extract azure-storage-file-share 12.4.2
%autosetup -n %{name}-%{version} -D -T -a 178
# Extract azure-storage-nspkg 3.1.0
%autosetup -n %{name}-%{version} -D -T -a 179
# Extract azure-storage-queue 2.1.0
%autosetup -n %{name}-%{version} -D -T -a 180
# Extract azure-synapse 0.1.1
%autosetup -n %{name}-%{version} -D -T -a 181
# Extract azure-synapse-nspkg 1.0.0
%autosetup -n %{name}-%{version} -D -T -a 182
# Extract azure-template 0.0.17
%autosetup -n %{name}-%{version} -D -T -a 183


%generate_buildrequires
%pyproject_buildrequires

%build
# Get a list of python projects that we've extracted.
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)

# Loop over each project and build a wheel for each.
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %pyproject_wheel
    popd
done

%install
%pyproject_install

# Some of the wheels contain random stuff at the top level that don't belong in
# any RPM packages.
rm -rf %{buildroot}%{python3_sitelib}/{doc,samples,tests}


%files -n python%{python3_pkgversion}-azure-ai-textanalytics
%{python3_sitelib}/azure/ai/textanalytics
%{python3_sitelib}/azure_ai_textanalytics-*.dist-info/


%files -n python%{python3_pkgversion}-azure-appconfiguration
%{python3_sitelib}/azure/appconfiguration
%{python3_sitelib}/azure_appconfiguration-*.dist-info/


%files -n python%{python3_pkgversion}-azure-applicationinsights
%{python3_sitelib}/azure/applicationinsights
%{python3_sitelib}/azure_applicationinsights-*.dist-info/


%files -n python%{python3_pkgversion}-azure-batch
%{python3_sitelib}/azure/batch
%{python3_sitelib}/azure_batch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-anomalydetector
%{python3_sitelib}/azure/cognitiveservices/anomalydetector
%{python3_sitelib}/azure_cognitiveservices_anomalydetector-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-formrecognizer
%{python3_sitelib}/azure/cognitiveservices/formrecognizer
%{python3_sitelib}/azure_cognitiveservices_formrecognizer-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-nspkg
%{python3_sitelib}/azure_cognitiveservices_knowledge_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-knowledge-qnamaker
%{python3_sitelib}/azure/cognitiveservices/knowledge/qnamaker
%{python3_sitelib}/azure_cognitiveservices_knowledge_qnamaker-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-language-luis
%{python3_sitelib}/azure/cognitiveservices/language/luis
%{python3_sitelib}/azure_cognitiveservices_language_luis-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-language-nspkg
%{python3_sitelib}/azure_cognitiveservices_language_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-language-spellcheck
%{python3_sitelib}/azure/cognitiveservices/language/spellcheck
%{python3_sitelib}/azure_cognitiveservices_language_spellcheck-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-language-textanalytics
%{python3_sitelib}/azure/cognitiveservices/language/textanalytics
%{python3_sitelib}/azure_cognitiveservices_language_textanalytics-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-nspkg
%{python3_sitelib}/azure_cognitiveservices_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-personalizer
%{python3_sitelib}/azure/cognitiveservices/personalizer
%{python3_sitelib}/azure_cognitiveservices_personalizer-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-autosuggest
%{python3_sitelib}/azure/cognitiveservices/search/autosuggest
%{python3_sitelib}/azure_cognitiveservices_search_autosuggest-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-customimagesearch
%{python3_sitelib}/azure/cognitiveservices/search/customimagesearch
%{python3_sitelib}/azure_cognitiveservices_search_customimagesearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-customsearch
%{python3_sitelib}/azure/cognitiveservices/search/customsearch
%{python3_sitelib}/azure_cognitiveservices_search_customsearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-entitysearch
%{python3_sitelib}/azure/cognitiveservices/search/entitysearch
%{python3_sitelib}/azure_cognitiveservices_search_entitysearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-imagesearch
%{python3_sitelib}/azure/cognitiveservices/search/imagesearch
%{python3_sitelib}/azure_cognitiveservices_search_imagesearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-newssearch
%{python3_sitelib}/azure/cognitiveservices/search/newssearch
%{python3_sitelib}/azure_cognitiveservices_search_newssearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-nspkg
%{python3_sitelib}/azure_cognitiveservices_search_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-videosearch
%{python3_sitelib}/azure/cognitiveservices/search/videosearch
%{python3_sitelib}/azure_cognitiveservices_search_videosearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-visualsearch
%{python3_sitelib}/azure/cognitiveservices/search/visualsearch
%{python3_sitelib}/azure_cognitiveservices_search_visualsearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-search-websearch
%{python3_sitelib}/azure/cognitiveservices/search/websearch
%{python3_sitelib}/azure_cognitiveservices_search_websearch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-vision-computervision
%{python3_sitelib}/azure/cognitiveservices/vision/computervision
%{python3_sitelib}/azure_cognitiveservices_vision_computervision-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-vision-contentmoderator
%{python3_sitelib}/azure/cognitiveservices/vision/contentmoderator
%{python3_sitelib}/azure_cognitiveservices_vision_contentmoderator-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-vision-customvision
%{python3_sitelib}/azure/cognitiveservices/vision/customvision
%{python3_sitelib}/azure_cognitiveservices_vision_customvision-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-vision-face
%{python3_sitelib}/azure/cognitiveservices/vision/face
%{python3_sitelib}/azure_cognitiveservices_vision_face-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cognitiveservices-vision-nspkg
%{python3_sitelib}/azure_cognitiveservices_vision_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-common
%{python3_sitelib}/azure/common
%{python3_sitelib}/azure_common-*.dist-info/
%{python3_sitelib}/azure/profiles/__init__.py
%{python3_sitelib}/azure/profiles/__pycache__/__init__*
%{python3_sitelib}/azure/profiles/multiapiclient.py
%{python3_sitelib}/azure/profiles/__pycache__/multiapiclient*.pyc


%files -n python%{python3_pkgversion}-azure-communication-chat
%{python3_sitelib}/azure/communication/chat
%{python3_sitelib}/azure_communication_chat-*.dist-info/


%files -n python%{python3_pkgversion}-azure-communication-identity
%{python3_sitelib}/azure/communication/identity
%{python3_sitelib}/azure_communication_identity-*.dist-info/


%files -n python%{python3_pkgversion}-azure-communication-phonenumbers
%{python3_sitelib}/azure/communication/phonenumbers
%{python3_sitelib}/azure_communication_phonenumbers-*.dist-info/


%files -n python%{python3_pkgversion}-azure-communication-sms
%{python3_sitelib}/azure/communication/sms
%{python3_sitelib}/azure_communication_sms-*.dist-info/


%files -n python%{python3_pkgversion}-azure-core
%{python3_sitelib}/azure/core
%{python3_sitelib}/azure_core-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cosmos
%{python3_sitelib}/azure/cosmos
%{python3_sitelib}/azure_cosmos-*.dist-info/


%files -n python%{python3_pkgversion}-azure-cosmosdb-table
%{python3_sitelib}/azure/cosmosdb/table
%{python3_sitelib}/azure_cosmosdb_table-*.dist-info/


%files -n python%{python3_pkgversion}-azure-data-nspkg
%{python3_sitelib}/azure_data_nspkg-*.dist-info/
%{python3_sitelib}/azure/data/__init__.py
%{python3_sitelib}/azure/data/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-datalake-store
%{python3_sitelib}/azure/datalake/store
%{python3_sitelib}/azure_datalake_store-*.dist-info/
%{python3_sitelib}/azure/datalake/__init__.py
%{python3_sitelib}/azure/datalake/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-digitaltwins-core
%{python3_sitelib}/azure/digitaltwins/core
%{python3_sitelib}/azure_digitaltwins_core-*.dist-info/


%files -n python%{python3_pkgversion}-azure-digitaltwins-nspkg
%{python3_sitelib}/azure_digitaltwins_nspkg-*.dist-info/
%{python3_sitelib}/azure/digitaltwins/__init__.py
%{python3_sitelib}/azure/digitaltwins/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-eventgrid
%{python3_sitelib}/azure/eventgrid
%{python3_sitelib}/azure_eventgrid-*.dist-info/


%files -n python%{python3_pkgversion}-azure-eventhub
%{python3_sitelib}/azure/eventhub
%{python3_sitelib}/azure_eventhub-*.dist-info/


%files -n python%{python3_pkgversion}-azure-graphrbac
%{python3_sitelib}/azure/graphrbac
%{python3_sitelib}/azure_graphrbac-*.dist-info/


%files -n python%{python3_pkgversion}-azure-identity
%{python3_sitelib}/azure/identity
%{python3_sitelib}/azure_identity-*.dist-info/


%files -n python%{python3_pkgversion}-azure-iot-device
%{python3_sitelib}/azure/iot/device
%{python3_sitelib}/azure_iot_device-*.dist-info/


%files -n python%{python3_pkgversion}-azure-iot-hub
%{python3_sitelib}/azure/iot/hub
%{python3_sitelib}/azure_iot_hub-*.dist-info/


%files -n python%{python3_pkgversion}-azure-keyvault
%{python3_sitelib}/azure/keyvault
%{python3_sitelib}/azure_keyvault-*.dist-info/


%files -n python%{python3_pkgversion}-azure-keyvault-certificates
%{python3_sitelib}/azure/keyvault/certificates
%{python3_sitelib}/azure_keyvault_certificates-*.dist-info/


%files -n python%{python3_pkgversion}-azure-keyvault-keys
%{python3_sitelib}/azure/keyvault/keys
%{python3_sitelib}/azure_keyvault_keys-*.dist-info/


%files -n python%{python3_pkgversion}-azure-keyvault-nspkg
%{python3_sitelib}/azure_keyvault_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-keyvault-secrets
%{python3_sitelib}/azure/keyvault/secrets
%{python3_sitelib}/azure_keyvault_secrets-*.dist-info/


%files -n python%{python3_pkgversion}-azure-kusto-data
%{python3_sitelib}/azure/kusto/data
%{python3_sitelib}/azure_kusto_data-*.dist-info/
%{python3_sitelib}/azure/kusto/__init__.py
%{python3_sitelib}/azure/kusto/__pycache__/__init__*
%{python3_sitelib}/azure_kusto_data-*.pth


%files -n python%{python3_pkgversion}-azure-loganalytics
%{python3_sitelib}/azure/loganalytics
%{python3_sitelib}/azure_loganalytics-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-advisor
%{python3_sitelib}/azure/mgmt/advisor
%{python3_sitelib}/azure_mgmt_advisor-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-alertsmanagement
%{python3_sitelib}/azure/mgmt/alertsmanagement
%{python3_sitelib}/azure_mgmt_alertsmanagement-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-apimanagement
%{python3_sitelib}/azure/mgmt/apimanagement
%{python3_sitelib}/azure_mgmt_apimanagement-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-appconfiguration
%{python3_sitelib}/azure/mgmt/appconfiguration
%{python3_sitelib}/azure_mgmt_appconfiguration-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-applicationinsights
%{python3_sitelib}/azure/mgmt/applicationinsights
%{python3_sitelib}/azure_mgmt_applicationinsights-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-appplatform
%{python3_sitelib}/azure/mgmt/appplatform
%{python3_sitelib}/azure_mgmt_appplatform-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-attestation
%{python3_sitelib}/azure/mgmt/attestation
%{python3_sitelib}/azure_mgmt_attestation-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-authorization
%{python3_sitelib}/azure/mgmt/authorization
%{python3_sitelib}/azure_mgmt_authorization-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-automation
%{python3_sitelib}/azure/mgmt/automation
%{python3_sitelib}/azure_mgmt_automation-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-avs
%{python3_sitelib}/azure/mgmt/avs
%{python3_sitelib}/azure_mgmt_avs-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-azurestack
%{python3_sitelib}/azure/mgmt/azurestack
%{python3_sitelib}/azure_mgmt_azurestack-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-azurestackhci
%{python3_sitelib}/azure/mgmt/azurestackhci
%{python3_sitelib}/azure_mgmt_azurestackhci-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-batch
%{python3_sitelib}/azure/mgmt/batch
%{python3_sitelib}/azure_mgmt_batch-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-batchai
%{python3_sitelib}/azure/mgmt/batchai
%{python3_sitelib}/azure_mgmt_batchai-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-billing
%{python3_sitelib}/azure/mgmt/billing
%{python3_sitelib}/azure_mgmt_billing-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-botservice
%{python3_sitelib}/azure/mgmt/botservice
%{python3_sitelib}/azure_mgmt_botservice-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-cdn
%{python3_sitelib}/azure/mgmt/cdn
%{python3_sitelib}/azure_mgmt_cdn-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-cognitiveservices
%{python3_sitelib}/azure/mgmt/cognitiveservices
%{python3_sitelib}/azure_mgmt_cognitiveservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-commerce
%{python3_sitelib}/azure/mgmt/commerce
%{python3_sitelib}/azure_mgmt_commerce-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-common
%{python3_sitelib}/azure/mgmt/common
%{python3_sitelib}/azure_mgmt_common-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-communication
%{python3_sitelib}/azure/mgmt/communication
%{python3_sitelib}/azure_mgmt_communication-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-compute
%{python3_sitelib}/azure/mgmt/compute
%{python3_sitelib}/azure_mgmt_compute-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-confluent
%{python3_sitelib}/azure/mgmt/confluent
%{python3_sitelib}/azure_mgmt_confluent-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-consumption
%{python3_sitelib}/azure/mgmt/consumption
%{python3_sitelib}/azure_mgmt_consumption-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-containerinstance
%{python3_sitelib}/azure/mgmt/containerinstance
%{python3_sitelib}/azure_mgmt_containerinstance-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-containerregistry
%{python3_sitelib}/azure/mgmt/containerregistry
%{python3_sitelib}/azure_mgmt_containerregistry-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-containerservice
%{python3_sitelib}/azure/mgmt/containerservice
%{python3_sitelib}/azure_mgmt_containerservice-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-core
%{python3_sitelib}/azure/mgmt/core
%{python3_sitelib}/azure_mgmt_core-*.dist-info/
%{python3_sitelib}/azure/__init__.py
%{python3_sitelib}/azure/__pycache__/__init__*
%{python3_sitelib}/azure/mgmt/__init__.py
%{python3_sitelib}/azure/mgmt/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-mgmt-cosmosdb
%{python3_sitelib}/azure/mgmt/cosmosdb
%{python3_sitelib}/azure_mgmt_cosmosdb-*.dist-info/
%{python3_sitelib}/azure/cosmosdb/__init__.py
%{python3_sitelib}/azure/cosmosdb/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-mgmt-costmanagement
%{python3_sitelib}/azure/mgmt/costmanagement
%{python3_sitelib}/azure_mgmt_costmanagement-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-customproviders
%{python3_sitelib}/azure/mgmt/customproviders
%{python3_sitelib}/azure_mgmt_customproviders-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-databox
%{python3_sitelib}/azure/mgmt/databox
%{python3_sitelib}/azure_mgmt_databox-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-databoxedge
%{python3_sitelib}/azure/mgmt/databoxedge
%{python3_sitelib}/azure_mgmt_databoxedge-*.dist-info/
%{python3_sitelib}/azure/mgmt/datab


%files -n python%{python3_pkgversion}-azure-mgmt-databricks
%{python3_sitelib}/azure/mgmt/databricks
%{python3_sitelib}/azure_mgmt_databricks-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datadog
%{python3_sitelib}/azure/mgmt/datadog
%{python3_sitelib}/azure_mgmt_datadog-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datafactory
%{python3_sitelib}/azure/mgmt/datafactory
%{python3_sitelib}/azure_mgmt_datafactory-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datalake-analytics
%{python3_sitelib}/azure/mgmt/datalake/analytics
%{python3_sitelib}/azure_mgmt_datalake_analytics-*.dist-info/
%{python3_sitelib}/azure/mgmt/datalake/__init__.py
%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-mgmt-datalake-nspkg
%{python3_sitelib}/azure_mgmt_datalake_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datalake-store
%{python3_sitelib}/azure/mgmt/datalake/store
%{python3_sitelib}/azure_mgmt_datalake_store-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datamigration
%{python3_sitelib}/azure/mgmt/datamigration
%{python3_sitelib}/azure_mgmt_datamigration-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-datashare
%{python3_sitelib}/azure/mgmt/datashare
%{python3_sitelib}/azure_mgmt_datashare-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-deploymentmanager
%{python3_sitelib}/azure/mgmt/deploymentmanager
%{python3_sitelib}/azure_mgmt_deploymentmanager-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-devspaces
%{python3_sitelib}/azure/mgmt/devspaces
%{python3_sitelib}/azure_mgmt_devspaces-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-devtestlabs
%{python3_sitelib}/azure/mgmt/devtestlabs
%{python3_sitelib}/azure_mgmt_devtestlabs-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-digitaltwins
%{python3_sitelib}/azure/mgmt/digitaltwins
%{python3_sitelib}/azure_mgmt_digitaltwins-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-dns
%{python3_sitelib}/azure/mgmt/dns
%{python3_sitelib}/azure_mgmt_dns-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-edgegateway
%{python3_sitelib}/azure/mgmt/edgegateway
%{python3_sitelib}/azure_mgmt_edgegateway-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-eventgrid
%{python3_sitelib}/azure/mgmt/eventgrid
%{python3_sitelib}/azure_mgmt_eventgrid-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-eventhub
%{python3_sitelib}/azure/mgmt/eventhub
%{python3_sitelib}/azure_mgmt_eventhub-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-frontdoor
%{python3_sitelib}/azure/mgmt/frontdoor
%{python3_sitelib}/azure_mgmt_frontdoor-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-hanaonazure
%{python3_sitelib}/azure/mgmt/hanaonazure
%{python3_sitelib}/azure_mgmt_hanaonazure-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-hdinsight
%{python3_sitelib}/azure/mgmt/hdinsight
%{python3_sitelib}/azure_mgmt_hdinsight-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-healthcareapis
%{python3_sitelib}/azure/mgmt/healthcareapis
%{python3_sitelib}/azure_mgmt_healthcareapis-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-hybridcompute
%{python3_sitelib}/azure/mgmt/hybridcompute
%{python3_sitelib}/azure_mgmt_hybridcompute-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-hybridkubernetes
%{python3_sitelib}/azure/mgmt/hybridkubernetes
%{python3_sitelib}/azure_mgmt_hybridkubernetes-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-imagebuilder
%{python3_sitelib}/azure/mgmt/imagebuilder
%{python3_sitelib}/azure_mgmt_imagebuilder-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-iotcentral
%{python3_sitelib}/azure/mgmt/iotcentral
%{python3_sitelib}/azure_mgmt_iotcentral-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-iothub
%{python3_sitelib}/azure/mgmt/iothub
%{python3_sitelib}/azure_mgmt_iothub-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-iothubprovisioningservices
%{python3_sitelib}/azure/mgmt/iothubprovisioningservices
%{python3_sitelib}/azure_mgmt_iothubprovisioningservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-keyvault
%{python3_sitelib}/azure/mgmt/keyvault
%{python3_sitelib}/azure_mgmt_keyvault-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-kusto
%{python3_sitelib}/azure/mgmt/kusto
%{python3_sitelib}/azure_mgmt_kusto-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-labservices
%{python3_sitelib}/azure/mgmt/labservices
%{python3_sitelib}/azure_mgmt_labservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-loganalytics
%{python3_sitelib}/azure/mgmt/loganalytics
%{python3_sitelib}/azure_mgmt_loganalytics-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-logic
%{python3_sitelib}/azure/mgmt/logic
%{python3_sitelib}/azure_mgmt_logic-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-machinelearningcompute
%{python3_sitelib}/azure/mgmt/machinelearningcompute
%{python3_sitelib}/azure_mgmt_machinelearningcompute-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-machinelearningservices
%{python3_sitelib}/azure/mgmt/machinelearningservices
%{python3_sitelib}/azure_mgmt_machinelearningservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-maintenance
%{python3_sitelib}/azure/mgmt/maintenance
%{python3_sitelib}/azure_mgmt_maintenance-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-managedservices
%{python3_sitelib}/azure/mgmt/managedservices
%{python3_sitelib}/azure_mgmt_managedservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-managementgroups
%{python3_sitelib}/azure/mgmt/managementgroups
%{python3_sitelib}/azure_mgmt_managementgroups-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-managementpartner
%{python3_sitelib}/azure/mgmt/managementpartner
%{python3_sitelib}/azure_mgmt_managementpartner-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-maps
%{python3_sitelib}/azure/mgmt/maps
%{python3_sitelib}/azure_mgmt_maps-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-marketplaceordering
%{python3_sitelib}/azure/mgmt/marketplaceordering
%{python3_sitelib}/azure_mgmt_marketplaceordering-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-media
%{python3_sitelib}/azure/mgmt/media
%{python3_sitelib}/azure_mgmt_media-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-mixedreality
%{python3_sitelib}/azure/mgmt/mixedreality
%{python3_sitelib}/azure_mgmt_mixedreality-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-monitor
%{python3_sitelib}/azure/mgmt/monitor
%{python3_sitelib}/azure_mgmt_monitor-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-msi
%{python3_sitelib}/azure/mgmt/msi
%{python3_sitelib}/azure_mgmt_msi-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-netapp
%{python3_sitelib}/azure/mgmt/netapp
%{python3_sitelib}/azure_mgmt_netapp-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-network
%{python3_sitelib}/azure/mgmt/network
%{python3_sitelib}/azure_mgmt_network-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-notificationhubs
%{python3_sitelib}/azure/mgmt/notificationhubs
%{python3_sitelib}/azure_mgmt_notificationhubs-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-nspkg
%{python3_sitelib}/azure_mgmt_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-operationsmanagement
%{python3_sitelib}/azure/mgmt/operationsmanagement
%{python3_sitelib}/azure_mgmt_operationsmanagement-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-peering
%{python3_sitelib}/azure/mgmt/peering
%{python3_sitelib}/azure_mgmt_peering-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-policyinsights
%{python3_sitelib}/azure/mgmt/policyinsights
%{python3_sitelib}/azure_mgmt_policyinsights-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-powerbidedicated
%{python3_sitelib}/azure/mgmt/powerbidedicated
%{python3_sitelib}/azure_mgmt_powerbidedicated-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-powerbiembedded
%{python3_sitelib}/azure/mgmt/powerbiembedded
%{python3_sitelib}/azure_mgmt_powerbiembedded-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-privatedns
%{python3_sitelib}/azure/mgmt/privatedns
%{python3_sitelib}/azure_mgmt_privatedns-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-rdbms
%{python3_sitelib}/azure/mgmt/rdbms
%{python3_sitelib}/azure_mgmt_rdbms-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-recoveryservices
%{python3_sitelib}/azure/mgmt/recoveryservices
%{python3_sitelib}/azure_mgmt_recoveryservices-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-recoveryservicesbackup
%{python3_sitelib}/azure/mgmt/recoveryservicesbackup
%{python3_sitelib}/azure_mgmt_recoveryservicesbackup-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-redhatopenshift
%{python3_sitelib}/azure/mgmt/redhatopenshift
%{python3_sitelib}/azure_mgmt_redhatopenshift-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-redis
%{python3_sitelib}/azure/mgmt/redis
%{python3_sitelib}/azure_mgmt_redis-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-relay
%{python3_sitelib}/azure/mgmt/relay
%{python3_sitelib}/azure_mgmt_relay-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-reservations
%{python3_sitelib}/azure/mgmt/reservations
%{python3_sitelib}/azure_mgmt_reservations-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-resource
%{python3_sitelib}/azure/mgmt/resource
%{python3_sitelib}/azure_mgmt_resource-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-resourcegraph
%{python3_sitelib}/azure/mgmt/resourcegraph
%{python3_sitelib}/azure_mgmt_resourcegraph-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-resourcemover
%{python3_sitelib}/azure/mgmt/resourcemover
%{python3_sitelib}/azure_mgmt_resourcemover-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-scheduler
%{python3_sitelib}/azure/mgmt/scheduler
%{python3_sitelib}/azure_mgmt_scheduler-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-search
%{python3_sitelib}/azure/mgmt/search
%{python3_sitelib}/azure_mgmt_search-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-security
%{python3_sitelib}/azure/mgmt/security
%{python3_sitelib}/azure_mgmt_security-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-serialconsole
%{python3_sitelib}/azure/mgmt/serialconsole
%{python3_sitelib}/azure_mgmt_serialconsole-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-servermanager
%{python3_sitelib}/azure/mgmt/servermanager
%{python3_sitelib}/azure_mgmt_servermanager-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-servicebus
%{python3_sitelib}/azure/mgmt/servicebus
%{python3_sitelib}/azure_mgmt_servicebus-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-sql
%{python3_sitelib}/azure/mgmt/sql
%{python3_sitelib}/azure_mgmt_sql-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-sqlvirtualmachine
%{python3_sitelib}/azure/mgmt/sqlvirtualmachine
%{python3_sitelib}/azure_mgmt_sqlvirtualmachine-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-storage
%{python3_sitelib}/azure/mgmt/storage
%{python3_sitelib}/azure_mgmt_storage-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-storagecache
%{python3_sitelib}/azure/mgmt/storagecache
%{python3_sitelib}/azure_mgmt_storagecache-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-storageimportexport
%{python3_sitelib}/azure/mgmt/storageimportexport
%{python3_sitelib}/azure_mgmt_storageimportexport-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-storagesync
%{python3_sitelib}/azure/mgmt/storagesync
%{python3_sitelib}/azure_mgmt_storagesync-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-subscription
%{python3_sitelib}/azure/mgmt/subscription
%{python3_sitelib}/azure_mgmt_subscription-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-support
%{python3_sitelib}/azure/mgmt/support
%{python3_sitelib}/azure_mgmt_support-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-synapse
%{python3_sitelib}/azure/mgmt/synapse
%{python3_sitelib}/azure_mgmt_synapse-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-timeseriesinsights
%{python3_sitelib}/azure/mgmt/timeseriesinsights
%{python3_sitelib}/azure_mgmt_timeseriesinsights-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-trafficmanager
%{python3_sitelib}/azure/mgmt/trafficmanager
%{python3_sitelib}/azure_mgmt_trafficmanager-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-vmwarecloudsimple
%{python3_sitelib}/azure/mgmt/vmwarecloudsimple
%{python3_sitelib}/azure_mgmt_vmwarecloudsimple-*.dist-info/


%files -n python%{python3_pkgversion}-azure-mgmt-web
%{python3_sitelib}/azure/mgmt/web
%{python3_sitelib}/azure_mgmt_web-*.dist-info/


%files -n python%{python3_pkgversion}-azure-nspkg
%{python3_sitelib}/azure_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-search-documents
%{python3_sitelib}/azure/search/documents
%{python3_sitelib}/azure_search_documents-*.dist-info/


%files -n python%{python3_pkgversion}-azure-search-nspkg
%{python3_sitelib}/azure_search_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-servicebus
%{python3_sitelib}/azure/servicebus
%{python3_sitelib}/azure_servicebus-*.dist-info/


%files -n python%{python3_pkgversion}-azure-servicefabric
%{python3_sitelib}/azure/servicefabric
%{python3_sitelib}/azure_servicefabric-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-blob
%{python3_sitelib}/azure/storage/blob
%{python3_sitelib}/azure_storage_blob-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-common
%{python3_sitelib}/azure/storage/common
%{python3_sitelib}/azure_storage_common-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-file
%{python3_sitelib}/azure/storage/file
%{python3_sitelib}/azure_storage_file-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-file-datalake
%{python3_sitelib}/azure/storage/filedatalake
%{python3_sitelib}/azure_storage_file_datalake-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-file-share
%{python3_sitelib}/azure/storage/fileshare
%{python3_sitelib}/azure_storage_file_share-*.dist-info/


%files -n python%{python3_pkgversion}-azure-storage-nspkg
%{python3_sitelib}/azure_storage_nspkg-*.dist-info/
%{python3_sitelib}/azure/storage/__init__.py
%{python3_sitelib}/azure/storage/__pycache__/__init__*


%files -n python%{python3_pkgversion}-azure-storage-queue
%{python3_sitelib}/azure/storage/queue
%{python3_sitelib}/azure_storage_queue-*.dist-info/


%files -n python%{python3_pkgversion}-azure-synapse
%{python3_sitelib}/azure/synapse
%{python3_sitelib}/azure_synapse-*.dist-info/


%files -n python%{python3_pkgversion}-azure-synapse-nspkg
%{python3_sitelib}/azure_synapse_nspkg-*.dist-info/


%files -n python%{python3_pkgversion}-azure-template
%{python3_sitelib}/azure/template
%{python3_sitelib}/azure_template-*.dist-info/



%changelog
* Thu May 27 2021 Major Hayden - 20210527-1
- First package.