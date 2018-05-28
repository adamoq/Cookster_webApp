import util.AntWrapper
import util.ConnectionInfo
import retriever.EnvironmentInfo
import util.FilterSet
import util.InstalledPackageFilterSet
import retriever.Retriever
import util.MetadataTypes

import java.util.regex.Pattern

//Initialize
String userName = "${properties['sf.username']}"
String password = "${properties['sf.password']}"
String serverurl = "${properties['sf.serverurl']}"
String apiversion = "${properties['sf.apiversion']}"
String targetDir = "${properties['component.backup.folder']}"
String tempDir = "${properties['component.backup.temp']}"
String forceExecutable = "${properties['force.executable']}"
String packageName = "${properties['sf.backup.installedpackage']}"

ConnectionInfo connectionInfo = new ConnectionInfo(userName,
												   password,
												   serverurl,
												   apiversion);
EnvironmentInfo environmentInfo = new EnvironmentInfo(targetDir,
													  tempDir,
													  forceExecutable)
AntWrapper antWrapper = new AntWrapper();

Filter filter = new Filter(Filter.CreateFor.RETRIEVE)
//filter.metadataFilter.skipInstalledPackages = true
filter.addFilter(packageName)

//For backup purposes, add filter for all parts of the managed package
InstalledPackageFilterSet installedPackageFilterSet = new InstalledPackageFilterSet()
if ( true ) {
	List toKeep = new ArrayList()
	List toSkip = null
	toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
	installedPackageFilterSet.fullNamesFilterSet.put("*", new FilterSet(toKeep, toSkip))
}
filter.metadataFilter.installedPackagesFilterSet.put(packageName, installedPackageFilterSet)

//Retrieve
Retriever retriever = new Retriever()
MetadataTypes metadataTypes = retriever.retrieve(connectionInfo, environmentInfo, antWrapper, metadataFilter)
println "Found " + metadataTypes.xmlName2MetadataType.size() + "  metadata types"

//Write package.xml
metadataTypes.writePackageXMLs(connectionInfo, environmentInfo, antWrapper)
