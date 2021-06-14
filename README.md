# Azure CLI/SDK RPM packaging

This is a tracker for getting the Azure CLI and SDK packaged in Fedora.

## Package status

| Package | Status | Notes |
| ------- | ------ | ----- |
| azure-cli | ⚫ | |
| python-applicationinsights | ⚫ | Not needed if `python-azure-cli-telemetry` is skipped |
| python-azure-appconfiguration | ⚫ | |
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
| python-azure-keyvault-keys | ⚫ | |
| python-azure-keyvault-secrets | ⚫ | |
| python-azure-keyvault | ⚫ | |
| python-azure-loganalytics | ⚫ | |
| python-azure-mgmt-advisor | ⚫ | |
| python-azure-mgmt-apimanagement | ⚫ | |
| python-azure-mgmt-appconfiguration | ⚫ | |
| python-azure-mgmt-applicationinsights | ⚫ | |
| python-azure-mgmt-authorization | ⚫ | |
| python-azure-mgmt-batchai | ⚫ | |
| python-azure-mgmt-batch | ⚫ | |
| python-azure-mgmt-billing | ⚫ | |
| python-azure-mgmt-botservice | ⚫ | |
| python-azure-mgmt-cdn | ⚫ | |
| python-azure-mgmt-cognitiveservices | ⚫ | |
| python-azure-mgmt-compute | ⚫ | |
| python-azure-mgmt-consumption | ⚫ | |
| python-azure-mgmt-containerinstance | ⚫ | |
| python-azure-mgmt-containerregistry | ⚫ | |
| python-azure-mgmt-containerservice | ⚫ | |
| python-azure-mgmt-core | ⚫ | |
| python-azure-mgmt-cosmosdb | ⚫ | |
| python-azure-mgmt-databoxedge | ⚫ | |
| python-azure-mgmt-datalake-analytics | ⚫ | |
| python-azure-mgmt-datalake-store | ⚫ | |
| python-azure-mgmt-datamigration | ⚫ | |
| python-azure-mgmt-deploymentmanager | ⚫ | |
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
