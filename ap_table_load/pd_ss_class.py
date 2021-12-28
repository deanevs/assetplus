import smartsheet
import pandas as pd
import gc

USER_SH_ID = 2653924667746180
SITES = 6307559394043780
MED_DEPTS = 6105077455841156

configs = {'api_key': '2s72jhlhz5470vo0culgpusmf4',
           'value_cols': ['Assigned User']}

def set_options():
    pd.set_option('max_columns', None)
    pd.set_option("max_rows", None)
    pd.set_option('display.width', 1000)


class SmartsheetConnector:
    def __init__(self, configs):
        self._cfg = configs
        self.ss = smartsheet.Smartsheet(self._cfg['api_key'])
        self.ss.errors_as_exceptions(True)

    def get_sheet_as_dataframe(self, sheet_id):l
        sheet = self.ss.Sheets.get_sheet(sheet_id)
        col_map = {col.id: col.title for col in sheet.columns}
        # rows = sheet id, row id, cell values or display values
        data_frame = pd.DataFrame([[sheet.id, row.id] +
                                   [cell.value if col_map[cell.column_id] in self._cfg['value_cols']
                                    else cell.display_value for cell in row.cells]
                                   for row in sheet.rows],
                                  columns=['Sheet ID', 'Row ID'] + [col.title for col in sheet.columns])
        del sheet, col_map
        gc.collect()  # force garbage collection
        return data_frame

    def get_report_as_dataframe(self, report_id):
        rprt = self.ss.Reports.get_report(report_id, page_size=0)
        page_count = int(rprt.total_row_count/10000) + 1
        col_map = {col.virtual_id: col.title for col in rprt.columns}
        data = []
        for page in range(1, page_count + 1):
            rprt = self.ss.Reports.get_report(report_id, page_size=10000, page=page)
            data += [[row.sheet_id, row.id] +
                     [cell.value if col_map[cell.virtual_column_id] in self._cfg['value_cols']
                      else cell.display_value for cell in row.cells] for row in rprt.rows]
            del rprt
        data_frame = pd.DataFrame(data, columns=['Sheet ID', 'Row ID']+list(col_map.values()))
        del col_map, page_count, data
        gc.collect()
        return data_frame

    def update_cell(self, row_id, col_id, value):
        """
        Updates a cell value by adding to appropriate update list
        Args:
            value = value to set the cell to
            row = SS row object for current row
            col_name = string value for column names
        Return:
            row object
        """
        # build new cell value
        new_cell = self.ss.models.Cell()  # first update the cell value according to the column
        new_cell.column_id = col_id
        new_cell.value = value
        new_cell.strict = False
        # build the row to update
        new_row = self.ss.models.Row()  # now set the correct row
        new_row.id = row_id
        new_row.cells.append(new_cell)  # set this row with the updated cell
        return new_row


def main():
    set_options()
    ss_obj = SmartsheetConnector(configs)
    df = ss_obj.get_sheet_as_dataframe(MED_DEPTS)
    print(df)

if __name__ == '__main__':
    main()