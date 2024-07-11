/* eslint-disable @next/next/no-img-element */
'use client';
import { useEffect, useState } from 'react';
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/react';
import { XMarkIcon } from '@heroicons/react/24/outline';
import {
  LinkIcon,
  PlusIcon,
  QuestionMarkCircleIcon,
} from '@heroicons/react/20/solid';
import { configuration_interface } from '@/exports/exports';
import { team } from '@/constants/static/staticTexts/staticTexts';

interface DbSettings {
  dbType: string;
}

interface Configuration {
  key?: string;
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
                <div className="h-0 flex-1 overflow-y-auto">
                  <div className=" px-4 py-6 sm:px-6">
                    <div className="flex items-center justify-between">
                      <DialogTitle className="text-base font-semibold leading-6 ">
                        {dbType}
                      </DialogTitle>
                      <div className="ml-3 flex h-7 items-center">
                        <button
                          type="button"
                          className="relative rounded-md  text-Pri-Dark hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
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
                        {Object.values(configuration).map((item, index) => (
                          <div key={index}>
                            <label
                              htmlFor="project-name"
                              className="block text-sm font-medium leading-6 text-gray-900"
                            >
                              {snakeToTitleCase(
                                Object.keys(configuration)[index]
                              )}
                            </label>
                            <div className="mt-2">
                              <input
                                type="text"
                                name={Object.keys(configuration)[index]}
                                id={Object.keys(configuration)[index]}
                                value={item}
                                onChange={(e: {
                                  target: { name: any; value: any };
                                }) => {
                                  handleConfigurationChange(e);
                                }}
                                className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2"
                              />
                            </div>
                          </div>
                        ))}

                        <div>
                          <h3 className="text-sm font-medium leading-6 text-gray-900">
                            Team Members
                          </h3>
                          <div className="mt-2">
                            <div className="flex space-x-2">
                              {team.map((person) => (
                                <a
                                  key={person.email}
                                  href={person.href}
                                  className="relative rounded-full hover:opacity-75"
                                >
                                  <img
                                    className="inline-block h-8 w-8 rounded-full"
                                    src={person.imageUrl}
                                    alt={person.name}
                                  />
                                </a>
                              ))}
                              <button
                                type="button"
                                className="relative inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full border-2 border-dashed border-gray-200 bg-white text-gray-400 hover:border-gray-300 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                              >
                                <span className="absolute -inset-2" />
                                <span className="sr-only">Add team member</span>
                                <PlusIcon
                                  className="h-5 w-5"
                                  aria-hidden="true"
                                />
                              </button>
                            </div>
                          </div>
                        </div>
                        <fieldset>
                          <legend className="text-sm font-medium leading-6 text-gray-900">
                            Privacy
                          </legend>
                          <div className="mt-2 space-y-4">
                            <div className="relative flex items-start">
                              <div className="absolute flex h-6 items-center">
                                <input
                                  id="privacy-public"
                                  name="privacy"
                                  aria-describedby="privacy-public-description"
                                  type="radio"
                                  className="h-4 w-4 border-gray-300 text-indigo-400 focus:ring-indigo-400"
                                  defaultChecked
                                />
                              </div>
                              <div className="pl-7 text-sm leading-6">
                                <label
                                  htmlFor="privacy-public"
                                  className="font-medium text-gray-900"
                                >
                                  Public access
                                </label>
                                <p
                                  id="privacy-public-description"
                                  className="text-gray-500"
                                >
                                  Everyone with the link will see this project.
                                </p>
                              </div>
                            </div>
                            <div>
                              <div className="relative flex items-start">
                                <div className="absolute flex h-6 items-center">
                                  <input
                                    id="privacy-private-to-project"
                                    name="privacy"
                                    aria-describedby="privacy-private-to-project-description"
                                    type="radio"
                                    className="h-4 w-4 border-gray-300 text-indigo-400 focus:ring-indigo-400"
                                  />
                                </div>
                                <div className="pl-7 text-sm leading-6">
                                  <label
                                    htmlFor="privacy-private-to-project"
                                    className="font-medium text-gray-900"
                                  >
                                    Private to project members
                                  </label>
                                  <p
                                    id="privacy-private-to-project-description"
                                    className="text-gray-500"
                                  >
                                    Only members of this project would be able
                                    to access.
                                  </p>
                                </div>
                              </div>
                            </div>
                            <div>
                              <div className="relative flex items-start">
                                <div className="absolute flex h-6 items-center">
                                  <input
                                    id="privacy-private"
                                    name="privacy"
                                    aria-describedby="privacy-private-to-project-description"
                                    type="radio"
                                    className="h-4 w-4 border-gray-300 text-indigo-400 focus:ring-indigo-400"
                                  />
                                </div>
                                <div className="pl-7 text-sm leading-6">
                                  <label
                                    htmlFor="privacy-private"
                                    className="font-medium text-gray-900"
                                  >
                                    Private to you
                                  </label>
                                  <p
                                    id="privacy-private-description"
                                    className="text-gray-500"
                                  >
                                    You are the only one able to access this
                                    project.
                                  </p>
                                </div>
                              </div>
                            </div>
                          </div>
                        </fieldset>
                      </div>

                      <div className="pb-6 pt-4">
                        <div className="flex text-sm">
                          <a
                            href="#"
                            className="group inline-flex items-center font-medium text-indigo-400 hover:text-indigo-900"
                          >
                            <LinkIcon
                              className="h-5 w-5 text-indigo-500 group-hover:text-indigo-900"
                              aria-hidden="true"
                            />
                            <span className="ml-2">Copy link</span>
                          </a>
                        </div>
                        <div className="mt-4 flex text-sm">
                          <a
                            href="#"
                            className="group inline-flex items-center text-gray-500 hover:text-gray-900"
                          >
                            <QuestionMarkCircleIcon
                              className="h-5 w-5 text-gray-400 group-hover:text-gray-500"
                              aria-hidden="true"
                            />
                            <span className="ml-2">
                              Learn more about sharing
                            </span>
                          </a>
                        </div>
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
                    className="ml-4 inline-flex justify-center rounded-md bg-indigo-400 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-400"
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
