import { useRef } from 'react';
import html2canvas from 'html2canvas';
import { file_interface } from '@/exports/exports';
import { v4 as uuidv4 } from 'uuid';

const useSaveChart = () => {
  const chartRef = useRef(null);

  const saveChart = async () => {
    if (chartRef.current) {
      html2canvas(chartRef.current).then(async (canvas) => {
        canvas.toBlob(async (blob) => {
          const formData = new FormData();
          if (!blob) {
            return;
          }
          const filename = `chart-${uuidv4()}.png`;
          formData.append('file', blob, filename);

          try {
            const token = localStorage.getItem('accessToken') || '';
            const response = await file_interface.uploadFiles(token, formData);

            if (response?.code === 200) {
              alert('Chart saved successfully');
            } else {
              alert('Failed to save chart');
            }
          } catch (error) {
            console.error('Error uploading file:', error);
            alert('Failed to save chart');
          }
        }, 'image/png');
      });
    }
  };

  return { chartRef, saveChart };
};

export default useSaveChart;
