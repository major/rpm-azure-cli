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
| python-azure-mgmt-devtestlabs | 🟡 | [RH BZ 1971801](https://bugzilla.redhat.com/show_bug.cgi?id=1971801) |
| python-azure-mgmt-dns | 🟡 | [RH BZ 1971803](https://bugzilla.redhat.com/show_bug.cgi?id=1971803) |
| python-azure-mgmt-eventgrid | 🟡 | [RH BZ 1971804](https://bugzilla.redhat.com/show_bug.cgi?id=1971804) |
| python-azure-mgmt-eventhub | 🟡 | [RH BZ 1971805](https://bugzilla.redhat.com/show_bug.cgi?id=1971805) |
| python-azure-mgmt-hdinsight | 🟡 | [RH BZ 1971806](https://bugzilla.redhat.com/show_bug.cgi?id=1971806) |
| python-azure-mgmt-imagebuilder | 🟡 | [RH BZ 1971807](https://bugzilla.redhat.com/show_bug.cgi?id=1971807) |
| python-azure-mgmt-iotcentral | 🟡 | [RH BZ 1971811](https://bugzilla.redhat.com/show_bug.cgi?id=1971811) |
| python-azure-mgmt-iothubprovisioningservices | 🟡 | [RH BZ 1971813](https://bugzilla.redhat.com/show_bug.cgi?id=1971813) |
| python-azure-mgmt-iothub | 🟡 | [RH BZ 1971815](https://bugzilla.redhat.com/show_bug.cgi?id=1971815) |
| python-azure-mgmt-keyvault | 🟡 | [RH BZ 1971816](https://bugzilla.redhat.com/show_bug.cgi?id=1971816) |
| python-azure-mgmt-kusto | 🟡 | [RH BZ 1971818](https://bugzilla.redhat.com/show_bug.cgi?id=1971818) |
| python-azure-mgmt-loganalytics | 🟡 | [RH BZ 1971819](https://bugzilla.redhat.com/show_bug.cgi?id=1971819) |
| python-azure-mgmt-managedservices | 🟡 | [RH BZ 1971820](https://bugzilla.redhat.com/show_bug.cgi?id=1971820) |
| python-azure-mgmt-managementgroups | 🟡 | [RH BZ 1971822](https://bugzilla.redhat.com/show_bug.cgi?id=1971822) |
| python-azure-mgmt-maps | 🟡 | [RH BZ 1971824](https://bugzilla.redhat.com/show_bug.cgi?id=1971824) |
| python-azure-mgmt-marketplaceordering | 🟡 | [RH BZ 1971827](https://bugzilla.redhat.com/show_bug.cgi?id=1971827) |
| python-azure-mgmt-media | 🟡 | [RH BZ 1971831](https://bugzilla.redhat.com/show_bug.cgi?id=1971831) |
| python-azure-mgmt-monitor | 🟡 | [RH BZ 1971834](https://bugzilla.redhat.com/show_bug.cgi?id=1971834) |
| python-azure-mgmt-msi | 🟡 | [RH BZ 1971836](https://bugzilla.redhat.com/show_bug.cgi?id=1971836) |
| python-azure-mgmt-netapp | 🟡 | [RH BZ 1971837](https://bugzilla.redhat.com/show_bug.cgi?id=1971837) |
| python-azure-mgmt-network | 🟡 | [RH BZ 1971842](https://bugzilla.redhat.com/show_bug.cgi?id=1971842) |
| python-azure-mgmt-policyinsights | 🟡 | [RH BZ 1971843](https://bugzilla.redhat.com/show_bug.cgi?id=1971843) |
| python-azure-mgmt-privatedns | 🟡 | [RH BZ 1971844](https://bugzilla.redhat.com/show_bug.cgi?id=1971844) |
| python-azure-mgmt-rdbms | 🟡 | [RH BZ 1971845](https://bugzilla.redhat.com/show_bug.cgi?id=1971845) |
| python-azure-mgmt-recoveryservicesbackup | 🟡 | [RH BZ 1971846](https://bugzilla.redhat.com/show_bug.cgi?id=1971846) |
| python-azure-mgmt-recoveryservices | 🟡 | [RH BZ 1971847](https://bugzilla.redhat.com/show_bug.cgi?id=1971847) |
| python-azure-mgmt-redhatopenshift | 🟡 | [RH BZ 1971848](https://bugzilla.redhat.com/show_bug.cgi?id=1971848) |
| python-azure-mgmt-redis | 🟡 | [RH BZ 1971849](https://bugzilla.redhat.com/show_bug.cgi?id=1971849) |
| python-azure-mgmt-relay | 🟡 | [RH BZ 1971850](https://bugzilla.redhat.com/show_bug.cgi?id=1971850) |
| python-azure-mgmt-reservations | 🟡 | [RH BZ 1971851](https://bugzilla.redhat.com/show_bug.cgi?id=1971851) |
| python-azure-mgmt-resource | 🟡 | [RH BZ 1971852](https://bugzilla.redhat.com/show_bug.cgi?id=1971852) |
| python-azure-mgmt-search | 🟡 | [RH BZ 1971853](https://bugzilla.redhat.com/show_bug.cgi?id=1971853) |
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
