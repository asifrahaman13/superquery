'use client';
import React from 'react';
import { Line, Bar, Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  BarElement,
  PointElement,
  CategoryScale,
  LinearScale,
  ArcElement,
} from 'chart.js';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  BarElement,
  PointElement,
  CategoryScale,
  LinearScale,
  ArcElement
);

interface DynamicChartProps {
  data: string; // Dynamic JSON data as a string
  type: string; // Type of chart
}

const DynamicChart: React.FC<DynamicChartProps> = ({ data, type }) => {
  const parsedData = JSON.parse(data);
  console.log(
    'Here is the data #######################################################33',
    parsedData
  );

  // Extract keys (columns) for labels and their corresponding values for datasets
  const keys = Object.keys(parsedData[0]);
  const labels = parsedData
    .map((item: any) => keys.map((key) => item[key]))
    .flat(); // Flatten the values to create labels
  const datasets = keys.map((key) => {
    const values = parsedData.map((item: any) => item[key]);
    return {
      label: key,
      data: values,
      borderColor: getRandomColor(),
      backgroundColor: type === 'pie' ? getRandomColor() : undefined,
      borderWidth: type === 'pie' ? undefined : 1,
      fill: type === 'line',
    };
  });

  // Prepare chart data
  const chartData = {
    labels: parsedData.map((item: any) => item[keys[0]]), // Use the first key's values as labels
    datasets,
  };

  // Render chart based on type
  switch (type) {
    case 'line':
      return <Line data={chartData} />;
    case 'bar':
      return <Bar data={chartData} />;
    case 'pie':
      return <Pie data={chartData as any} />;
    default:
      return null;
  }
};

function getRandomColor() {
  return `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 0.5)`;
}

export default DynamicChart;
