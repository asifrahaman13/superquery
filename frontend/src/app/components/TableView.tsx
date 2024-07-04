import React from 'react';

interface TableViewProps {
  tableData: any[];
}

const TableView = ({ tableData }: TableViewProps) => {
  const tableHeaders = tableData.length > 0 ? Object.keys(tableData[0]) : [];
  return (
    <div>
      {' '}
      {tableData.length !== 0 && (
        <div className=" overflow-y-scroll no-scrollbar flex flex-col gap-4">
          <div className="text-2xl font-semibold text-Pri-Dark">
            {' '}
            🚀My Result
          </div>
          <div className="flex flex-col">
            <div className="flex bg-gray-200 font-bold">
              {tableHeaders?.map((header) => (
                <div key={header} className="p-2 flex-1 border">
                  {header}
                </div>
              ))}
            </div>
            <div className="flex flex-col">
              {tableData?.map((row, index) => (
                <div key={index} className="flex border-b">
                  {tableHeaders?.map((header) => (
                    <div
                      key={`${index}-${header}`}
                      className="p-2 flex-1 border"
                    >
                      {row[header]}
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TableView;
