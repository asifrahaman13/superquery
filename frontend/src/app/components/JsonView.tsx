import React from 'react';

interface JSONRendererProps {
  data: any;
}

const JSONRenderer: React.FC<JSONRendererProps> = ({ data }) => {
  // Recursive function to render JSON data with indentation
  const renderJSON = (data: any, indentLevel: number = 0): JSX.Element => {
    if (Array.isArray(data)) {
      return (
        <div className="ml-6">
          <span className="text-gray-700">[</span>
          <ul className="list-none">
            {data.map((item, index) => (
              <li key={index} className="ml-4">
                {renderJSON(item, indentLevel + 1)}
              </li>
            ))}
          </ul>
          <span className="text-gray-700">]</span>
        </div>
      );
    } else if (typeof data === 'object' && data !== null) {
      return (
        <div className="ml-6">
          <span className="text-gray-700">{'{'}</span>
          <ul className="list-none">
            {Object.entries(data).map(([key, value]) => (
              <li key={key} className="ml-4">
                <span className="text-red-600">{key}</span>:{' '}
                {renderJSON(value, indentLevel + 1)}
              </li>
            ))}
          </ul>
          <span className="text-gray-700">{'}'}</span>
        </div>
      );
    } else {
      return <span className="text-blue-600">{String(data)}</span>;
    }
  };

  return (
    <div className="font-mono text-sm p-4 overflow-y-scroll bg-gray-100 rounded shadow">
      {renderJSON(data)}
    </div>
  );
};

export default JSONRenderer;
