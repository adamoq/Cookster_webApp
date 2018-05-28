package util;

/**
 * Class to run a command line
 */
public class CommandRunner {

    public static final String ERROR = "Error"

    /**
     * Run a command in the operation system command prompt
     * @param baseDir
     * @param command
     * @return the output of the command
     */
    public static String runCommand(String baseDir, String command){

        /*String cmd = ""
        command.split('"').each {
            if (it.trim() != "") { cmd += it.trim(); }
        }*/
        String cmd = command

        //println "Running command " + cmd

        try {
            def proc = cmd.execute(null, new File(baseDir))

            //Any error message?
            StreamGobbler errorGobbler = new StreamGobbler(proc.getErrorStream(), "ERROR")

            //Any output?
            StreamGobbler outputGobbler = new StreamGobbler(proc.getInputStream(), "OUTPUT")

            //Kick them off
            errorGobbler.start();
            outputGobbler.start();

            //Any error???
            int exitVal = proc.waitFor();
            errorGobbler.join();
            outputGobbler.join();
            def output = outputGobbler.buffer
            def error = errorGobbler.buffer
            
            //println "Output: " + output
            //println "Error: " + error

            return output
        }
        catch (Throwable t) {
            t.printStackTrace();
            return ERROR
        }
    }
}
