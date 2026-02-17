pkg_weights=[4,18,70,-2,30,55,0,90,12]
full_name="MaheshKumarBolagani"
name_length=0
for ch in full_name:
    name_length=name_length+1
pli_value=name_length%3
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
for weight in pkg_weights:
    if weight<0:
        invalid_entries=invalid_entries+[weight]
    elif weight<=5:
        very_light=very_light+[weight]
    elif weight<=25:
        normal_load=normal_load+[weight]
    elif weight<=60:
        heavy_load=heavy_load+[weight]
    else:
        overload=overload+[weight]
changed_count=0
if pli_value==0:
    for item in overload:
        invalid_entries=invalid_entries+[item]
        changed_count=changed_count+1
    overload=[]
elif pli_value==1:
    for item in very_light:
        changed_count=changed_count+1
    very_light=[]
elif pli_value==2:
    for item in very_light:
        changed_count=changed_count+1
    for item in overload:
        changed_count=changed_count+1
    very_light=[]
    overload=[]
final_plan=[]
for item in very_light:
    final_plan=final_plan+[item]
for item in normal_load:
    final_plan=final_plan+[item]
for item in heavy_load:
    final_plan=final_plan+[item]
for item in overload:
    final_plan=final_plan+[item]
valid_total=0
for weight in pkg_weights:
    if weight>=0:
        valid_total=valid_total+1
print("Length(L):",name_length)
print("PLI value:",pli_value)
print("Affected Items:",changed_count)
print("Total valid Weights:",valid_total)
print("very_light:",very_light)
print("normal_load:",normal_load)
print("heavy_load:",heavy_load)
print("overload:",overload)
print("invalid_entries:",invalid_entries)
print("Final plan:",final_plan)
