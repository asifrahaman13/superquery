/* eslint-disable @next/next/no-img-element */
'use client';
import { useEffect, useState } from 'react';
import { Dialog } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import { Fragment } from 'react';
import { Popover, Transition } from '@headlessui/react';
import { ChevronDownIcon } from '@heroicons/react/20/solid';
import {
  callsToAction,
  navigation,
} from '@/constants/static/HeroSection/HeroSectionStatic';
import Link from 'next/link';
import axios from 'axios';

export default function HeroSection() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isSignedIn, setIsSignedIn] = useState(false);

  useEffect(() => {
    async function isSignedIn() {
      try {
        const access_token = localStorage.getItem('accessToken');
        const response = await axios.post(
          `${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/user`,
          {},
          {
            headers: {
              Authorization: `Bearer ${access_token}`,
            },
          }
        );

        if (response.status === 200) {
          setIsSignedIn(true);
        }
      } catch {
        setIsSignedIn(false);
      }
    }

    isSignedIn();
  }, []);

  return (
    <header className="sticky bg-white backdrop-filter backdrop-blur-xl inset-x-0 top-0 z-50">
      <nav
        className="flex items-center justify-between p-6 lg:px-8"
        aria-label="Global"
      >
        <div className="flex lg:flex-1">
          <a href="#" className="-m-1.5 p-1.5">
            <span className="sr-only">Your Company</span>
            <img
              className="h-8 w-auto"
              src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
              alt=""
            />
          </a>
        </div>
        <div className="flex lg:hidden">
          <button
            type="button"
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            onClick={() => setMobileMenuOpen(true)}
          >
            <span className="sr-only">Open main menu</span>
            <Bars3Icon className="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div className="hidden justify-center items-center lg:flex lg:gap-x-12">
          <div className="inline-flex outline-none items-center gap-x-1 text-sm font-semibold leading-6 text-gray-90">
            <Link href="/">Why SuperQuery?</Link>
          </div>
          <div>
            {' '}
            {navigation.map((item) => (
              <Popover className="relative" key={item.name}>
                <Popover.Button className="inline-flex outline-none items-center gap-x-1 text-sm font-semibold leading-6 text-gray-900">
                  <span>{item.name}</span>
                  <ChevronDownIcon className="h-5 w-5" aria-hidden="true" />
                </Popover.Button>

                <Transition
                  as={Fragment}
                  enter="transition ease-out duration-200"
                  enterFrom="opacity-0 translate-y-1"
                  enterTo="opacity-100 translate-y-0"
                  leave="transition ease-in duration-150"
                  leaveFrom="opacity-100 translate-y-0"
                  leaveTo="opacity-0 translate-y-1"
                >
                  <Popover.Panel className="absolute left-1/2 z-10 mt-5 flex w-screen max-w-max -translate-x-1/2 px-4">
                    <div className="w-screen max-w-4xl flex-auto overflow-hidden rounded-3xl bg-white text-sm leading-6 shadow-lg ring-1 ring-gray-900/5">
                      <div className="grid grid-cols-3 gap-4 p-4">
                        {item?.solutions.map((solution) => (
                          <div
                            key={solution.name}
                            className="group relative flex gap-x-6 rounded-lg p-4 hover:bg-gray-50"
                          >
                            <div className="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                              <solution.icon
                                className="h-6 w-6 text-gray-600 group-hover:text-indigo-600"
                                aria-hidden="true"
                              />
                            </div>
                            <div>
                              <a
                                href={solution.href}
                                className="font-semibold text-gray-900"
                              >
                                {solution.name}
                                <span className="absolute inset-0" />
                              </a>
                              <p className="mt-1 text-gray-600">
                                {solution.description}
                              </p>
                            </div>
                          </div>
                        ))}
                      </div>
                      <div className="grid grid-cols-3 divide-x divide-gray-900/5 bg-gray-50">
                        {callsToAction.map((cta) => (
                          <a
                            key={cta.name}
                            href={cta.href}
                            className="flex items-center justify-center gap-x-2.5 p-3 font-semibold text-gray-900 hover:bg-gray-100"
                          >
                            <cta.icon
                              className="h-5 w-5 flex-none text-gray-400"
                              aria-hidden="true"
                            />
                            {cta.name}
                          </a>
                        ))}
                      </div>
                    </div>
                  </Popover.Panel>
                </Transition>
              </Popover>
            ))}
          </div>

          <div className="inline-flex outline-none items-center gap-x-1 text-sm font-semibold leading-6 text-gray-90">
            <Link href="/about">About</Link>
          </div>
          {isSignedIn === true && (
            <div className="inline-flex outline-none items-center gap-x-1 text-sm font-semibold leading-6 text-gray-90">
              <Link href="/dashboard/mysql">Dashboard</Link>
            </div>
          )}
          <Link
            className="bg-black rounded-md font-semibold text-sm gap-2 text-white py-2 px-4 flex items-center"
            href="https://github.com/asifrahaman13/superquery.git"
          >
            <svg
              fill="currentColor"
              viewBox="0 0 20 20"
              aria-hidden="true"
              className="h-5 w-5 fill-white"
            >
              <path
                d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z"
                clipRule="evenodd"
                fillRule="evenodd"
              />
            </svg>
            Star us on github 🌟
          </Link>
        </div>
        <div className="hidden lg:flex lg:flex-1 lg:justify-end">
          {isSignedIn === true ? (
            <div className="text-lg font-medium">Signed In</div>
          ) : (
            <Link
              href="/auth/signup"
              className="bg-Lime-Green p-2 rounded-md text-green-400"
            >
              Signup{' '}
            </Link>
          )}
        </div>
      </nav>
      <Dialog
        as="div"
        className="lg:hidden"
        open={mobileMenuOpen}
        onClose={setMobileMenuOpen}
      >
        <div className="fixed inset-0 z-50" />
        <Dialog.Panel className="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div className="flex items-center justify-between">
            <a href="#" className="-m-1.5 p-1.5">
              <span className="sr-only">Your Company</span>
              <img
                className="h-8 w-auto"
                src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
                alt=""
              />
            </a>
            <button
              type="button"
              className="-m-2.5 rounded-md p-2.5 text-gray-700"
              onClick={() => setMobileMenuOpen(false)}
            >
              <span className="sr-only">Close menu</span>
              <XMarkIcon className="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div className="mt-6 flow-root">
            <div className="-my-6 divide-y divide-gray-500/10">
              <div className="space-y-2 py-6">
                {navigation.map((item) => (
                  <a
                    key={item.name}
                    href={item.href}
                    className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >
                    {item.name}
                  </a>
                ))}
              </div>
              <div className="py-6">
                <a
                  href="#"
                  className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  Log in
                </a>
              </div>
            </div>
          </div>
        </Dialog.Panel>
      </Dialog>
    </header>
  );
}
