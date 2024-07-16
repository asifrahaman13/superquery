import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { materialLight } from 'react-syntax-highlighter/dist/esm/styles/prism';

interface SQLHighlighterProps {
  sqlQuery: string | undefined;
}

const SqlRender: React.FC<SQLHighlighterProps> = ({
  sqlQuery,
}: SQLHighlighterProps) => {
  return (
    <React.Fragment>
      <div>
        <h1 className="text-md font-semibold text-gray-700">SQL Query</h1>
      </div>
      {sqlQuery && (
        <SyntaxHighlighter language="sql" style={materialLight}>
          {sqlQuery}
        </SyntaxHighlighter>
      )}
    </React.Fragment>
  );
};

export default SqlRender;
