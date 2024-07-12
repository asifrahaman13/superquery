import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import useSaveChart from '@/app/hooks/charts';

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
  const { chartRef, saveChart } = useSaveChart();

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
