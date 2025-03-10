/* eslint-disable @next/next/no-img-element */
'use client';
import { useEffect, useState } from 'react';
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/react';
import { XMarkIcon } from '@heroicons/react/24/outline';
import { configuration_interface } from '@/exports/exports';
import SuccessStatus from '../ui/SuccessStatus';

interface DbSettings {
  dbType: string;
}

interface Configuration {
  db_type?: string;
  project_name?: string;
  username?: string;
  description?: string;
  connection_string?: string;
  ddl_commands?: string[];
  examples?: { query: string; sqlQuery: string }[];
}

export default function ConnectionSettings({ dbType }: DbSettings) {
  const [open, setOpen] = useState(true);
  const [configuration, setConfiguration] = useState<Configuration>({});
  const [successMessage, setSuccessMessage] = useState<boolean>(false);

  useEffect(() => {
    async function fetchConfigurations() {
      const token = localStorage.getItem('accessToken') || '';
      const response = await configuration_interface.getConfiguration(
        dbType,
        token
      );
      if (response?.code === 200) {
        setConfiguration(response.data);
      }
    }
    fetchConfigurations();
  }, [dbType]);

  async function updateConfigurations() {
    const token = localStorage.getItem('accessToken') || '';
    setConfiguration((prev) => ({ ...prev, db_type: dbType }));
    const response = await configuration_interface.updateConfiguration(
      token,
      configuration
    );
    if (response?.code === 200) {
      setSuccessMessage(true);
      setTimeout(() => setSuccessMessage(false), 1500);
    }
  }

  function handleChange(
    e: React.ChangeEvent<HTMLTextAreaElement>,
    index?: number,
    field?: string
  ) {
    const { name, value } = e.target;
    setConfiguration((prev) => {
      if (index !== undefined && field) {
        const examples = [...(prev.examples || [])];
        examples[index] = { ...examples[index], [field]: value };
        return { ...prev, examples };
      } else if (index !== undefined) {
        const ddl_commands = [...(prev.ddl_commands || [])];
        ddl_commands[index] = value;
        return { ...prev, ddl_commands };
      } else {
        return { ...prev, [name]: value };
      }
    });
  }

  return (
    <Dialog className="relative z-50" open={open} onClose={setOpen}>
      {successMessage && <SuccessStatus />}
      <div className="fixed inset-0" />
      <div className="fixed inset-0 overflow-hidden">
        <div className="absolute inset-0 overflow-hidden">
          <div className="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16">
            <DialogPanel className="pointer-events-auto w-screen max-w-md transform transition duration-500 ease-in-out data-[closed]:translate-x-full sm:duration-700">
              <div className="flex h-full flex-col divide-y divide-gray-200 text-Pri-Dark bg-white shadow-xl">
                <div className="h-0 flex-1 overflow-y-scroll no-scrollbar">
                  <div className="px-4 py-6 sm:px-6">
                    <div className="flex items-center justify-between">
                      <DialogTitle className="text-base font-semibold leading-6">
                        {dbType}
                      </DialogTitle>
                      <button
                        type="button"
                        className="relative rounded-md text-Pri-Dark focus:outline-none focus:ring-2"
                        onClick={() => setOpen(false)}
                      >
                        <span className="absolute -inset-2.5" />
                        <span className="sr-only">Close panel</span>
                        <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                      </button>
                    </div>
                    <p className="mt-1 text-sm">
                      Get started by filling in the information below to create
                      your new project.
                    </p>
                  </div>
                  <div className="flex flex-1 flex-col justify-between divide-y divide-gray-200 px-4 sm:px-6">
                    <div className="space-y-6 pb-5 pt-6">
                      {Object.entries(configuration).map(
                        ([key, value], index) => (
                          <div key={index}>
                            <label
                              htmlFor={key}
                              className="block text-sm font-medium leading-6 text-gray-900"
                            >
                              {key
                                .replace(/_/g, ' ')
                                .replace(/\b\w/g, (char) => char.toUpperCase())}
                            </label>
                            {Array.isArray(value) ? (
                              value.map((item, idx) => (
                                <textarea
                                  key={idx}
                                  name={key}
                                  id={`${key}-${idx}`}
                                  value={item}
                                  onChange={(e) => handleChange(e, idx)}
                                  className="block w-full mt-2 rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 resize-none no-scrollbar"
                                  rows={key === 'ddl_commands' ? 4 : 3}
                                  placeholder={
                                    key === 'examples'
                                      ? idx % 2 === 0
                                        ? 'Query'
                                        : 'SQL Query'
                                      : ''
                                  }
                                />
                              ))
                            ) : (
                              <textarea
                                name={key}
                                id={key}
                                value={value}
                                onChange={handleChange}
                                className="block w-full mt-2 rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 no-scrollbar"
                              />
                            )}
                          </div>
                        )
                      )}
                    </div>
                  </div>
                </div>
                <div className="flex flex-shrink-0 justify-end px-4 py-4">
                  <button
                    type="button"
                    className="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                    onClick={() => setOpen(false)}
                  >
                    Cancel
                  </button>
                  <button
                    className="ml-4 inline-flex justify-center rounded-md bg-gray-100 text-Pri-Dark px-3 py-2 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2"
                    onClick={updateConfigurations}
                  >
                    Save
                  </button>
                </div>
              </div>
            </DialogPanel>
          </div>
        </div>
      </div>
    </Dialog>
  );
}
