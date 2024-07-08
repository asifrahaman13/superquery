import { Chart as ChartJS, ArcElement, Title, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Title, Tooltip, Legend);

interface PieChartProps {
  data: {
    message: string;
  };
}

const PieChart = ({ data }: PieChartProps) => {
  // Parse the JSON data
  const parsedData = JSON.parse(data.message);

  // Extract labels and values
  const labels = parsedData.map((item: any) => Object.keys(item)[0]);
  const values = parsedData.map((item: any) => Object.values(item)[0]);

  // Prepare chart data
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: 'Data Points',
        data: values,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  // Chart options
  const options = {
    plugins: {
      legend: {
        display: true,
        position: 'top' as 'top', // Specify the position as 'top'
      },
    },
  };

  return <Pie data={chartData} options={options} />;
};

export default PieChart;
