import pandas as pd
import os

def generate_raw(src_path, dest_path, separator, dataset_name,columns):
    complaint_cols = {
        "Ano":"int64",
        "Trimestre":"str",
        "Categoria":"str",
        "Tipo":"str",
        "CNPJ IF":"str",
        "Instituição financeira":"str",
        # "Índice":"float64",
        "Quantidade de reclamações reguladas procedentes":"int64",
        "Quantidade de reclamações reguladas - outras":"int64",
        "Quantidade de reclamações não reguladas":"int64",
        "Quantidade total de reclamações":"int64",
        "Quantidade total de clientes – CCS e SCR":"int64",
        "Quantidade de clientes – CCS":"int64",
        "Quantidade de clientes – SCR":"int64"
    }
    concatenated_dataframes = []
    files_in_path = os.listdir(path=src_path)
    if dataset_name == "banks":
        extension = ".tsv"
    else:
        extension = ".csv"
    
    for file in files_in_path:
        # file_name_parquet = file.replace(extension,".parquet")

        if file.endswith(extension):
            if dataset_name == 'complaints':
                df = pd.read_csv(src_path+"\\"+file,sep=separator,encoding="latin-1",dtype=complaint_cols,)
                
            else:
                df = pd.read_csv(src_path+"\\"+file,sep=separator,encoding="latin-1")
            if "CNPJ" in df.columns:
                df['CNPJ'] = df['CNPJ'].astype('str')
            df.columns = columns
            concatenated_dataframes.append(df)

    df_final = pd.concat(concatenated_dataframes,)
    df_final.to_csv(dest_path+f"\\{dataset_name}.csv",index=False)


    
            

    
destination_path = "C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\USP\\C3_Ingestão de Dados\\ETL com Python DBT\\Dados\\_raw\\"
source_path="C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\USP\\C3_Ingestão de Dados\\ETL com Python DBT\\Dados\\"
bancos_columns = ["SEGMNETO","CNPJ","NOME"]
empregados_columns = ["employer_name",	"reviews_count",	"culture_count",	"salaries_count",	"benefits_count",	"employer_website",	"employer_headquarters",	"employer_founded",	"employer_industry",	"employer_revenue",	"url",	"Geral",	"Cultura_e_valores",	"Diversidade_e_inclusao",	"Qualidade_de_vida",	"Alta_lideranca",	"Remuneracao_e_beneficios",	"Oportunidades_de_carreira",	"Recomendam_para_outras_pessoas_PCT",	"Perspectiva_positiva_da_empresa_PCT",	"CNPJ_Segmento",	"Nome",	"match_percent"]
reclamacoes_columns = ["Ano","Trimestre","Categoria","Tipo","CNPJ_IF","instituicao_financeira","indice","quantidade_de_reclamacoes_reguladas_procedentes","quantidade_de_reclamacoes_reguladas_outras","quantidade_de_reclamacoes_nao_reguladas","quantidade_total_de_reclamacoes","quantidade_total_de_clientes_CCS_e_SCR","quantidade_de_clientes_CCS","quantidade_de_clientes_SCR","drop_this_column"]

generate_raw(src_path=source_path+"Bancos", dest_path=destination_path+"banks",separator="\t",dataset_name="banks",columns=bancos_columns)
generate_raw(src_path=source_path+"Empregados", dest_path=destination_path+"employees",separator="|",dataset_name="employees",columns=empregados_columns)
generate_raw(src_path=source_path+"Reclamações", dest_path=destination_path+"complaints",separator=";",dataset_name="complaints",columns=reclamacoes_columns)