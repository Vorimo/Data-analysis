import pandas as pd


def gather_data_from_raw_extraction(extractions_file_name, save_path: str):
    raw_extraction_df = pd.read_csv(extractions_file_name, encoding='cp1251', sep=';', engine='python',
                                    usecols=[0, 1, 2, 8])
    # drop empty values
    prepared_extraction_df = raw_extraction_df.dropna()
    # columns rename
    prepared_extraction_df = prepared_extraction_df.rename(columns={
        'Дата транзакции': 'Transaction date',
        'Операция': 'Operation',
        'Сумма': 'Amount',
        'Валюта': 'Currency',
        'Категория операции': 'Category'
    })
    # trim all strings
    prepared_extraction_df = prepared_extraction_df.applymap(lambda x: x.strip())
    # sort by date desc
    prepared_extraction_df = prepared_extraction_df.sort_values(by='Transaction date', ascending=False)
    # sanitize numeric input
    prepared_extraction_df['Amount'] = prepared_extraction_df['Amount'].apply(lambda x: sanitize_numeric_input(x))
    # open a file for writing
    prepared_extraction_file = open(save_path, "w", encoding="utf-8")
    # convert df to .csv with no df index
    prepared_extraction_file.write(prepared_extraction_df.to_csv(sep=';', line_terminator='\n', index=False))
    prepared_extraction_file.close()


def read_from_excel(file_name, columns):
    return pd.read_csv(file_name, sep=';', usecols=columns)


def sanitize_numeric_input(numeric_input):
    stripped_input = numeric_input.replace(' ', '')
    return float(stripped_input.replace(',', '.'))
