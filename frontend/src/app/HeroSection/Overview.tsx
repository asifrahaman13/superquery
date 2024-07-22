/* eslint-disable @next/next/no-img-element */
import React from 'react';

const Overview = () => {
  return (
    <React.Fragment>
      <section className=" body-font max-w-6xl">
        <div className="container mx-auto flex px-5  md:flex-row flex-col items-center">
          <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 className="text-3xl font-bold tracking-tight text-Pri-Dark 0 sm:text-4xl font-sans ">
              Save your time
              <br className="hidden lg:inline-block" />
            </h1>
            <p className="mb-8 leading-relaxed text-medium text-black">
              {' '}
              Save your precious time in building your stuff rather than trying
              to serach the information. With our amazing tool you can find
              instant asnwers from your knowledgebase.
            </p>
            <div className="flex justify-center">
              <a
                href="#"
                className="rounded-md  px-3.5 py-2.5 text-sm font-semibold  shadow-sm  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 0"
              >
                Get started
              </a>
              <button className="rounded-md  px-3.5 py-2.5 text-sm font-semibold  shadow-sm  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 0">
                Button
              </button>
            </div>
          </div>
          <div className="sm:w-1/2 mb-10 px-4">
            <img
              alt="content"
              className="object-cover object-center h-full w-full rounded-lg sm:rounded-none md:rounded-md lg:rounded-x"
              src="https://uploads-ssl.webflow.com/64b66ad2d48ca7a912ddf3eb/64b66ad2d48ca7a912ddf45d_Group%2011394.png"
            />
          </div>
        </div>
      </section>

      <section className="text-gray-600 body-font max-w-6xl">
        <div className="container mx-auto flex px-5  md:flex-row flex-col items-center">
          <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <img
              alt="content"
              className="object-cover object-center h-full w-full rounded-lg sm:rounded-none md:rounded-md lg:rounded-xl"
              src="https://uploads-ssl.webflow.com/64b66ad2d48ca7a912ddf3eb/64b66ad2d48ca7a912ddf45f_Group%2011383.png"
            />
          </div>
          <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
            <h1 className="text-3xl font-bold tracking-tight text-gray-700 sm:text-4xl font-sans">
              Get more convenience
              <br className="hidden lg:inline-block" />
            </h1>
            <p className="mb-8 leading-relaxed text-medium text-black">
              Make it more convenient to use through our amazing tool. Just
              upload your knowledgebase and you are good to go! 🚀
            </p>
            <div className="flex justify-center">
              <a
                href="#"
                className="rounded-md  px-3.5 py-2.5 text-sm text-black font-semibold  shadow-sm  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 0"
              >
                Get started
              </a>
              <button className="rounded-md text-black px-3.5 py-2.5 text-sm font-semibold  shadow-sm  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 0">
                Button
              </button>
            </div>
          </div>
        </div>
      </section>
    </React.Fragment>
  );
};

export default Overview;
