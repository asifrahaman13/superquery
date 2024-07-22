'use client';
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
import useSaveChart from '@/app/hooks/charts';

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
  data: string;
  type: string;
}

function getRandomColor() {
  return `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 0.5)`;
}

const DynamicChart: React.FC<DynamicChartProps> = ({ data, type }) => {
  const { chartRef, saveChart } = useSaveChart();

  const parsedData = JSON.parse(data);
  const keys = Object.keys(parsedData[0]);
  const labels = parsedData
    .map((item: any) => keys.map((key) => item[key]))
    .flat();
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

  const chartData = {
    labels: parsedData.map((item: any) => item[keys[0]]),
    datasets,
  };

  return (
    <div>
      <div ref={chartRef}>
        {type === 'line' && <Line data={chartData} />}
        {type === 'bar' && <Bar data={chartData} />}
        {type === 'pie' && <Pie data={chartData as any} />}
      </div>
      <button onClick={saveChart} className="bg-gray-100 rounded-lg px-4 py-2">
        Save Chart
      </button>
    </div>
  );
};

export default DynamicChart;
