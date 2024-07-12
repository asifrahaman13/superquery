'use client';
/* eslint-disable @next/next/no-img-element */
import { file_interface } from '@/exports/exports';
import React, { useEffect } from 'react';

const Page = () => {
  const [presignedUrls, setPresignedUrls] = React.useState([]);
  useEffect(() => {
    console.log('Saved graphs page');

    async function fetchAllPresignedUrls() {
      const token = localStorage.getItem('accessToken') || '';
      const response = await file_interface.presignedUrls(token);
      if (response?.code === 200) {
        setPresignedUrls(response.data.url);
      }
    }

    fetchAllPresignedUrls();
  }, []);
  return (
    <React.Fragment>
      <div className="flex flex-col">
        <div className="text-xl font-medium px-4">My saved graphs</div>
        <div className="flex flex-col h-full overflow-y-scroll no-scrollbar py-12">
          <div className="flex flex-wrap px-4">
            {presignedUrls.map((item, index) => (
              <div key={index} className="p-2">
                <img src={item} alt="" />
              </div>
            ))}
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Page;
