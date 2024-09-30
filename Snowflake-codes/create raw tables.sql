USE DBT_DB.DBT_RAW;

CREATE TABLE BANKS (
    SEGMENTO NVARCHAR(5)
    ,CNPJ NVARCHAR(12)
    ,Nome NVARCHAR(255)
);

CREATE TABLE COMPLAINTS (
	Ano INT,
	Trimestre NVARCHAR(4),
	Categoria NVARCHAR(100),
	Tipo NVARCHAR(30),
	CNPJ_IF NVARCHAR(15),
	Instituicao_financeira NVARCHAR(100),
	Indice FLOAT,
	Quantidade_de_reclamacoes_reguladas_procedentes INT,
	Quantidade_de_reclamacoes_reguladas_outras INT,
	Quantidade_de_reclamacoes_nao_reguladas INT,
	Quantidade_total_de_reclamacoes INT,
	Quantidade_total_de_clientes_CCS_e_SCR INT,
	Quantidade_de_clientes_CCS INT,
	Quantidade_de_clientes_SCR INT
);

CREATE TABLE EMPLOYEES(
    employer_name NVARCHAR(50),
	reviews_count INT,
	culture_count INT,
	salaries_count INT,
	benefits_count INT,
	employer_website NVARCHAR(100),
	employer_headquarters NVARCHAR(50),
	employer_founded FLOAT,
	employer_industry NVARCHAR(255),
	employer_revenue NVARCHAR(80),
	url NVARCHAR(255),
	Geral FLOAT,
	Cultura_e_valores FLOAT,
	Diversidade_e_inclusao FLOAT,
	Qualidade_de_vida FLOAT,
	Alta_lideranca FLOAT,
	Remuneracao_e_beneficios FLOAT,
	Oportunidades_de_carreira FLOAT,
	Recomendam_para_outras_pessoas_PCT FLOAT,
	Perspectiva_positiva_da_empresa_PCT FLOAT,
	CNPJ_Segmento NVARCHAR(30),
	Nome NVARCHAR(255),
	match_percent NVARCHAR(3)
);