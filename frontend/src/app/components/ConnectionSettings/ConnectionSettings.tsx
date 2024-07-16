/* eslint-disable @next/next/no-img-element */
'use client';
import { useEffect, useState } from 'react';
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/react';
import { XMarkIcon } from '@heroicons/react/24/outline';
import { configuration_interface } from '@/exports/exports';

interface DbSettings {
  dbType: string;
}

interface Configuration {
  db_type?: string;
  projectName?: string;
  username?: string;
  description?: string;
  connectionString?: string;
  ddlCommands?: string[];
  examples?: { query: string; sqlQuery: string }[];
}

function snakeToTitleCase(snakeCaseStr: string): string {
  const words = snakeCaseStr.split('_');
  const titleCaseStr = words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
  return titleCaseStr;
}

export default function ConnectionSettings({ dbType }: DbSettings) {
  const [open, setOpen] = useState(true);

  const [configuration, setConfiguration] = useState<Configuration>({});

  useEffect(() => {
    async function fetchConfigurations(dbType: string) {
      const token = localStorage.getItem('accessToken') || '';
      const response = await configuration_interface.getConfiguration(
        dbType,
        token
      );
      if (response?.code === 200) {
        console.log(response.data);
        setConfiguration(response.data);
      }
      try {
      } catch (e) {
        throw new Error("Couldn't get configurations");
      }
    }

    fetchConfigurations(dbType);
  }, [dbType]);

  async function updateConfigurations() {
    const token = localStorage.getItem('accessToken') || '';
    setConfiguration((prev) => ({ ...prev, db_type: dbType }));
    const response = await configuration_interface.updateConfiguration(
      token,
      configuration
    );
    if (response?.code === 200) {
      console.log(response.data);
    }
    try {
    } catch (e) {
      throw new Error("Couldn't update configurations");
    }
  }

  function handleConfigurationChange(e: { target: { name: any; value: any } }) {
    const { name, value } = e.target;
    setConfiguration((prev) => ({ ...prev, [name]: value }));
  }

  function handleDDLChange(index: number, value: string) {
    setConfiguration((prev) => {
      const ddlCommands = [...(prev.ddlCommands || [])];
      ddlCommands[index] = value;
      return { ...prev, ddlCommands };
    });
  }

  function handleExampleChange(index: number, field: string, value: string) {
    setConfiguration((prev) => {
      const examples = [...(prev.examples || [])];
      examples[index] = { ...examples[index], [field]: value };
      return { ...prev, examples };
    });
  }

  return (
    <Dialog className="relative z-50" open={open} onClose={setOpen}>
      <div className="fixed inset-0" />

      <div className="fixed inset-0 overflow-hidden">
        <div className="absolute inset-0 overflow-hidden">
          <div className="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16">
            <DialogPanel
              transition
              className="pointer-events-auto w-screen max-w-md transform transition duration-500 ease-in-out data-[closed]:translate-x-full sm:duration-700"
            >
              <div className="flex h-full flex-col divide-y divide-gray-200 text-Pri-Dark bg-white shadow-xl">
                <div className="h-0 flex-1 overflow-y-scroll no-scrollbar">
                  <div className=" px-4 py-6 sm:px-6">
                    <div className="flex items-center justify-between">
                      <DialogTitle className="text-base font-semibold leading-6 ">
                        {dbType}
                      </DialogTitle>
                      <div className="ml-3 flex h-7 items-center">
                        <button
                          type="button"
                          className="relative rounded-md  text-Pri-Dark  focus:outline-none focus:ring-2 "
                          onClick={() => setOpen(false)}
                        >
                          <span className="absolute -inset-2.5" />
                          <span className="sr-only">Close panel</span>
                          <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                        </button>
                      </div>
                    </div>
                    <div className="mt-1">
                      <p className="text-sm ">
                        Get started by filling in the information below to
                        create your new project.
                      </p>
                    </div>
                  </div>
                  <div className="flex flex-1 flex-col justify-between">
                    <div className="divide-y divide-gray-200 px-4 sm:px-6">
                      <div className="space-y-6 pb-5 pt-6">
                        {Object.entries(configuration).map(
                          ([key, value], index) => {
                            if (Array.isArray(value)) {
                              return (
                                <div key={index}>
                                  <label
                                    htmlFor="project-name"
                                    className="block text-sm font-medium leading-6 text-gray-900"
                                  >
                                    {snakeToTitleCase(key)}
                                  </label>
                                  {key === 'ddlCommands' ? (
                                    value.map((item, idx) => (
                                      <div key={idx} className="mt-2">
                                        <textarea
                                          name={`${key}-${idx}`}
                                          id={`${key}-${idx}`}
                                          value={item}
                                          onChange={(e: {
                                            target: { value: string };
                                          }) => {
                                            handleDDLChange(
                                              idx,
                                              e.target.value
                                            );
                                          }}
                                          className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 resize-none no-scrollbar"
                                          rows={4}
                                        />
                                      </div>
                                    ))
                                  ) : key === 'examples' ? (
                                    <div className="flex flex-col gap-8">
                                      {value.map((example, idx) => (
                                        <div key={idx} className="mt-2 ">
                                          <div>{idx + 1}</div>
                                          <textarea
                                            name={`examples-query-${idx}`}
                                            id={`examples-query-${idx}`}
                                            value={example.query}
                                            onChange={(e: {
                                              target: { value: string };
                                            }) => {
                                              handleExampleChange(
                                                idx,
                                                'query',
                                                e.target.value
                                              );
                                            }}
                                            className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 resize-none no-scrollbar"
                                            rows={3}
                                            placeholder="Query"
                                          />
                                          <textarea
                                            rows={5}
                                            name={`examples-sqlQuery-${idx}`}
                                            id={`examples-sqlQuery-${idx}`}
                                            value={example.sqlQuery}
                                            onChange={(e: {
                                              target: { value: string };
                                            }) => {
                                              handleExampleChange(
                                                idx,
                                                'sqlQuery',
                                                e.target.value
                                              );
                                            }}
                                            className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 resize-none no-scrollbar"
                                            placeholder="SQL Query"
                                          />
                                        </div>
                                      ))}
                                    </div>
                                  ) : null}
                                </div>
                              );
                            } else {
                              return (
                                <div key={index}>
                                  <label
                                    htmlFor={key}
                                    className="block text-sm font-medium leading-6 text-gray-900"
                                  >
                                    {snakeToTitleCase(key)}
                                  </label>
                                  <div className="mt-2">
                                    <textarea
                                      name={key}
                                      id={key}
                                      value={value}
                                      onChange={(e: {
                                        target: { name: any; value: any };
                                      }) => {
                                        handleConfigurationChange(e);
                                      }}
                                      className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2 no-scrollbar"
                                    />
                                  </div>
                                </div>
                              );
                            }
                          }
                        )}
                      </div>
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
                    className="ml-4 inline-flex justify-center rounded-md bg-indigo-400 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
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
