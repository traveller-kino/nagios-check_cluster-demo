
K_WORKSTATIONS = 24

workstation_command = r"""
   define command {{
       command_name check_vdi_workstation_{number}
       command_line $USER1$/check_tcp -H $HOSTADDRESS$ -p {numberPlusOffset} -w 5 -c 8 -e "RFB"
   }}
"""
check_cluster_command = r"""check_service_cluster!"VDI Workstations"!0!1!{workstationmacros}"""
workstation_macro = r"""$SERVICESTATEID::Workstation {number}$"""

for i in range(1, K_WORKSTATIONS):
    print(str(workstation_command.format(number=i, numberPlusOffset=5900+i)))

allWorkstations = []
for i in range(1, K_WORKSTATIONS):
    allWorkstations.append(workstation_macro.format(number=i))

print(check_cluster_command.format( workstationmacros=(",".join(allWorkstations)) ))