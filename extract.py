import pandas as pd
import os

def generate_raw_parquet(src_path, dest_path, separator, dataset_name):

    
    files_in_path = os.listdir(path=src_path)
    if dataset_name == "banks":
        extension = ".tsv"
    else:
        extension = ".csv"
    
    for file in files_in_path:
        file_name_parquet = file.replace(extension,".parquet")

        if file.endswith(extension):
            df = pd.read_csv(src_path+"\\"+file,sep=separator,encoding="latin-1")
            df.to_parquet(f"{dest_path}\\{file_name_parquet}")
            


destination_path = "C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\USP\\C3_Ingestão de Dados\\ETL com Python DBT\\seeds\\"
source_path="C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\USP\\C3_Ingestão de Dados\\ETL com Python DBT\\Dados\\"

generate_raw_parquet(src_path=source_path+"Bancos", dest_path=destination_path+"banks",separator="\t",dataset_name="banks")
generate_raw_parquet(src_path=source_path+"Empregados", dest_path=destination_path+"employees",separator="|",dataset_name="employees")
generate_raw_parquet(src_path=source_path+"Reclamações", dest_path=destination_path+"complaints",separator=";",dataset_name="complaints")