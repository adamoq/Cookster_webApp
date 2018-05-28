import util.FilterSet
import util.MetadataFilter

import java.util.regex.Pattern

/**
 * A class that provides the filter used for retrieving and deploying metadata from/to a Salesforce org.
 */
public class Filter {
    /**
     * Possible values for the purpose of the filter
     * <ul>
     *     <li>RETRIEVE</li>
     *     <li>DEPLOY</li>
     * </ul>
     */
    enum CreateFor{
        RETRIEVE,
        DEPLOY
    }

    /**
     * The purpose of the filter.
     * Defaults to CreateFor.RETRIEVE.
     */
    public CreateFor createFor = CreateFor.RETRIEVE;

    /**
     * Metadata types filter set.
     * Use the XML names, like
     * <ul>
     * <li>ApexClass</li>
     * <li>CustomObject</li>
     * </ul>
     */
    public MetadataFilter metadataFilter = null

    /**
     * Default constructor
     */
    public Filter() {
        metadataFilter = new MetadataFilter()
    }

    /**
     * Default constructor
     * @param createFor
     */
    public Filter(CreateFor createFor) {
        this();
        this.createFor = createFor;
    }

    /**
     * Adds default filters (based on metadata type, managed packages and file names)
     */
    public void addFilter() {
        addMetadataTypeFilter()
        addManagedPackageFilter(null)
        addFileNameFilter()
    }

    /**
     * Adds default filters (based on metadata type, managed packages and file names)
     * @param packageName Name of a managed package, can be null
     */
    public void addFilter(String packageName) {
        addMetadataTypeFilter()
        addManagedPackageFilter(packageName)
        addFileNameFilter()
    }

    /**
     * Filters out all metadata which do not belong to some specified types.
     * Useful for test purposes.
     */
    private void addMetadataTypeFilter() {
        //List toKeep = new ArrayList()
        //List toSkip = new ArrayList()
        //metadataFilter.metadataTypesFilterSet = new FilterSet(toKeep, toSkip)
    }

    /**
     * Specifies filter for managed packages.
     * @param packageName
     */
    private void addManagedPackageFilter(String packageName) {
        //if ( "ACCL".equals(packageName) ) {
        //    InstalledPackageFilterSet installedPackageFilterSet = new InstalledPackageFilterSet()
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("ApexPage", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("ApprovalProcess", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomApplication", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^.*?\.${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomField", new FilterSet(toKeep, toSkip))
        //    }
        //
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomObject", new FilterSet(toKeep, toSkip))
        //    }
        //
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__Order_Template__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Call__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Call_Attachment__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Call_Template__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Account_Extension__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Account_Call_Setting__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Account_Manager__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Account_Template__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Job_Definition_List__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Job_Definition_List_Template__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Order_Item__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Org_Unit__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Org_Unit_User__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Sales_Organization__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Tactic_Template__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Unit_of_Measure__c.*\.objectTranslation$/))
        //        toKeep.add(Pattern.compile(/^${packageName}__Workflow_State_Transition__c.*\.objectTranslation$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomObjectTranslation", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomPermission", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("CustomTab", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^.*?\.${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("FieldSet", new FilterSet(toKeep, toSkip))
        //    }
        //    //bcs this globalpicklist can not be deployed if ( true ) {
        //    //    List toKeep = new ArrayList()
        //    //    List toSkip = null
        //    //    toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //    //    installedPackageFilterSet.fullNamesFilterSet.put("GlobalValueSet", new FilterSet(toKeep, toSkip))
        //    //}
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        toKeep.add(Pattern.compile(/^.*?-${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("Layout", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("StaticResource", new FilterSet(toKeep, toSkip))
        //    }
        //    if ( true ) {
        //        List toKeep = new ArrayList()
        //        List toSkip = null
        //        toKeep.add(Pattern.compile(/^.*?\.${packageName}__.*?$/))
        //        installedPackageFilterSet.fullNamesFilterSet.put("ValidationRule", new FilterSet(toKeep, toSkip))
        //    }
        //    metadataFilter.installedPackagesFilterSet.put(packageName, installedPackageFilterSet)
        //}
    }

    /**
     * Add file name filters
     */
    private void addFileNameFilter() {
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ActionLinkGroupTemplate", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("AnalyticSnapshot", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^classes\/ConcurrentSessionsPolicyCondition.*?$/))
            toSkip.add(Pattern.compile(/^classes\/DataLoaderLeadExportCondition.*?$/))
            toSkip.add(Pattern.compile(/^classes\/FIELO_RESTBurningCodeServiceAPI.*?$/))
            toSkip.add(Pattern.compile(/^classes\/FIELO_RESTBurningCodeServiceAPITest.*?$/))
            toSkip.add(Pattern.compile(/^classes\/FIELO_RESTMessageAPI.*?$/))
            toSkip.add(Pattern.compile(/^classes\/FIELO_RESTPromotionServiceAPI.*?$/))
            toSkip.add(Pattern.compile(/^classes\/FIELO_RESTPromotionServiceAPITest.*?$/))
            metadataFilter.fileNamesFilterSet.put("ApexClass", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^components\/Site.*\.component$/))
            metadataFilter.fileNamesFilterSet.put("ApexComponent", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ApexPage", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ApexTestSuite", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ApexTrigger", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("AppMenu", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^approvalProcesses\/CCR_KnowledgeArticle__kav\.CCR_NewArticlesForApprovalKnowledgeArtic\.approvalProcess$/))
            toKeep.add(Pattern.compile(/^approvalProcesses\/CCR_MkTPromotions__kav\.CCR_NewArticlesForApprovalActivities\.approvalProcess$/))
            toKeep.add(Pattern.compile(/^approvalProcesses\/CCR_MkTPromotions__kav\.CCR_NewArticlesForApprovalMkTPromotion\.approvalProcess$/))
            toKeep.add(Pattern.compile(/^approvalProcesses\/FIELO_SalesPromotion__c\.Fielo_SalesPromotion_Approval\.approvalProcess$/))
            metadataFilter.fileNamesFilterSet.put("ApprovalProcess", new FilterSet(toKeep, toSkip))
        }
        //Configuration: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^.*$/))
            metadataFilter.fullNamesFilterSet.put("AssignmentRule", new FilterSet(toKeep, toSkip))
        }
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^assignmentRules\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("AssignmentRules", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("AssistantRecommendationType", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("AuraDefinitionBundle", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("AuthProvider", new FilterSet(toKeep, toSkip))
        //}
        //Configuration: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^.*$/))
            metadataFilter.fullNamesFilterSet.put("AutoResponseRule", new FilterSet(toKeep, toSkip))
        }
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^autoResponseRules\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("AutoResponseRules", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("BrandingSet", new FilterSet(toKeep, toSkip))
        //}
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("BusinessProcess", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CallCenter", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CaseSubjectParticle", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^certs\/*.*$/))
            metadataFilter.fileNamesFilterSet.put("Certificate", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ChannelLayout", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ChatterExtension", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^cleanDataServices\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CleanDataService", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^communities\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Community", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^communityTemplateDefinitions\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CommunityTemplateDefinition", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^communityThemeDefinitions\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CommunityThemeDefinition", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("CompactLayout", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (CreateFor.RETRIEVE == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^connectedApps\/REST_API_CONNECT\.connectedApp$/))
            toSkip.add(Pattern.compile(/^connectedApps\/Postman\.connectedApp$/))
            metadataFilter.fileNamesFilterSet.put("ConnectedApp", new FilterSet(toKeep, toSkip))
        }
        else
        if (CreateFor.DEPLOY == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^connectedApps\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("ConnectedApp", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^contentassets\/.*?/))
            metadataFilter.fileNamesFilterSet.put("ContentAsset", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CorsWhitelistOrigin", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^cspTrustedSites\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CspTrustedSite", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^applications\/standard__AppLauncher\.app$/))
            metadataFilter.fileNamesFilterSet.put("CustomApplication", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomApplicationComponent", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomFeedFilter", new FilterSet(toKeep, toSkip))
        //}
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("CustomField", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomLabel", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^customMetadata\/CAA.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_Country_Phone_Patterns.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_IframeEncryptionData.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_Languages.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_MarketProfileNumbers.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_Permission_set_Names.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_SelfRegistration.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTE_Video23_Key.*\.md$/))
            toSkip.add(Pattern.compile(/^customMetadata\/DTERRP_WidgetOrderOfFileds\.MY_Email\.md$/))
            metadataFilter.fileNamesFilterSet.put("CustomMetadata", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^objects\/KnowledgeArticleVersion\.object$/))
            toSkip.add(Pattern.compile(/^objects\/SocialPersona\.object$/))
            toSkip.add(Pattern.compile(/^objects\/UserProvisioningRequest\.object$/))
            metadataFilter.fileNamesFilterSet.put("CustomObject", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^objectTranslations\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CustomObjectTranslation", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomPageWebLink", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomPermission", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^sites\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("CustomSite", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("CustomTab", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^dashboards\/DTE_Dashboards\/.*\.dashboard$/))
            toKeep.add(Pattern.compile(/^dashboards\/DTE_Dashboards-meta\.xml$/))
            toKeep.add(Pattern.compile(/^dashboards\/DTE_Dashboards_FE\/Leads\.dashboard$/))
            toKeep.add(Pattern.compile(/^dashboards\/DTE_Dashboards_FE-meta\.xml$/))
            toKeep.add(Pattern.compile(/^dashboards\/Service_Dashboards\/CAA_Leads_Monitoring_Dashboard\.dashboard$/))
            toKeep.add(Pattern.compile(/^dashboards\/Service_Dashboards\/CCR_Call_Center_Dashboard\.dashboard$/))
            toKeep.add(Pattern.compile(/^dashboards\/Service_Dashboards-meta\.xml$/))
            toKeep.add(Pattern.compile(/^dashboards\/FIELO_Dashboards\/.*\.dashboard$/))
            toKeep.add(Pattern.compile(/^dashboards\/FIELO_Dashboards-meta\.xml$/))
            metadataFilter.fileNamesFilterSet.put("Dashboard", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^datacategorygroups\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("DataCategoryGroup", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^delegateGroups\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("DelegateGroup", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^documents\/Field_Observation_Tool\/FOT_Legal_Document\.pdf$/))
            toKeep.add(Pattern.compile(/^documents\/Field_Observation_Tool\/FOT_Legal_Document\.pdf-meta.xml$/))
            toKeep.add(Pattern.compile(/^documents\/Field_Observation_Tool-meta\.xml$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/CCR_DeviceDiagnostic\.pdf$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/CCR_DeviceDiagnostic\.pdf-meta.xml$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/DTE_OrderManagementInternalUserTemplateLetterHeadLogo\.png$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/DTE_OrderManagementInternalUserTemplateLetterHeadLogo\.png-meta.xml$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/Email_Template_PMI_Logo\.png$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/Email_Template_PMI_Logo\.png-meta.xml$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/PMI_Logo\.jpg$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments\/PMI_Logo\.jpg-meta.xml$/))
            toKeep.add(Pattern.compile(/^documents\/SharedDocuments-meta\.xml$/))
            metadataFilter.fileNamesFilterSet.put("Document", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("DuplicateRule", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EclairGeoData", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/Article_Notification\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/Article_Notification\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticelTempleForRejectionKnowledgeArticle\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticelTempleForRejectionKnowledgeArticle\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticelTempleForRejectionPromotions\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticelTempleForRejectionPromotions\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticleApprovalTemplateKnowledgeArticle\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticleApprovalTemplateKnowledgeArticle\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticleApprovalTemplatePromotions\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NewArticleApprovalTemplatePromotions\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForActivities\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForActivities\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForKnowledgeArticles\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForKnowledgeArticles\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForTalkingPoints\.email$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications\/CCR_NotificationForTalkingPoints\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Article_Notifications-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/CAA_Email_Templates\/.*\.email$/))
            toKeep.add(Pattern.compile(/^email\/CAA_Email_Templates\/.*\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_One_Device_Authorization\/DTE_One_Device_Example\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_One_Device_Authorization\/DTE_One_Device_Example\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_One_Device_Authorization-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Quiz_Notifications\/DTE_QuizExample_en_US.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Quiz_Notifications\/DTE_QuizExample_en_US.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Quiz_Notifications-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_ApprovalRequest\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_ApprovalRequest\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Approve_user\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Approve_user\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_Referer_Rejection\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_Referer_Rejection\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_Referer_successful_registration\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_Referer_successful_registration\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_shop_owner_about_pending_approval\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_shop_owner_about_pending_approval\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_user_about_proposal\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_user_about_proposal\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_user_about_reactivation\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration\/DTE_Inform_user_about_reactivation\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Self_Registration-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_StaffReview\/DTE_StaffReviewTemplate\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_StaffReview\/DTE_StaffReviewTemplate\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_StaffReview-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Survey_Notifications\/DTE_SurveyExample_en_US\.email$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Survey_Notifications\/DTE_SurveyExample_en_US\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/DTE_Survey_Notifications-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Field_Observation_Tool\/FOT_Notification\.email$/))
            toKeep.add(Pattern.compile(/^email\/Field_Observation_Tool\/FOT_Notification\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Field_Observation_Tool-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/FIELO_Templates\/.*\.email$/))
            toKeep.add(Pattern.compile(/^email\/FIELO_Templates\/.*\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/FIELO_Templates-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/My_Data\/DTE_MyData_UserName_Sample_Market_en_us\.email$/))
            toKeep.add(Pattern.compile(/^email\/My_Data\/DTE_MyData_UserName_Sample_Market_en_us\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/My_Data\/DTE_MyDataDefaultUserNameChangeTemplate\.email$/))
            toKeep.add(Pattern.compile(/^email\/My_Data\/DTE_MyDataDefaultUserNameChangeTemplate\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/My_Data-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_EmailTemplateForExternalUsersPrizeCatalog\.email$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_EmailTemplateForExternalUsersPrizeCatalog\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeCatalogInternalUserVFTemplate\.email$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeCatalogInternalUserVFTemplate\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeCatalogStockWarningExternalTemplate\.email$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeCatalogStockWarningExternalTemplate\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeStockWarningInternalVFTemplate\.email$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates\/DTE_PrizeStockWarningInternalVFTemplate\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Prize_Catalog_templates-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Task_Notifications\/DTE_TaskExample_en_US\.email$/))
            toKeep.add(Pattern.compile(/^email\/Task_Notifications\/DTE_TaskExample_en_US\.email-meta\.xml$/))
            toKeep.add(Pattern.compile(/^email\/Task_Notifications-meta\.xml$/))
            metadataFilter.fileNamesFilterSet.put("EmailTemplate", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EmbeddedServiceBranding", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EmbeddedServiceConfig", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EmbeddedServiceLiveAgent", new FilterSet(toKeep, toSkip))
        //}
        //Configuration: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^.*$/))
            metadataFilter.fullNamesFilterSet.put("EscalationRule", new FilterSet(toKeep, toSkip))
        }
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^escalationRules\/.*?/))
            metadataFilter.fileNamesFilterSet.put("EscalationRules", new FilterSet(toKeep, toSkip))
        }
        //Undefined
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EventDelivery", new FilterSet(toKeep, toSkip))
        //}
        //Undefined
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("EventSubscription", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ExternalDataSource", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("ExternalServiceRegistration", new FilterSet(toKeep, toSkip))
        //}
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("FieldSet", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^flexipages\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("FlexiPage", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^flows\/DTE_CommunityUserRegistrationConfirmation.*\.flow$/))
            toSkip.add(Pattern.compile(/^flows\/DTE_Send_Registrations_Rejection_Email_In_Proper_User_Languge.*\.flow$/))
            toSkip.add(Pattern.compile(/^flows\/LiveChat.*\.flow$/))
            metadataFilter.fileNamesFilterSet.put("Flow", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^flowDefinitions\/DTE_CommunityUserRegistrationConfirmation\.flowDefinition$/))
            toSkip.add(Pattern.compile(/^flowDefinitions\/DTE_Send_Registrations_Rejection_Email_In_Proper_User_Languge\.flowDefinition$/))
            toSkip.add(Pattern.compile(/^flowDefinitions\/LiveChat.*\.flowDefinition$/))
            metadataFilter.fileNamesFilterSet.put("FlowDefinition", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^globalValueSets\/DTE_ArticleNotificationTemplate\.globalValueSet$/))
            metadataFilter.fileNamesFilterSet.put("GlobalValueSet", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^globalValueSetTranslations\/.*\.globalValueSetTranslation$/))
            metadataFilter.fileNamesFilterSet.put("GlobalValueSetTranslation", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^groups\/DTE_GlobalGroup\.group$/))
            toSkip.add(Pattern.compile(/^groups\/DTE_GlobalPortalRole\.group$/))
            toSkip.add(Pattern.compile(/^groups\/DTE_Knowledge_Users\.group$/))
            metadataFilter.fileNamesFilterSet.put("Group", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("HomePageComponents", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("HomePageLayouts", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (CreateFor.RETRIEVE == createFor ) {
            //List toKeep = new ArrayList();
            //List toSkip = new ArrayList();
            //metadataFilter.fileNamesFilterSet.put("InstalledPackage", new FilterSet(toKeep, toSkip))
        }
        else
        if (CreateFor.DEPLOY == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^installedPackages\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("InstalledPackage", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^moderation\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("KeywordList", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^layouts\/AssetRelationship-Formato Relaci.n de activo\.layout$/)) //AssetRelationship-Formato Relación de activo.layout
            toSkip.add(Pattern.compile(/^layouts\/EmailMessage-Email Message Layout\.layout$/))
            //toSkip.add(Pattern.compile(/^layouts\/LiveAgentSession-Live Agent Session Layout\.layout$/))
            //toSkip.add(Pattern.compile(/^layouts\/LiveChatTranscript-Live Chat Transcript Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/LiveChatTranscriptActive-Live Chat Transcript.*Layout\.layout$/))
            //toSkip.add(Pattern.compile(/^layouts\/LiveChatTranscriptEvent-Live Chat Transcript Event Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/LiveChatTranscriptWaiting-Live Chat Transcript.*Layout\.layout$/))
            //toSkip.add(Pattern.compile(/^layouts\/LiveChatVisitor-Live Chat Visitor Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/SocialPersona-Social Persona Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/SocialPost-Social Post Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/UserProvAccount-User Provisioning Account Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/UserProvisioningLog-User Provisioning Log Layout\.layout$/))
            toSkip.add(Pattern.compile(/^layouts\/UserProvisioningRequest-User Provisioning Request Layout\.layout$/))
            metadataFilter.fileNamesFilterSet.put("Layout", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("LeadConvertSettings", new FilterSet(toKeep, toSkip))
        //}
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^letterhead\/Blue\.letter$/))
            toKeep.add(Pattern.compile(/^letterhead\/CCR_iQOSemailtemplate2\.letter$/))
            toKeep.add(Pattern.compile(/^letterhead\/CCR_White\.letter$/))
            toKeep.add(Pattern.compile(/^letterhead\/DTE_PrizeCatalogExternalUsersLetterHeadEmailTemplate\.letter$/))
            toKeep.add(Pattern.compile(/^letterhead\/PMI_Notification\.letter$/))
            metadataFilter.fileNamesFilterSet.put("Letterhead", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("ListView", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("LiveChatAgentConfig", new FilterSet(toKeep, toSkip))
        //}
        //Development (not yet deployed)
        if (CreateFor.RETRIEVE == createFor ) {
            //List toKeep = new ArrayList();
            //List toSkip = new ArrayList();
            //metadataFilter.fileNamesFilterSet.put("LiveChatButton", new FilterSet(toKeep, toSkip))
        }
        else
        if (CreateFor.DEPLOY == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^liveChatButtons\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("LiveChatButton", new FilterSet(toKeep, toSkip))
        }
        //Undefined
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("LiveChatDeployment", new FilterSet(toKeep, toSkip))
        //}
        //Undefined
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("LiveChatSensitiveDataRule", new FilterSet(toKeep, toSkip))
        //}
        //Configuration: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^.*?$/))
            metadataFilter.fullNamesFilterSet.put("ManagedTopic", new FilterSet(toKeep, toSkip))
        }
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^managedTopics\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("ManagedTopics", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fullNamesFilterSet.put("MatchingRule", new FilterSet(toKeep, toSkip))
        //}
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("MatchingRules", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^moderation\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("ModerationRule", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^namedCredentials\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("NamedCredential", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^networks\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Network", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^networkBranding\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("NetworkBranding", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^pathAssistants\/Default_Opportunity\.pathAssistant$/))
            metadataFilter.fileNamesFilterSet.put("PathAssistant", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    toSkip.add(Pattern.compile(/^permissionsets\/.*?$/))
        //    metadataFilter.fileNamesFilterSet.put("PermissionSet", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("PlatformCachePartition", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("PostTemplate", new FilterSet(toKeep, toSkip))
        //}
        //Development (not yet deployed)
        if (CreateFor.RETRIEVE == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^profiles\/live chat Profile\.profile$/))
            toSkip.add(Pattern.compile(/^profiles\/live chat Profile.*\.profile$/))
            metadataFilter.fileNamesFilterSet.put("Profile", new FilterSet(toKeep, toSkip))
        }
        else
        if (CreateFor.DEPLOY == createFor ) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^profiles\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Profile", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^profilePasswordPolicies\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("ProfilePasswordPolicy", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^profileSessionSettings\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("ProfileSessionSetting", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("Queue", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("QuickAction", new FilterSet(toKeep, toSkip))
        //}
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("RecordType", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^remoteSiteSettings\/CCR_.*\.remoteSite$/))
            toKeep.add(Pattern.compile(/^remoteSiteSettings\/fcm\.remoteSite$/))
            toKeep.add(Pattern.compile(/^remoteSiteSettings\/Video23\.remoteSite$/))
            metadataFilter.fileNamesFilterSet.put("RemoteSiteSetting", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^reports\/CA_Reports\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CA_Reports-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_AssetHistory\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_AssetHistory-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Call_Center_Agent_Availability\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Call_Center_Agent_Availability-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Contacts\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Contacts-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Financial_Department\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Financial_Department-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Logista_Report\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/CCR_Logista_Report-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/DTE_Reports\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/DTE_Reports-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/DTE_Reports_FE\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/DTE_Reports_FE-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/FIELO_Codes\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/FIELO_Codes-meta.xml$/))
            toKeep.add(Pattern.compile(/^reports\/Service_Dashboards_Reports\/.*\.report$/))
            toKeep.add(Pattern.compile(/^reports\/Service_Dashboards_Reports-meta.xml$/))
            metadataFilter.fileNamesFilterSet.put("Report", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^reportTypes\/ANNA_TEST\.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/Test.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/TEST_24_07_2017.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/Test_New_GR_24_07.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/Test_Report_with_Retailer_Fields.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/Test_Report_with_Retailer_Fields_Accounts.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/UA_test_report_types.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/UA_TEST_TASKS.reportType$/))
            toSkip.add(Pattern.compile(/^reportTypes\/ZA_JobDefinitionList_Task_Account.reportType$/))
            metadataFilter.fileNamesFilterSet.put("ReportType", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^roles\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Role", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^samlssoconfigs\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("SamlSsoConfig", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^scontrols\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Scontrol", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^settings\/Case.settings$/))
            toSkip.add(Pattern.compile(/^settings\/Security.settings$/))
            toSkip.add(Pattern.compile(/^settings\/Knowledge.settings$/))
            toSkip.add(Pattern.compile(/^settings\/PersonalJourney.settings$/))
            metadataFilter.fileNamesFilterSet.put("Settings", new FilterSet(toKeep, toSkip))
        }
        //Undefined: Does not work on file names filter!
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("SharingCriteriaRule", new FilterSet(toKeep, toSkip))
        //}
        //Undefined: Does not work on file names filter!
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("SharingOwnerRule", new FilterSet(toKeep, toSkip))
        //}
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("SharingReason", new FilterSet(toKeep, toSkip))
        }
        //Development
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("SharingRules", new FilterSet(toKeep, toSkip))
        //}
        //Undefined: Does not work on file names filter!
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("SharingTerritoryRule", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^siteDotComSites\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("SiteDotCom", new FilterSet(toKeep, toSkip))
        }
        //Undefined
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("Skill", new FilterSet(toKeep, toSkip))
        //}
        //Development
        //The value sets are not returned when describing this type.
        //Therefore the list of value sets to retrieve is added in the patch target.
        //if (true) {
        //    List toKeep = new ArrayList();
        //    List toSkip = new ArrayList();
        //    metadataFilter.fileNamesFilterSet.put("StandardValueSet", new FilterSet(toKeep, toSkip))
        //}
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^standardValueSetTranslations\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("StandardValueSetTranslation", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^staticresources\/DTECanadaCommunityLogo\.resource$/))
           // toSkip.add(Pattern.compile(/^staticresources\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("StaticResource", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^synonymDictionaries\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("SynonymDictionary", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toKeep.add(Pattern.compile(/^territories\/CCR_Disabled_Accounts\.territory$/))
            toKeep.add(Pattern.compile(/^territories\/CCR_France_territory\.territory$/))
            toKeep.add(Pattern.compile(/^territories\/CCR_Italy_Territory\.territory$/))
            toKeep.add(Pattern.compile(/^territories\/CCR_Koreaterritory\.territory$/))
            toKeep.add(Pattern.compile(/^territories\/CCR_Poland_territory\.territory$/))
            toKeep.add(Pattern.compile(/^territories\/CCR_Serbiaterritory\.territory$/))
            metadataFilter.fileNamesFilterSet.put("Territory", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^topicsForObjects\/ccrz.*?$/))
            metadataFilter.fileNamesFilterSet.put("TopicsForObjects", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^transactionSecurityPolicies\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("TransactionSecurityPolicy", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^translations\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("Translations", new FilterSet(toKeep, toSkip))
        }
        //Configuration
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^userCriteria\/.*?$/))
            metadataFilter.fileNamesFilterSet.put("UserCriteria", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("ValidationRule", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^KnowledgeArticleVersion\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            toSkip.add(Pattern.compile(/^UserProvisioningRequest\..*$/))
            metadataFilter.fullNamesFilterSet.put("WebLink", new FilterSet(toKeep, toSkip))
        }
        //Development
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^workflows\/DTE_UserRegistration__c\.workflow$/))
            toSkip.add(Pattern.compile(/^workflows\/Question\.workflow$/))
            toSkip.add(Pattern.compile(/^workflows\/Reply\.workflow$/))
            toSkip.add(Pattern.compile(/^workflows\/SocialPersona\.workflow$/))
            metadataFilter.fileNamesFilterSet.put("Workflow", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList()
            List toSkip = new ArrayList()
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowAlert", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowFieldUpdate", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowKnowledgePublish", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowOutboundMessage", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowSend", new FilterSet(toKeep, toSkip))
        }
        //Development: Does not work on file names filter!
        if (true) {
            List toKeep = new ArrayList();
            List toSkip = new ArrayList();
            toSkip.add(Pattern.compile(/^DTE_UserRegistration__c\..*$/))
            toSkip.add(Pattern.compile(/^Question\..*$/))
            toSkip.add(Pattern.compile(/^Reply\..*$/))
            toSkip.add(Pattern.compile(/^SocialPersona\..*$/))
            metadataFilter.fullNamesFilterSet.put("WorkflowTask", new FilterSet(toKeep, toSkip))
        }
    }
}
