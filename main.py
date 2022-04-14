import excelService
import plotService

if __name__ == '__main__':
    # pandas
    output_march_file = 'extractions/prepared/03_2022.csv'
    output_april_file = 'extractions/prepared/04_2022.csv'
    excelService.gather_data_from_raw_extraction('extractions/03_2022.csv', output_march_file)
    excelService.gather_data_from_raw_extraction('extractions/04_2022.csv', output_april_file)
    columns_to_extract = ['Amount', 'Transaction date']
    extraction_march = excelService.read_from_excel(output_march_file, columns_to_extract)
    extraction_april = excelService.read_from_excel(output_april_file, columns_to_extract)
    columns_to_show = [columns_to_extract[0]]
    x_label = 'date'
    y_label = 'amount'
    title = 'Money spending data'
    plotService.plot_df(extraction_march, columns_to_show, x_label, y_label, title, 'March')
    plotService.plot_df(extraction_april, columns_to_show, x_label, y_label, title, 'April')
    plotService.save_plot_and_show('extractions/plots/1.png')
