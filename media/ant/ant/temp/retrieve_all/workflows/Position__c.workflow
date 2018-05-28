<?xml version="1.0" encoding="UTF-8"?>
<Workflow xmlns="http://soap.sforce.com/2006/04/metadata">
    <alerts>
        <fullName>Email_to_Position_Owner_then_there_are_no_Interviewers</fullName>
        <description>Email to Position Owner then there are no Interviewers</description>
        <protected>false</protected>
        <recipients>
            <type>owner</type>
        </recipients>
        <senderType>CurrentUser</senderType>
        <template>Workflow_Email_Templates/PositionwithnoInterviewers</template>
    </alerts>
    <fieldUpdates>
        <fullName>Assign_New_Position_to_Recruiter_Queue</fullName>
        <field>OwnerId</field>
        <lookupValue>Recruiter_Queue</lookupValue>
        <lookupValueType>Queue</lookupValueType>
        <name>Assign New Position to Recruiter Queue</name>
        <notifyAssignee>true</notifyAssignee>
        <operation>LookupValue</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Date_Opened_to_Today</fullName>
        <field>Data_Opened__c</field>
        <formula>NOW()</formula>
        <name>Date Opened to Today</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Formula</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Owner_to_Recruiter_Queue_on_Approval</fullName>
        <field>OwnerId</field>
        <lookupValue>Recruiter_Queue</lookupValue>
        <lookupValueType>Queue</lookupValueType>
        <name>Owner to Recruiter Queue on Approval</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>LookupValue</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Status_to_Closed_on_Not_Approved</fullName>
        <field>Status__c</field>
        <literalValue>Closed</literalValue>
        <name>Status to Closed on Not Approved</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Literal</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Status_to_Open_on_Approval</fullName>
        <field>Status__c</field>
        <literalValue>Open</literalValue>
        <name>Status to Open on Approval</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Literal</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Sub_status_for_Position_in_Progress</fullName>
        <field>Sub_Status__c</field>
        <literalValue>Pending</literalValue>
        <name>Sub-status for Position in Progress</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Literal</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Sub_status_to_Approved_on_Approval</fullName>
        <field>Sub_Status__c</field>
        <literalValue>Approved</literalValue>
        <name>Sub-status to Approved on Approval</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Literal</operation>
        <protected>false</protected>
    </fieldUpdates>
    <fieldUpdates>
        <fullName>Sub_status_to_Not_Approved_on_Reject</fullName>
        <field>Sub_Status__c</field>
        <literalValue>Not Approved</literalValue>
        <name>Sub-status to Not Approved on Reject</name>
        <notifyAssignee>false</notifyAssignee>
        <operation>Literal</operation>
        <protected>false</protected>
    </fieldUpdates>
    <rules>
        <fullName>New Position Rule</fullName>
        <actions>
            <name>Assign_New_Position_to_Recruiter_Queue</name>
            <type>FieldUpdate</type>
        </actions>
        <active>true</active>
        <criteriaItems>
            <field>Position__c.Status__c</field>
            <operation>equals</operation>
            <value>New</value>
        </criteriaItems>
        <triggerType>onCreateOnly</triggerType>
    </rules>
    <rules>
        <fullName>Position has no Interviewers</fullName>
        <active>true</active>
        <criteriaItems>
            <field>Position__c.Number_of_Interviewers__c</field>
            <operation>equals</operation>
            <value>0</value>
        </criteriaItems>
        <triggerType>onCreateOrTriggeringUpdate</triggerType>
        <workflowTimeTriggers>
            <actions>
                <name>Email_to_Position_Owner_then_there_are_no_Interviewers</name>
                <type>Alert</type>
            </actions>
            <timeLength>30</timeLength>
            <workflowTimeTriggerUnit>Days</workflowTimeTriggerUnit>
        </workflowTimeTriggers>
    </rules>
</Workflow>
