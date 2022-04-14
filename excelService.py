import pandas as pd


def gather_data_from_raw_extractions(extractions_file_names, save_path: str):
    full_data = pd.DataFrame()
    for extraction_file_name in extractions_file_names:
        raw_extraction_df = pd.read_csv(extraction_file_name, encoding='cp1251', sep=';', engine='python',
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
        full_data = pd.concat([full_data, prepared_extraction_df])
    a = full_data.groupby('Category').sum().reset_index().sort_values(by='Amount')
    save_df_to_csv(full_data, save_path)


def get_category_spending(file: str):
    df = read_from_excel(file)
    return df.groupby('Category').sum().reset_index().sort_values(by='Amount')


def save_df_to_csv(df, save_path: str):
    # open a file for writing
    prepared_extraction_file = open(save_path, "w", encoding="utf-8")
    # convert df to .csv with no df index
    prepared_extraction_file.write(df.to_csv(sep=';', line_terminator='\n', index=False))
    prepared_extraction_file.close()


def read_from_excel(file_name, columns=None):
    return pd.read_csv(file_name, sep=';', usecols=columns)


def sanitize_numeric_input(numeric_input):
    stripped_input = numeric_input.replace(' ', '')
    return float(stripped_input.replace(',', '.'))
