'use client';
import React, { useState } from 'react';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
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

  return <Bar data={chartData} options={options} />;
};

const Page = () => {
  const jsonData = {
    message:
      '[\n    {"x": "Mumbai jn", "y": 1},\n    {"x": "41 Nirupama devi road", "y": 1},\n    {"x": "Salimar", "y": 1},\n    {"x": "Mumbai", "y": 1},\n    {"x": "Delhi", "y": 2}\n]',
  };

  const [query, setQuery] = useState<string>('');

  const handleChange = (e: {
    target: {
      value: React.SetStateAction<string>;
    };
  }) => {
    setQuery(e.target.value);
  };

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault();
  };

  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  return (
    <>
      {settingsBar && <ConnectionSettings dbType="mysql" key={key} />}
      <div className="w-full flex flex-col ">
        <div className="w-full flex flex-row h-full">
          <div className="w-1/2 flex flex-col gap-4 h-full justify-between  p-6">
            <label
              htmlFor="email"
              className="block font-semibold leading-6 text-3xl text-Pri-Dark"
            >
              MySQL Query
            </label>

            <div className="overflow-y-scroll no-scrollbar h-full flex flex-col gap-2 text-justify">
              <div className="bg-indigo-400 w-3/4 max-w-3/4 rounded-md p-2 text-white">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Cupiditate, quaerat beatae iste deserunt animi rem totam nulla
                enim voluptatem obcaecati assumenda earum minus, accusamus
                praesentium libero hic ad sunt, dolor magni quia dolores
                corrupti.
              </div>
              <div className="bg-gray-200 w-3/4 max-w-3/4 rounded-md p-2 ml-auto text-justify">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. At
                doloremque sunt nesciunt qui impedit voluptatibus quod iusto
                fugit, vel, quaerat enim rerum quas, numquam et culpa eum! Et
                itaque harum unde veniam ex tenetur aperiam esse facilis maxime
                consequatur. Recusandae optio perspiciatis odio praesentium
                autem hic? Nam accusamus quaerat aut.
              </div>
              <div className="bg-indigo-400 w-4/5 rounded-md p-2 text-white">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Cupiditate, quaerat beatae iste deserunt animi rem totam nulla
                enim voluptatem obcaecati assumenda earum minus, accusamus
                praesentium libero hic ad sunt, dolor magni quia dolores
                corrupti.
              </div>
              <div className="bg-gray-200 w-4/5 max-w-4/5 rounded-md p-2 ml-auto text-justify">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. At
                doloremque sunt nesciunt qui impedit voluptatibus quod iusto
                fugit, vel, quaerat enim rerum quas, numquam et culpa eum! Et
                itaque harum unde veniam ex tenetur aperiam esse facilis maxime
                consequatur. Recusandae optio perspiciatis odio praesentium
                autem hic? Nam accusamus quaerat aut.
              </div>{' '}
              <div className="bg-indigo-400 w-4/5 rounded-md p-2 text-white">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Cupiditate, quaerat beatae iste deserunt animi rem totam nulla
                enim voluptatem obcaecati assumenda earum minus, accusamus
                praesentium libero hic ad sunt, dolor magni quia dolores
                corrupti.
              </div>
              <div className="bg-gray-200 w-4/5 max-w-4/5 rounded-md p-2 ml-auto text-justify">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. At
                doloremque sunt nesciunt qui impedit voluptatibus quod iusto
                fugit, vel, quaerat enim rerum quas, numquam et culpa eum! Et
                itaque harum unde veniam ex tenetur aperiam esse facilis maxime
                consequatur. Recusandae optio perspiciatis odio praesentium
                autem hic? Nam accusamus quaerat aut.
              </div>{' '}
              <div className="bg-indigo-400 w-4/5 rounded-md p-2 text-white">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Cupiditate, quaerat beatae iste deserunt animi rem totam nulla
                enim voluptatem obcaecati assumenda earum minus, accusamus
                praesentium libero hic ad sunt, dolor magni quia dolores
                corrupti.
              </div>
              <div className="bg-gray-200 w-4/5 max-w-4/5 rounded-md p-2 ml-auto text-justify">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. At
                doloremque sunt nesciunt qui impedit voluptatibus quod iusto
                fugit, vel, quaerat enim rerum quas, numquam et culpa eum! Et
                itaque harum unde veniam ex tenetur aperiam esse facilis maxime
                consequatur. Recusandae optio perspiciatis odio praesentium
                autem hic? Nam accusamus quaerat aut.
              </div>{' '}
              <div className="bg-indigo-400 w-4/5 rounded-md p-2 text-white">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Cupiditate, quaerat beatae iste deserunt animi rem totam nulla
                enim voluptatem obcaecati assumenda earum minus, accusamus
                praesentium libero hic ad sunt, dolor magni quia dolores
                corrupti.
              </div>
              <div className="bg-gray-200 w-4/5 max-w-4/5 rounded-md p-2 ml-auto text-justify">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. At
                doloremque sunt nesciunt qui impedit voluptatibus quod iusto
                fugit, vel, quaerat enim rerum quas, numquam et culpa eum! Et
                itaque harum unde veniam ex tenetur aperiam esse facilis maxime
                consequatur. Recusandae optio perspiciatis odio praesentium
                autem hic? Nam accusamus quaerat aut.
              </div>
              <BarChart data={jsonData} />
            </div>

            {/* 
            <div className="flex justify-center flex-grow">
              <SiMysql size={300} />
            </div> */}
            <div className="mt-2 flex gap-2 ">
              <input
                type="text"
                name="query"
                id="query"
                className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2"
                placeholder="Enter your query"
                value={query}
                onChange={handleChange}
              />
              <button
                onClick={handleSubmit}
                className="bg-Pri-Dark rounded-lg  p-3 px-5 text-white"
              >
                Submit
              </button>
            </div>
          </div>
          <div className="flex flex-col w-1/2 gap-8 border-2 p-6">
            <div className="h-1/2 flex flex-col gap-6">
              {' '}
              <div className="flex  w-full justify-between">
                <div className="text-3xl font-semibold text-Pri-Dark">
                  🎉 Manual Query
                </div>{' '}
                <div>
                  <button
                    className=" bg-Pri-Dark p-2 rounded-md px-4 text-white"
                    onClick={toggleSettingsBar}
                  >
                    Settings
                  </button>
                </div>
              </div>
              <p className="text-Pri-Dark text-lg font-medium text-justify">
                MySQL is a widely-used open-source relational database
                management system known for its scalability, performance, and
                robust feature set. It organizes data into tables linked by
                relationships, supporting multi-platform deployment and offering
                high availability through features like replication and
                clustering. MySQL excels in handling both small-scale
                applications and large-scale systems with efficient data
                management and query execution. Security features include access
                control and encryption, while its active community ensures
                continuous development and support. Commonly used in web
                applications, data warehousing, and online transaction
                processing (OLTP), MySQL remains a cornerstone for developers
                and businesses seeking a reliable, flexible database solution.{' '}
              </p>
              <textarea
                name="query"
                className="w-full h-20 border-2"
                id=""
              ></textarea>
              <div className="flex justify-end">
                <button className="bg-Pri-Dark rounded-lg w-1/5 text-righ p-3 px-5 text-white">
                  Submit
                </button>
              </div>
            </div>
            <div className="text-2xl font-semibold text-Pri-Dark">
              {' '}
              🚀My Result
            </div>
            <div className="h-1/2 border-2"></div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Page;
