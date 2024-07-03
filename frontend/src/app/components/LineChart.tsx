import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
  TimeScale,
} from 'chart.js';
import 'chartjs-adapter-date-fns';

ChartJS.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
);

interface LineChartProps {
  data: {
    message: string;
  };
}

const LineChart = ({ data }: LineChartProps) => {
  // Parse the JSON data
  const parsedData = JSON.parse(data.message);

  // Prepare chart data
  const datasets = parsedData.map((product: any) => {
    const productName = Object.keys(product)[0];
    const productData = product[productName];

    return {
      label: productName,
      data: productData.map((item: { x: any; y: any }) => ({
        x: item.x,
        y: item.y,
      })),
      fill: 'start', // Fill below the line
      backgroundColor: `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(
        Math.random() * 255
      )}, ${Math.floor(Math.random() * 255)}, 0.2)`,
      borderColor: `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(
        Math.random() * 255
      )}, ${Math.floor(Math.random() * 255)}, 1)`,
      tension: 0.4, // Adjust the curve tension here
    };
  });

  // Chart options
  const options = {
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'day',
        },
        title: {
          display: true,
          text: 'Date',
        },
      },
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Value',
        },
      },
    },
  };

  // Chart data
  const chartData = {
    datasets: datasets,
  };

  return <Line data={chartData} options={options} />;
};

export default LineChart;
