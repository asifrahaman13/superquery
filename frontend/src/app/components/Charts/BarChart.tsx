import React, { useRef } from 'react';
import { Bar } from 'react-chartjs-2';
import html2canvas from 'html2canvas';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

interface BarChartProps {
  data: {
    message: string;
  };
}

const BarChart = ({ data }: BarChartProps) => {
  const chartRef = useRef(null);

  // Parse the JSON data
  const parsedData = JSON.parse(data.message);

  // Extract labels and values
  const labels = parsedData.map((item: { x: any }) => item.x);
  const values = parsedData.map((item: { y: any }) => item.y);

  // Prepare chart data
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: 'Data Points',
        data: values,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  // Chart options
  const options = {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  const saveChart = () => {
    if (chartRef.current) {
      html2canvas(chartRef.current).then((canvas) => {
        const link = document.createElement('a');
        link.href = canvas.toDataURL('image/png');
        link.download = 'chart.png';
        link.click();
      });
    }
  };

  return (
    <div>
      <div ref={chartRef}>
        <Bar data={chartData} options={options} />
      </div>
      <button onClick={saveChart}>Save Chart</button>
    </div>
  );
};

export default BarChart;
