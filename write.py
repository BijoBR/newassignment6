import json
india ={

    "maharastra":"mumbai",
    "Tamil Nadu":"Chennai",
    "kerala":"Thiruvanthapuram",
    "karnataka":"Bangaore",
    "madhya pradesh":"bhopal",
    "goa":"panaji",
    "jarkhand":"ranchi" 
}
with open(r"D:\test file1\_1_datatype\Assignment_file.py\states.json","w+") as file:
    data =json.dump(india,file)
    print(data)