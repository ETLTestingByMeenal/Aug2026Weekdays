# Q1.Record Count Validation
# Compare Source & Target Record Count
source_count=1000
target_count=980
if source_count==target_count:
    print(f"Pass: {source_count} and {target_count} are matching")
else:
    print(f"Fail: {source_count} and {target_count} are not matching")

# Calculate Missing Record
missing_count=source_count-target_count
print(f"Missing record count between source and Target : {missing_count}")

# Q2. ETL Job SLA Validation
'''Business Rule:
# <= 30 minutes -> SLA Met
# 31-45 minutes -> SLA Warning
# > 45 minutes -> SLA Breached '''
duration=25
if duration<=30:
    print(f"SLA met: duration is {duration}")
elif duration<=45:
    print(f"SLA warning: duration is {duration}")
else:
    print(f"SLA breached: duration is {duration}")

# Q3. Validate 10 ETL Records
#Generates numbers from 1 to 10 using range()
for record in range(1,11):
    print(f"Validating record : {record}")
print("Validation completed")

# Q4. Identify failed ETL records
'''Assume we have 20 records.
Every 5th record is considered a failed record.
Expected failed records:
5, 10, 15, 20
% gives the remainder after division.
If remainder is 0, the number is divisible by 5 '''
for record in range(5,21,5):
    if record%5==0:
        print(f"Failed record : {record}")





