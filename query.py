# call table
SecurityEvent
# only certain records
| where Level == 8

# call table
SecurityEvent
# only certain records
| where Level == 8 and EventID == 4600

# call table
SecurityEvent
# only certain records
| where Level == 8 
| where EventID == 4600
| where TimeGenerated = ago(3d)
# only these columns
| project TimeGenerated, Computer, Activity
# only certain rows (records 0-4)
| extend EventCode = substring(Acitvity, 0, 4)
# aggregate data - sum of computers - for records, and then include Event Code
| summarize count() by Computer, EventCode
# create piechart
| render piechart
# create timechart
| render timechart
