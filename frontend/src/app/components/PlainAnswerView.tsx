import React from 'react';

export default function PlainAnswerView({ text }: { text: string }) {
  return (
    <React.Fragment>
      <div className="bg-indigo-400 max-w-xl text-white rounded-md p-4">{text}</div>
    </React.Fragment>
  );
}
