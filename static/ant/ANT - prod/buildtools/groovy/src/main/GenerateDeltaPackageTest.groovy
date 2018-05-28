import packagecreator.EnvironmentInfo
import packagecreator.PackageCreator
import util.AntWrapper
import util.ConnectionInfo

//Initialize
String userName = "uwe.voellger@cloudfirstdevopsstack.accenture.com"
String password = "MZRmpXBJ8ovtE5gpuAWRke68P0IXtWiLtLgY"
String serverurl = "https://login.salesforce.com"
String apiversion = "41.0"
String srcDir = "C:/Projects/General/asfbtools/src"
String destDir = "C:/Projects/General/asfbtools/temp/deploy_delta"
String tempDir = "C:/Projects/General/asfbtools/temp"
//String versions = "0a1d395009d888b88702ff6647fe637e4bcbd951"
String versions = "5699aaf6cfb4f0f6b5d0d6911f0e1b465efe1319 8e86df5363ee722b2bf3456fe9b0092248c695a0"
String gitExecutable = "C:/Users/uwe.voellger/AppData/Local/Programs/Git/bin/git.exe"

ConnectionInfo connectionInfo = new ConnectionInfo(userName,
												   password,
												   serverurl,
												   apiversion);
EnvironmentInfo environmentInfo = new EnvironmentInfo(srcDir,
                                                      destDir,
                                                      tempDir,
                                                      versions,
                                                      gitExecutable)
AntWrapper antWrapper = new AntWrapper();

Filter filter = new Filter(Filter.CreateFor.DEPLOY)
filter.addFilter()

//Create delta deployment package
PackageCreator packageCreator = new PackageCreator()
packageCreator.createPackage(connectionInfo, environmentInfo, antWrapper, filter.metadataFilter)
