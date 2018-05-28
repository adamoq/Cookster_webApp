import junit.framework.Test
import junit.textui.TestRunner
import packagecreator.EnvironmentInfo
import util.FilterSet
import util.InstalledPackageFilterSet
import util.MetadataDetail

import java.util.regex.Pattern

public class FilterSetTest extends GroovyTestCase  {

    void testFilternNullNull() {
        List toKeep = null;
        List toSkip = null;
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert false == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilterNull0() {
        List toKeep = null;
        List toSkip = new ArrayList();
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert false == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilterNullx() {
        List toKeep = null;
        List toSkip = new ArrayList();
        toSkip.add(Pattern.compile(/^dashboards\/Skip_Dashboards-meta\.xml$/))
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false  == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert true   == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFiltern0Null() {
        List toKeep = new ArrayList();
        List toSkip = null;
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert false == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilter00() {
        List toKeep = new ArrayList();
        List toSkip = new ArrayList();
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert false == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilter0x() {
        List toKeep = new ArrayList();
        List toSkip = new ArrayList();
        toSkip.add(Pattern.compile(/^dashboards\/Skip_Dashboards-meta\.xml$/))
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert true == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilternxNull() {
        List toKeep = new ArrayList();
        toKeep.add(Pattern.compile(/^dashboards\/Keep_Dashboards-meta\.xml$/))
        List toSkip = null;
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert true  == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilterx0() {
        List toKeep = new ArrayList();
        toKeep.add(Pattern.compile(/^dashboards\/Keep_Dashboards-meta\.xml$/))
        List toSkip = new ArrayList();
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert true  == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
    }

    void testFilterxx() {
        List toKeep = new ArrayList();
        toKeep.add(Pattern.compile(/^dashboards\/Keep_Dashboards-meta\.xml$/))
        toKeep.add(Pattern.compile(/^dashboards\/TwiceConfigured_Dashboard-meta\.xml$/))
        List toSkip = new ArrayList();
        toSkip.add(Pattern.compile(/^dashboards\/Skip_Dashboardss-meta\.xml$/))
        toSkip.add(Pattern.compile(/^dashboards\/TwiceConfigured_Dashboard-meta\.xml$/))
        FilterSet filterSet = new FilterSet(toKeep, toSkip)
        assert false == filterSet.filter("dashboards/Keep_Dashboards-meta.xml")
        assert true  == filterSet.filter("dashboards/Skip_Dashboards-meta.xml")
        assert true == filterSet.filter("dashboards/Unconfigure_Dashboard-meta.xml")
        assert true == filterSet.filter("dashboards/TwiceConfigured_Dashboard-meta.xml")
    }
}

public class InstalledPackageFilterSetTest extends GroovyTestCase  {

    void testFilterKeep() {
        InstalledPackageFilterSet filterSet = new InstalledPackageFilterSet()
        if ( true ) {
            List toKeep = new ArrayList()
            List toSkip = new ArrayList()
            toKeep.add(Pattern.compile(/^.*?\.Keep_ManagedPackage__.*?$/))
            //toSkip.add(Pattern.compile(/^.*?\.ACCLStableBeta__Active__c?$/))
            filterSet.fullNamesFilterSet.put("CustomField", new FilterSet(toKeep, toSkip))
        }

        if (true ) {
            MetadataDetail metadataDetail = new MetadataDetail("CustomField",
                                                               null,
                                                               "objects/Test.object",
                                                               "Account.Keep_ManagedPackage__StandardField",
                                                               null,
                                                               null,
                                                               null,
                                                               null,
                                                               null)
            assert false  == filterSet.filter(metadataDetail)
        }
        if (true ) {
            MetadataDetail metadataDetail = new MetadataDetail("CustomField",
                                                               null,
                                                               "objects/Test.object",
                                                               "Account.Keep_ManagedPackage__CustomField__c",
                                                               null,
                                                               null,
                                                               null,
                                                               null,
                                                               null)
            assert false  == filterSet.filter(metadataDetail)
        }
        if (true ) {
            MetadataDetail metadataDetail = new MetadataDetail("CustomField",
                                                               null,
                                                               "objects/Test.object",
                                                               "Test.Skip_ManagedPackage__StandardField",
                                                               null,
                                                               null,
                                                               null,
                                                               null,
                                                               null)
            assert true  == filterSet.filter(metadataDetail)
        }
        if (true ) {
            MetadataDetail metadataDetail = new MetadataDetail("CustomField",
                                                               null,
                                                               "objects/Test.object",
                                                               "Account.Skip_ManagedPackage__CustomField__c",
                                                               null,
                                                               null,
                                                               null,
                                                               null,
                                                               null)
            assert true  == filterSet.filter(metadataDetail)
        }
    }
}

public class DummyTest extends GroovyTestCase {

    void testD1() {
        EnvironmentInfo environmentInfo = new EnvironmentInfo("C:/Projects/PMI/MasInt1/src",
                "C:/Projects/asfltools/temp/deploy_delta",
                "312917068b388e7458103ab46f7cfc967dc4f2d8 432c5792fa862010235944fe2a08af20650dec9c",
                "C:/Users/uwe.voellger/AppData/Local/Programs/Git/bin/git.exe")
        String source = "C:\\Projects\\PMI\\MasInt1\\src\\reports\\DTE_Reports\\All_Customer_Community_Users_new1.report"
        if (source =~ /documents[\\\/]/ ||
            source =~ /dashboards[\\\/]/ ||
            source =~ /email[\\\/]/ ||
            source =~ /reports[\\\/]/){
            File f1 = new File(source).getParentFile()
            String folderName = f1.getName()
            File f2 = f1.getParentFile()
            String typeFolderName = f2.getName()
            String folderDescriptor = environmentInfo.srcDir + "/" + typeFolderName + "/" + folderName + "-meta.xml"
            String folder = environmentInfo.targetDir + "/" + typeFolderName
            if( new File(folderDescriptor).exists() ) {
                println "Copy folder descriptor " + folderDescriptor + " to " + folder
            }
            else {
                println "Missing folder descriptor ${folderDescriptor}"
            }
        }
    }
}

public class AllTests {
   static Test suite() {
      def allTests = new GroovyTestSuite()
      allTests.addTestSuite(FilterSetTest.class)
      allTests.addTestSuite(InstalledPackageFilterSetTest.class)
      allTests.addTestSuite(DummyTest.class)
      return allTests
   }
}

TestRunner.run(AllTests.suite())