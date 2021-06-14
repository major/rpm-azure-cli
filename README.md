# Azure CLI/SDK RPM packaging

This is a tracker for getting the Azure CLI and SDK packaged in Fedora.

## Package status

| Package | Status | Notes |
| ------- | ------ | ----- |
| azure-cli | ⚫ | |
| python-applicationinsights | ⚫ | Not needed if `python-azure-cli-telemetry` is skipped |
| python-azure-appconfiguration | 🟡 | [RH BZ 1971775](https://bugzilla.redhat.com/show_bug.cgi?id=1971775) |
| python-azure-batch | 🟡 | [RH BZ 1971717](https://bugzilla.redhat.com/show_bug.cgi?id=1971717) |
| python-azure-cli-core | ⚫ | |
| python-azure-cli-telemetry | ⚫ | Likely going to skip this one to maintain privacy. |
| python-azure-common | 🟡 | [RH BZ 1970619](https://bugzilla.redhat.com/show_bug.cgi?id=1970619) |
| python-azure-core | 🔵 | [RH BZ 1970073](https://bugzilla.redhat.com/show_bug.cgi?id=1970073) |
| python-azure-cosmos | 🟡 | [RH BZ 1971750](https://bugzilla.redhat.com/show_bug.cgi?id=1971750) |
| python-azure-datalake-store | 🟡 | [RH BZ 1971751](https://bugzilla.redhat.com/show_bug.cgi?id=1971751) |
| python-azure-devtools | ⚫ | |
| python-azure-functions-devops-build | 🟡 | [RH BZ 1971753](https://bugzilla.redhat.com/show_bug.cgi?id=1971753) |
| python-azure-graphrbac | 🟡 | [RH BZ 1971758](https://bugzilla.redhat.com/show_bug.cgi?id=1971758) |
| python-azure-identity | 🟡 | [RH BZ 1971760](https://bugzilla.redhat.com/show_bug.cgi?id=1971760) |
| python-azure-keyvault-administration | 🟡 | [RH BZ 1971761](https://bugzilla.redhat.com/show_bug.cgi?id=1971761) |
| python-azure-keyvault-certificates | 🟡 | [RH BZ 1971763](https://bugzilla.redhat.com/show_bug.cgi?id=1971763) |
| python-azure-keyvault-keys | 🟡 | [RH BZ 1971766](https://bugzilla.redhat.com/show_bug.cgi?id=1971766) |
| python-azure-keyvault-secrets | 🟡 | [RH BZ 1971767](https://bugzilla.redhat.com/show_bug.cgi?id=1971767) |
| python-azure-keyvault | 🟡 | [RH BZ 1971768](https://bugzilla.redhat.com/show_bug.cgi?id=1971768) |
| python-azure-loganalytics | 🟡 | [RH BZ 1971769](https://bugzilla.redhat.com/show_bug.cgi?id=1971769) |
| python-azure-mgmt-advisor | 🟡 | [RH BZ 1971770](https://bugzilla.redhat.com/show_bug.cgi?id=1971770) |
| python-azure-mgmt-apimanagement | 🟡 | [RH BZ 1971772](https://bugzilla.redhat.com/show_bug.cgi?id=1971772) |
| python-azure-mgmt-appconfiguration | 🟡 | [RH BZ 1971775](https://bugzilla.redhat.com/show_bug.cgi?id=1971775) |
| python-azure-mgmt-applicationinsights | 🟡 | [RH BZ 1971776](https://bugzilla.redhat.com/show_bug.cgi?id=1971776) |
| python-azure-mgmt-authorization | 🟡 | [RH BZ 1971777](https://bugzilla.redhat.com/show_bug.cgi?id=1971777) |
| python-azure-mgmt-batchai | 🟡 | [RH BZ 1971780](https://bugzilla.redhat.com/show_bug.cgi?id=1971780) |
| python-azure-mgmt-batch | 🟡 | [RH BZ 1971778](https://bugzilla.redhat.com/show_bug.cgi?id=1971778) |
| python-azure-mgmt-billing | 🟡 | [RH BZ 1971781](https://bugzilla.redhat.com/show_bug.cgi?id=1971781) |
| python-azure-mgmt-botservice | 🟡 | [RH BZ 1971782](https://bugzilla.redhat.com/show_bug.cgi?id=1971782) |
| python-azure-mgmt-cdn | 🟡 | [RH BZ 1971784](https://bugzilla.redhat.com/show_bug.cgi?id=1971784) |
| python-azure-mgmt-cognitiveservices | 🟡 | [RH BZ 1971786](https://bugzilla.redhat.com/show_bug.cgi?id=1971786) |
| python-azure-mgmt-compute | 🟡 | [RH BZ 1971787](https://bugzilla.redhat.com/show_bug.cgi?id=1971787) |
| python-azure-mgmt-consumption | 🟡 | [RH BZ 1971790](https://bugzilla.redhat.com/show_bug.cgi?id=1971790) |
| python-azure-mgmt-containerinstance | 🟡 | [RH BZ 1971791](https://bugzilla.redhat.com/show_bug.cgi?id=1971791) |
| python-azure-mgmt-containerregistry | 🟡 | [RH BZ 1971792](https://bugzilla.redhat.com/show_bug.cgi?id=1971792) |
| python-azure-mgmt-containerservice | 🟡 | [RH BZ 1971793](https://bugzilla.redhat.com/show_bug.cgi?id=1971793) |
| python-azure-mgmt-core | 🟡 | [RH BZ 1971794](https://bugzilla.redhat.com/show_bug.cgi?id=1971794) |
| python-azure-mgmt-cosmosdb | 🟡 | [RH BZ 1971795](https://bugzilla.redhat.com/show_bug.cgi?id=1971795) |
| python-azure-mgmt-databoxedge | 🟡 | [RH BZ 1971796](https://bugzilla.redhat.com/show_bug.cgi?id=1971796) |
| python-azure-mgmt-datalake-analytics | 🟡 | [RH BZ 1971797](https://bugzilla.redhat.com/show_bug.cgi?id=1971797) |
| python-azure-mgmt-datalake-store | 🟡 | [RH BZ 1971798](https://bugzilla.redhat.com/show_bug.cgi?id=1971798) |
| python-azure-mgmt-datamigration | 🟡 | [RH BZ 1971799](https://bugzilla.redhat.com/show_bug.cgi?id=1971799) |
| python-azure-mgmt-deploymentmanager | 🟡 | [RH BZ 1971800](https://bugzilla.redhat.com/show_bug.cgi?id=1971800) |
| python-azure-mgmt-devtestlabs | ⚫ | |
| python-azure-mgmt-dns | ⚫ | |
| python-azure-mgmt-eventgrid | ⚫ | |
| python-azure-mgmt-eventhub | ⚫ | |
| python-azure-mgmt-hdinsight | ⚫ | |
| python-azure-mgmt-imagebuilder | ⚫ | |
| python-azure-mgmt-iotcentral | ⚫ | |
| python-azure-mgmt-iothubprovisioningservices | ⚫ | |
| python-azure-mgmt-iothub | ⚫ | |
| python-azure-mgmt-keyvault | ⚫ | |
| python-azure-mgmt-kusto | ⚫ | |
| python-azure-mgmt-loganalytics | ⚫ | |
| python-azure-mgmt-managedservices | ⚫ | |
| python-azure-mgmt-managementgroups | ⚫ | |
| python-azure-mgmt-maps | ⚫ | |
| python-azure-mgmt-marketplaceordering | ⚫ | |
| python-azure-mgmt-media | ⚫ | |
| python-azure-mgmt-monitor | ⚫ | |
| python-azure-mgmt-msi | ⚫ | |
| python-azure-mgmt-netapp | ⚫ | |
| python-azure-mgmt-network | ⚫ | |
| python-azure-mgmt-policyinsights | ⚫ | |
| python-azure-mgmt-privatedns | ⚫ | |
| python-azure-mgmt-rdbms | ⚫ | |
| python-azure-mgmt-recoveryservicesbackup | ⚫ | |
| python-azure-mgmt-recoveryservices | ⚫ | |
| python-azure-mgmt-redhatopenshift | ⚫ | |
| python-azure-mgmt-redis | ⚫ | |
| python-azure-mgmt-relay | ⚫ | |
| python-azure-mgmt-reservations | ⚫ | |
| python-azure-mgmt-resource | ⚫ | |
| python-azure-mgmt-search | ⚫ | |
| python-azure-mgmt-security | ⚫ | |
| python-azure-mgmt-servicebus | ⚫ | |
| python-azure-mgmt-servicefabricmanagedclusters | ⚫ | |
| python-azure-mgmt-servicefabric | ⚫ | |
| python-azure-mgmt-signalr | ⚫ | |
| python-azure-mgmt-sql | ⚫ | |
| python-azure-mgmt-sqlvirtualmachine | ⚫ | |
| python-azure-mgmt-storage | ⚫ | |
| python-azure-mgmt-synapse | ⚫ | |
| python-azure-mgmt-trafficmanager | ⚫ | |
| python-azure-mgmt-web | ⚫ | |
| python-azure-multiapi-storage | ⚫ | |
| python-azure-sdk-tools | ⚫ | |
| python-azure-storage-common | 🔵 | [RH BZ 1970638](https://bugzilla.redhat.com/show_bug.cgi?id=1970638) |
| python-azure-synapse-accesscontrol | ⚫ | |
| python-azure-synapse-artifacts | ⚫ | |
| python-azure-synapse-spark | ⚫ | |
| python-fabric | 🟢 | |
| python-javaproperties | 🟢 | |
| python-jsondiff | 🟢  | |
| python-knack | 🟢 | |
| python-vsts-cd-manager | 🟢 | |
| python-vsts | 🟢 | |

## Legend:

* ⚫ Not started
* 🟡 Package in review
* 🔵 Approved and awaiting builds
* 🟢 Fully packaged
