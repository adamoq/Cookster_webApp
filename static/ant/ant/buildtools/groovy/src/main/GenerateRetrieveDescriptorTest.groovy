import util.AntWrapper
import util.ConnectionInfo
import retriever.EnvironmentInfo
import util.FilterSet
import util.InstalledPackageFilterSet
import retriever.Retriever
import util.MetadataType
import util.MetadataTypes

import java.util.regex.Pattern

//Initialize
String userName = "uwe.voellger@cloudfirstdevopsstack.accenture.com"
String password = "MZRmpXBJ8ovtE5gpuAWRke68P0IXtWiLtLgY"
String serverurl = "https://login.salesforce.com"
String apiversion = "41.0"
String targetDir = "C:/Projects/General/asfbtools/temp/retrieve_all"
String tempDir = "C:/Projects/General/asfbtools/temp/retrieve_all_temp"
String forceExecutable = "C:/Projects/General/asfbtools/bin/Force.exe"

ConnectionInfo connectionInfo = new ConnectionInfo(userName,
                                                   password,
                                                   serverurl,
                                                   apiversion);
EnvironmentInfo environmentInfo = new EnvironmentInfo(targetDir,
                                                      tempDir,
                                                      forceExecutable)

AntWrapper antWrapper = new AntWrapper();

Filter filter = new Filter(Filter.CreateFor.RETRIEVE)
filter.metadataFilter.skipInstalledPackages = true
filter.addFilter()

//if ( true ) {
//    InstalledPackageFilterSet installedPackageFilterSet = new InstalledPackageFilterSet()
//    if ( true ) {
//        List toKeep = new ArrayList()
//        List toSkip = new ArrayList()
//        toKeep.add(Pattern.compile(/^.*?\.ACCLStableBeta__A.*?$/))
//        //toSkip.add(Pattern.compile(/^.*?\.ACCLStableBeta__Active__c?$/))
//        installedPackageFilterSet.fullNamesFilterSet.put("CustomField", new FilterSet(toKeep, toSkip))
//    }
//    filter.metadataFilter.installedPackagesFilterSet.put("ACCLStableBeta", installedPackageFilterSet)
//}

//if (true) {
//    List toKeep = null;
//    List toSkip = new ArrayList();
//    toSkip.add(Pattern.compile(/^components\/Site.*\.component$/))
//    filter.metadataFilter.fileNamesFilterSet.put("ApexComponent", new FilterSet(toKeep, toSkip))
//}

//if (true) {
//    List toKeep = null;
//    List toSkip = null;
//    metadataFilter.fullNamesFilterSet.put("CustomField", new FilterSet(toKeep, toSkip))
//}

//Retrieve
Retriever retriever = new Retriever()
MetadataTypes metadataTypes = retriever.retrieve(connectionInfo, environmentInfo, antWrapper, filter.metadataFilter)

//Write package.xml
metadataTypes.writePackageXMLs(connectionInfo, environmentInfo, antWrapper)

//Output
println "Result contains " + metadataTypes.xmlName2MetadataType.size() + " metadata types"
for ( String xmlName : metadataTypes.xmlName2MetadataType.keySet() ) {
    MetadataType metadataType = metadataTypes.xmlName2MetadataType.get(xmlName)
    println "  Found " + metadataType.fullName2MetadataDetails.size() + " " + xmlName + " metadata details:"
    for ( String fullName : metadataType.fullName2MetadataDetails.keySet() ) {
        println "    " + fullName
    }
}
