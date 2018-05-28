<?xml version="1.0" encoding="UTF-8"?>
<Workflow xmlns="http://soap.sforce.com/2006/04/metadata">
    <fieldUpdates>
        <fullName>Assign_New_Candidate_to_Recruiter_Queue</fullName>
        <field>OwnerId</field>
        <lookupValue>Recruiter_Queue</lookupValue>
        <lookupValueType>Queue</lookupValueType>
        <name>Assign New Candidate to Recruiter Queue</name>
        <notifyAssignee>true</notifyAssignee>
        <operation>LookupValue</operation>
        <protected>false</protected>
    </fieldUpdates>
    <rules>
        <fullName>New Candidate Notification</fullName>
        <actions>
            <name>Assign_New_Candidate_to_Recruiter_Queue</name>
            <type>FieldUpdate</type>
        </actions>
        <active>true</active>
        <formula>DATEVALUE(CreatedDate ) = TODAY()</formula>
        <triggerType>onCreateOnly</triggerType>
    </rules>
</Workflow>
