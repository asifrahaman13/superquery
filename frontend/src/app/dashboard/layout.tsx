/* eslint-disable @next/next/no-img-element */
'use client';
import { useEffect, useState } from 'react';
import {
  SiMysql,
  SiPostgresql,
  SiMongodb,
  SiSqlite,
  SiNeo4J,
  SiPinescript,
} from 'react-icons/si';
import { MdOutlineEco } from 'react-icons/md';
import {
  Dialog,
  DialogBackdrop,
  DialogPanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
} from '@headlessui/react';
import {
  Bars3Icon,
  BellIcon,
  ChevronDownIcon,
  Cog6ToothIcon,
  MagnifyingGlassIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import React from 'react';
const userNavigation = [
  { name: 'Your profile', href: '#' },
  { name: 'Sign out', href: 'signout' },
];

const teams = [
  {
    id: 1,
    name: 'Heroicons',
    href: '#',
    initial: 'H',
    current: false,
  },
  {
    id: 2,
    name: 'Tailwind Labs',
    href: '#',
    initial: 'T',
    current: false,
  },
  {
    id: 3,
    name: 'Workcation',
    href: '#',
    initial: 'W',
    current: false,
  },
];

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ');
}

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const [navigation, SetNavigation] = useState([
    {
      name: 'MySQL',
      href: '/dashboard/mysql',
      icon: SiMysql,
      current: true,
    },
    {
      name: 'PostgreSQL',
      href: '/dashboard/postgres',
      icon: SiPostgresql,
      current: false,
    },
    {
      name: 'SQLite',
      href: '/dashboard/sqlite',
      icon: SiSqlite,
      current: false,
    },
    {
      name: 'MongoDB',
      href: '/dashboard/mongodb',
      icon: SiMongodb,
      current: false,
    },
    {
      name: 'Pinecone',
      href: '/dashboard/pinecone',
      icon: SiPinescript,
      current: false,
    },
    {
      name: 'Qdrant',
      href: '/dashboard/qdrant',
      icon: MdOutlineEco,
      current: false,
    },
    {
      name: 'Neo4j',
      href: '/dashboard/neo4j',
      icon: SiNeo4J,
      current: false,
    },
  ]);

  const router = usePathname();
  useEffect(() => {
    const path = router;
    SetNavigation(
      navigation.map((item) => {
        if (item.href === path) {
          return { ...item, current: true };
        } else {
          return { ...item, current: false };
        }
      })
    );
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [router]);

  const signuout = () => {
    localStorage.removeItem('accessToken');
    window.location.href = '/';
  };
  return (
    <React.Fragment>
      <div className="w-screen flex flex-row h-screen overflow-y-hidden bg-gray-100">
        <Dialog
          className="relative z-50 lg:hidden"
          open={sidebarOpen}
          onClose={setSidebarOpen}
        >
          <DialogBackdrop
            transition
            className="fixed inset-0 bg-gray-900/80 transition-opacity duration-300 ease-linear data-[closed]:opacity-0"
          />

          <div className="fixed inset-0 flex">
            <DialogPanel
              transition
              className="relative mr-16 flex w-full max-w-xs flex-1 transform transition duration-300 ease-in-out data-[closed]:-translate-x-full"
            >
              <TransitionChild>
                <div className="absolute left-full top-0 flex w-16 justify-center pt-5 duration-300 ease-in-out data-[closed]:opacity-0">
                  <button
                    type="button"
                    className="-m-2.5 p-2.5"
                    onClick={() => setSidebarOpen(false)}
                  >
                    <span className="sr-only">Close sidebar</span>
                    <XMarkIcon
                      className="h-6 w-6 text-white"
                      aria-hidden="true"
                    />
                  </button>
                </div>
              </TransitionChild>
              {/* Sidebar component, swap this element with another sidebar if you like */}
              <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-white px-6 pb-4">
                <div className="flex h-16 shrink-0 items-center">
                  <img
                    className="h-8 w-auto"
                    src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
                    alt="Your Company"
                  />
                </div>
                <nav className="flex flex-1 flex-col">
                  <ul role="list" className="flex flex-1 flex-col gap-y-7">
                    <li>
                      <ul role="list" className="-mx-2 space-y-1">
                        {navigation.map((item) => (
                          <li key={item.name}>
                            <Link
                              href={item.href}
                              className={classNames(
                                item.current
                                  ? 'bg-gray-50 text-indigo-500'
                                  : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-500',
                                'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'
                              )}
                            >
                              <item.icon
                                className={classNames(
                                  item.current
                                    ? 'text-indigo-500'
                                    : 'text-gray-400 group-hover:text-indigo-500',
                                  'h-6 w-6 shrink-0'
                                )}
                                aria-hidden="true"
                              />
                              {item.name}
                            </Link>
                          </li>
                        ))}
                      </ul>
                    </li>
                    <li>
                      <div className="text-xs font-semibold leading-6 text-gray-400">
                        Your teams
                      </div>
                      <ul role="list" className="-mx-2 mt-2 space-y-1">
                        {teams.map((team) => (
                          <li key={team.name}>
                            <Link
                              href={team.href}
                              className={classNames(
                                team.current
                                  ? 'bg-gray-50 text-indigo-500'
                                  : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-500',
                                'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'
                              )}
                            >
                              <span
                                className={classNames(
                                  team.current
                                    ? 'border-indigo-500 text-indigo-500'
                                    : 'border-gray-200 text-gray-400 group-hover:border-indigo-500 group-hover:text-indigo-500',
                                  'flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border bg-white text-[0.625rem] font-medium'
                                )}
                              >
                                {team.initial}
                              </span>
                              <span className="truncate">{team.name}</span>
                            </Link>
                          </li>
                        ))}
                      </ul>
                    </li>
                    <li className="mt-auto">
                      <Link
                        href="#"
                        className="group -mx-2 flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-500"
                      >
                        <Cog6ToothIcon
                          className="h-6 w-6 shrink-0 text-gray-400 group-hover:text-indigo-500"
                          aria-hidden="true"
                        />
                        Settings
                      </Link>
                    </li>
                  </ul>
                </nav>
              </div>
            </DialogPanel>
          </div>
        </Dialog>

        {/* Static sidebar for desktop */}
        <div className="w-[15%] h-full overflow-y-hidden">
          {/* Sidebar component, swap this element with another sidebar if you like */}

          <div className="flex grow flex-col gap-y-5 h-full overflow-y-auto border-r border-gray-200 bg-white px-6 pb-4">
            <div className="flex h-16 shrink-0 items-center">
              <img
                className="h-8 w-auto"
                src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
                alt="Your Company"
              />
            </div>
            <nav className="flex flex-1 flex-col">
              <ul role="list" className="flex flex-1 flex-col gap-y-7">
                <li>
                  <ul role="list" className="-mx-2 space-y-1">
                    {navigation.map((item) => (
                      <li key={item.name}>
                        <Link
                          href={item.href}
                          className={classNames(
                            item.current
                              ? 'bg-gray-50 text-indigo-500'
                              : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-500',
                            'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'
                          )}
                        >
                          <item.icon
                            className={classNames(
                              item.current
                                ? 'text-indigo-500'
                                : 'text-gray-400 group-hover:text-indigo-500',
                              'h-6 w-6 shrink-0'
                            )}
                            aria-hidden="true"
                          />
                          {item.name}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </li>
                <li>
                  <div className="text-xs font-semibold leading-6 text-gray-400">
                    Your teams
                  </div>
                  <ul role="list" className="-mx-2 mt-2 space-y-1">
                    {teams.map((team) => (
                      <li key={team.name}>
                        <Link
                          href={team.href}
                          className={classNames(
                            team.current
                              ? 'bg-gray-50 text-indigo-500'
                              : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-500',
                            'group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'
                          )}
                        >
                          <span
                            className={classNames(
                              team.current
                                ? 'border-indigo-500 text-indigo-500'
                                : 'border-gray-200 text-gray-400 group-hover:border-indigo-500 group-hover:text-indigo-500',
                              'flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border bg-white text-[0.625rem] font-medium'
                            )}
                          >
                            {team.initial}
                          </span>
                          <span className="truncate">{team.name}</span>
                        </Link>
                      </li>
                    ))}
                  </ul>
                </li>
                <li className="mt-auto">
                  <Link
                    href="#"
                    className="group -mx-2 flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-500"
                  >
                    <Cog6ToothIcon
                      className="h-6 w-6 shrink-0 text-gray-400 group-hover:text-indigo-500"
                      aria-hidden="true"
                    />
                    Settings
                  </Link>
                </li>
              </ul>
            </nav>
          </div>
        </div>

        <div className="w-[85%] overflow-y-hidden">
          <div className="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 bg-white px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
            <button
              type="button"
              onClick={() => setSidebarOpen(true)}
              className="-m-2.5 p-2.5 text-gray-700 lg:hidden"
            >
              <span className="sr-only">Open sidebar</span>
              <Bars3Icon aria-hidden="true" className="h-6 w-6" />
            </button>

            {/* Separator */}
            <div
              aria-hidden="true"
              className="h-6 w-px bg-gray-900/10 lg:hidden"
            />

            <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
              <form className="relative flex flex-1">
                <label htmlFor="search-field" className="sr-only">
                  Search
                </label>
                <MagnifyingGlassIcon
                  aria-hidden="true"
                  className="pointer-events-none absolute inset-y-0 left-0 h-full w-5 text-gray-400"
                />
                <input
                  id="search-field"
                  name="search"
                  type="search"
                  placeholder="Search..."
                  className="block h-full w-full border-0 py-0 pl-8 pr-0 text-gray-900 placeholder:text-gray-400 outline-none sm:text-sm "
                />
              </form>
              <div className="flex items-center gap-x-4 lg:gap-x-6">
                <button
                  type="button"
                  className="-m-2.5 p-2.5 text-gray-400 hover:text-gray-500"
                >
                  <span className="sr-only">View notifications</span>
                  <BellIcon aria-hidden="true" className="h-6 w-6" />
                </button>

                {/* Separator */}
                <div
                  aria-hidden="true"
                  className="hidden lg:block lg:h-6 lg:w-px lg:bg-gray-900/10"
                />

                {/* Profile dropdown */}
                <Menu as="div" className="relative">
                  <MenuButton className="-m-1.5 flex items-center p-1.5">
                    <span className="sr-only">Open user menu</span>
                    <img
                      alt=""
                      src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      className="h-8 w-8 rounded-full bg-gray-50"
                    />
                    <span className="hidden lg:flex lg:items-center">
                      <span
                        aria-hidden="true"
                        className="ml-4 text-sm font-semibold leading-6 text-gray-900"
                      >
                        Tom Cook
                      </span>
                      <ChevronDownIcon
                        aria-hidden="true"
                        className="ml-2 h-5 w-5 text-gray-400"
                      />
                    </span>
                  </MenuButton>
                  <MenuItems
                    transition
                    className="absolute right-0 z-10 mt-2.5 w-32 origin-top-right rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 transition focus:outline-none data-[closed]:scale-95 data-[closed]:transform data-[closed]:opacity-0 data-[enter]:duration-100 data-[leave]:duration-75 data-[enter]:ease-out data-[leave]:ease-in"
                  >
                    {userNavigation.map((item) => (
                      <MenuItem key={item.name}>
                        {item.href === 'signout' ? (
                          <button
                            onClick={() => {
                              signuout();
                            }}
                            className="block px-3 py-1 text-sm leading-6 text-gray-900 data-[focus]:bg-gray-50"
                          >
                            {item.name}
                          </button>
                        ) : (
                          <>
                            <a
                              href={item.href}
                              className="block px-3 py-1 text-sm leading-6 text-gray-900 data-[focus]:bg-gray-50"
                            >
                              {item.name}
                            </a>
                          </>
                        )}
                      </MenuItem>
                    ))}
                  </MenuItems>
                </Menu>
              </div>
            </div>
          </div>
          <div className="flex w-full h-full overflow-y-hidden">{children}</div>
        </div>
      </div>
    </React.Fragment>
  );
}
