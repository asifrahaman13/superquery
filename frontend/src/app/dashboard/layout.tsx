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
  TransitionChild,
} from '@headlessui/react';
import { Cog6ToothIcon, XMarkIcon } from '@heroicons/react/24/outline';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

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
  return (
    <>
      <div className="w-screen flex flex-row h-screen bg-gray-100">
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
        <div className="w-[15%] h-screen">
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

        <div className="flex w-[85%] overflow-y-hidden">{children}</div>
      </div>
    </>
  );
}
