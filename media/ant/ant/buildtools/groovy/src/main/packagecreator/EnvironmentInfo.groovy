package packagecreator

/**
 * Environment information like pathes
 */
public class EnvironmentInfo {
    public String srcDir = null
    public String targetDir = null
    public String tempDir
    public String versions = null
    public String gitExecutable

    /**
     * Constructor
     * @param srcDir
     * @param targetDir
     * @param tempDir
     * @param versions
     */
    public EnvironmentInfo(String srcDir,
                           String targetDir,
                           String tempDir,
                           String versions,
                           String gitExecutable) {
        this.srcDir = srcDir
        this.targetDir = targetDir
        this.tempDir = tempDir
        this.versions = versions
        this.gitExecutable = gitExecutable
    }
}
