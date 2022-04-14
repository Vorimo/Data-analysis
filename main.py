import excelService
import plotService

if __name__ == '__main__':
    # pandas
    output_file = 'extractions/prepared/full_data.csv'
    excelService.gather_data_from_raw_extractions([
        'extractions/raw/03_2022.csv',
        'extractions/raw/04_2022.csv'
    ], output_file)
    columns_to_extract = ['Amount', 'Transaction date']
    full_extraction = excelService.read_from_excel(output_file, columns_to_extract)
    columns_to_show = [columns_to_extract[0]]
    x_label = 'date'
    y_label = 'amount'
    title = 'Money spending data'
    # plot full extraction info by date
    plotService.plot_df(full_extraction, columns_to_show, x_label, y_label, title, 'BYN')
    plotService.save_plot_and_show('extractions/plots/full_data.png')
    # plot bar with categories spending ordered by amount
    category_spending = excelService.get_category_spending(output_file)
    plotService.plot_chart_df(category_spending['Category'], category_spending['Amount'])
    plotService.save_plot_and_show('extractions/plots/category_spending.png')
