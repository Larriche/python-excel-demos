# This program was used to read an Excel file containing 
# vehicle recall data and outputting the data to a text file
# in a format where it could be copied to create a Laravel 
# seeder file
import xlrd

filename = "recalls.xlsx"
workbook = xlrd.open_workbook(filename)
sheet = workbook.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols
seed = ""

template = ("[\n\t\"nhtsa_campaign_number\" => \"NHTSA\",\n\t\"recall_id\""
             + " => \"RECALL\",\n\t\"component\"=>\"COMPONENT\"\n]")

for i in range(1, rows):
    recall = sheet.cell(i, 1).value.upper().replace(", ", ",").strip()
    nhtsas  = sheet.cell(i, 2).value.upper().strip()
    component = sheet.cell(i, 3).value.upper().strip()

    for nhtsa in nhtsas.split(","):
        # The final data requires 3 more trailing zeroes
        if nhtsa != "":
            nhtsa += "000"
            
        current = template
        current = current.replace("NHTSA",nhtsa.strip())
        current = current.replace("RECALL", recall)
        current = current.replace("COMPONENT", component)

        seed += current + ",\n\n" 

with open("output.txt", "w") as out:
    out.write(seed)
    

    
