import excelService
import plotService

if __name__ == '__main__':
    # pandas
    excelService.gather_data_from_raw_extraction('extractions/Vpsk_68738292.csv', 'extractions/prepared/1.csv')
    excelService.gather_data_from_raw_extraction('extractions/Vpsk_68738293.csv', 'extractions/prepared/2.csv')
    columns_to_extract = ['Amount', 'Transaction date']
    extraction_march = excelService.read_from_excel('extractions/prepared/1.csv', columns_to_extract)
    extraction_april = excelService.read_from_excel('extractions/prepared/2.csv', columns_to_extract)
    columns_to_show = [columns_to_extract[0]]
    x_label = 'date'
    y_label = 'amount'
    title = 'Money spending data'
    plotService.plot_df(extraction_march, columns_to_show, x_label, y_label, title, 'March')
    plotService.plot_df(extraction_april, columns_to_show, x_label, y_label, title, 'April')
    plotService.save_plot_and_show('extractions/plots/1.png')
