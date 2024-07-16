import React from 'react';

interface TableViewProps {
  tableData: any[];
}

const TableView = ({ tableData }: TableViewProps) => {
  const tableHeaders = tableData.length > 0 ? Object.keys(tableData[0]) : [];

  const downloadCSV = () => {
    const csvRows = [];
    csvRows.push(tableHeaders.join(','));
    for (const row of tableData) {
      const values = tableHeaders.map((header) =>
        JSON.stringify(row[header], replacer)
      );
      csvRows.push(values.join(','));
    }
    const csvString = csvRows.join('\n');
    const blob = new Blob([csvString], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'tableData.csv';
    a.click();
    URL.revokeObjectURL(url);
  };

  const replacer = (key: any, value: null) => (value === null ? '' : value);

  return (
    <div className="overflow-x-auto text-Pri-Dark">
      {tableData.length !== 0 && (
        <div className="min-w-full">
          <button
            onClick={downloadCSV}
            className="mb-4 px-4 py-2 font-semibold bg-gray-100 text-Pri-Dark rounded"
          >
            Download CSV
          </button>
          <div>
            <h1 className="text-md font-semibold text-gray-700">Table Data</h1>
          </div>
          <table className="min-w-full border-collapse">
            <thead>
              <tr className="bg-gray-200 font-bold text-Pri-Dark">
                {tableHeaders.map((header) => (
                  <th key={header} className="p-2 border">
                    {header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, index) => (
                <tr key={index} className="border-b">
                  {tableHeaders.map((header) => (
                    <td key={`${index}-${header}`} className="p-2 border">
                      {row[header]}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default TableView;
