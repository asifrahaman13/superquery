/* eslint-disable @next/next/no-img-element */
'use client';
import Overview from './HeroSection/Overview';
import Banner from './HeroSection/Banner';
import UseCase from './HeroSection/UseCase';
import FooterComponent from './HeroSection/FooterComponent';
import HeroSection from './HeroSection/HeroSection';

export default function Home() {
  return (
    <div className="bg-white min-h-screen">
      <HeroSection />

      <div className="relative isolate px-6 pt-14 lg:px-8">
        <div
          className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
          aria-hidden="true"
        >
          <div
            className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
            style={{
              clipPath:
                'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)',
            }}
          />
        </div>

        <div className="mx-auto max-w-4xl py-32 sm:py-48 lg:py-16">
          <div className="text-center flex  flex-col items-center gap-8">
            <h1 className="text-6xl font-bold font-sans">
              Welcome to SuperQuery
            </h1>
            <div className="max-w-2xl bg-Sec-Amber py-3 -rotate-3">
              {' '}
              <h1 className="text-4xl font-bold rotate-3  text-white sm:text-6xl font-sans transform ">
                Analyze your database in seconds
              </h1>
            </div>

            <p className="max-w-xl mt-6 text-medium leading-8 text-gray-600">
              Out main objective is to make you 10x more productive. We are here
              to help you to find the information you need in a within a few
              seconds.
            </p>
            <div className="mt-10 flex items-center justify-center gap-x-6">
              <a
                href="#"
                className="rounded-md bg-green-100 text-green-400 px-3.5 py-2.5 text-sm font-semibold  shadow-sm hover:bg-green-200 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 0"
              >
                Get started
              </a>
              <a
                href="#"
                className="rounded-md  text-black px-3.5 py-2.5 text-sm font-semibold  shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Learn more <span aria-hidden="true">→</span>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div>
        <Banner />
      </div>
      <div className="flex flex-col items-center">
        <Overview />
      </div>
      <div>
        <UseCase />
      </div>
      <div>
        <FooterComponent />
      </div>
    </div>
  );
}
