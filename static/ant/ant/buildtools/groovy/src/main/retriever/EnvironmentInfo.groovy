package retriever

/**
 * Environment information like pathes
 */
public class EnvironmentInfo {
    public String targetDir
    public String tempDir
    public String forceExecutable

    /**
     * Constructor
     * @param targetDir
     * @param tempDir
     * @param forceExecutable
     */
    public EnvironmentInfo(String targetDir,
                           String tempDir,
                           String forceExecutable) {
        this.targetDir = targetDir
        this.tempDir = tempDir
        this.forceExecutable = forceExecutable;
    }
}
