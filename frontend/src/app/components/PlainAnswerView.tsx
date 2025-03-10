import React from 'react';

export default function PlainAnswerView({ text }: { text: string }) {
  return (
    <React.Fragment>
      <div className="bg-indigo-400 text-white rounded-md p-2">{text}</div>
    </React.Fragment>
  );
}
