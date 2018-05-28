import packagecreator.EnvironmentInfo
import packagecreator.PackageCreator
import util.AntWrapper
import util.ConnectionInfo

//Initialize
String userName = "${properties['sf.username']}"
String password = "${properties['sf.password']}"
String serverurl = "${properties['sf.serverurl']}"
String apiversion = "${properties['sf.apiversion']}"
String srcDir = "${properties['component.src']}"
String destDir = "${properties['component.deploy_delta']}"
String tempDir = "${properties['component.temp_dir']}"
String versions = "${properties['git.versions']}"
String gitExecutable = "${properties['git.executable']}"

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
