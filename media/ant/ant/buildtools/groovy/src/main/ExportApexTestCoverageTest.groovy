import retriever.EnvironmentInfo
import util.ConnectionInfo
import util.ToolingAPIConnector

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

ToolingAPIConnector toolingAPIConnector = new ToolingAPIConnector(connectionInfo)
toolingAPIConnector.createConnection()
toolingAPIConnector.exportCodeCoverage("C:/Projects/General/asfbtools/temp/coverage.csv")
toolingAPIConnector.closeConnection()

