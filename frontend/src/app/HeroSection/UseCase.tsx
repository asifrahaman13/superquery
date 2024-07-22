/* eslint-disable @next/next/no-img-element */
import React from 'react';
import { posts } from '@/constants/static/HeroSection/HeroSectionStatic';
import Link from 'next/link';

const UseCase = () => {
  return (
    <React.Fragment>
      <div className="bg-white py-24 sm:py-32">
        <div className="mx-auto max-w-7xl px-6 lg:px-8 flex flex-col gap-20">
          <div className="mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 border-t border-gray-200 pt-10 sm:mt-16 sm:pt-16 lg:mx-0 lg:max-w-none lg:grid-cols-3">
            {posts.map((post) => (
              <article
                key={post.id}
                className="flex max-w-xl flex-col items-start justify-between"
              >
                <div className="flex items-center gap-x-4 text-xs"></div>
                <div className="group relative">
                  <h3 className="mt-3 text-lg font-semibold leading-6 text-gray-900 group-hover:text-gray-600">
                    <a href={post.href}>
                      <span className="absolute inset-0" />
                      {post.title}
                    </a>
                  </h3>
                  <p className="mt-5 line-clamp-3 text-sm leading-6">
                    {post.description}
                  </p>
                </div>
                <div className="relative mt-8 flex items-center gap-x-4">
                  <img
                    src={post.author.imageUrl}
                    alt=""
                    className="h-10 w-10 rounded-full bg-gray-50"
                  />
                  <div className="text-sm leading-6">
                    <p className="font-semibold text-gray-900">
                      <a href={post.author.href}>
                        <span className="absolute inset-0" />
                        {post.author.name}
                      </a>
                    </p>
                    <p className="text-gray-600">{post.author.role}</p>
                  </div>
                </div>
              </article>
            ))}
          </div>
          <div className="  flex flex-col justify-center items-center ">
            <div className="flex flex-col">
              <div className=" text-center font-semibold text-lg  text-Pri-Dark">
                Community
              </div>
              <div className="text-center font-bold text-Pri-Dark text-2xl">
                Join our community
              </div>
              <div className="font-medium">
                Join our open-source community and help to create a pwoerful
                open source project.
              </div>
              <div className="flex justify-center mt-2 gap-6">
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
                <Link
                  className="bg-indigo-700 rounded-md font-semibold text-sm gap-2 text-white py-2 px-4 flex items-center"
                  href="https://discord.gg/bQBqdA6NsU"
                >
                  <svg
                    fill="currentColor"
                    viewBox="0 0 24 24"
                    aria-hidden="true"
                    className="h-5 w-5 fill-white"
                  >
                    <path d="M20.317 4.369a19.791 19.791 0 00-4.885-1.515.074.074 0 00-.079.037c-.213.375-.453.86-.622 1.237a18.925 18.925 0 00-5.676 0 14.74 14.74 0 00-.631-1.237.077.077 0 00-.08-.037c-1.613.285-3.15.828-4.885 1.515a.07.07 0 00-.032.027C.533 9.366-.32 14.243.1 19.065a.081.081 0 00.031.056 19.907 19.907 0 005.992 3.04.079.079 0 00.085-.027c.464-.637.877-1.311 1.234-2.011a.076.076 0 00-.041-.105c-.652-.247-1.27-.552-1.868-.892a.077.077 0 01-.008-.128c.125-.094.251-.192.373-.291a.076.076 0 01.078-.012c3.927 1.807 8.18 1.807 12.061 0a.076.076 0 01.079.011c.122.099.248.198.373.291a.077.077 0 01-.009.128c-.598.34-1.216.645-1.868.892a.076.076 0 00-.04.106c.357.699.77 1.373 1.234 2.01a.078.078 0 00.085.028 19.876 19.876 0 005.993-3.04.077.077 0 00.031-.056c.5-5.177-.838-10.014-3.767-14.669a.061.061 0 00-.032-.028zM8.02 15.331c-1.183 0-2.156-1.092-2.156-2.433 0-1.34.961-2.433 2.156-2.433 1.194 0 2.166 1.092 2.156 2.433 0 1.341-.961 2.433-2.156 2.433zm7.95 0c-1.183 0-2.156-1.092-2.156-2.433 0-1.34.961-2.433 2.156-2.433 1.194 0 2.166 1.092 2.156 2.433 0 1.341-.961 2.433-2.156 2.433z" />
                  </svg>
                  Join discord 🚀
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default UseCase;
