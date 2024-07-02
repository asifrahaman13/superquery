'use client';
import { auth_interface } from '@/app/exports/exports';
import Link from 'next/dist/client/link';
import React from 'react';
import { useRouter } from 'next/navigation';

const Page = () => {
  const router = useRouter();
  const [username, setUsername] = React.useState({
    username: '',
    email: '',
    password: '',
  });

  async function handleSubmit() {
    try {
      const loginResponse = await auth_interface.login(
        username.username,
        username.password
      );
      if (loginResponse?.code === 200) {
        console.log(loginResponse.data);
        localStorage.setItem('accessToken', loginResponse.data.access_token);
        router.push('/dashboard/mysql');
      }
    } catch (error) {
      console.log(error);
    }
  }

  function handleChange(event: any) {
    setUsername({
      ...username,
      [event.target.name]: event.target.value,
    });
    console.log(username);
  }

  return (
    <>
      <section className="bg-Lt-gray">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <a
            href="#"
            className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
          >
            <div className="text-xl  font-semibold text-black">SuperQuery</div>
          </a>
          <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0  ">
            <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 className="text-xl font-bold leading-tight tracking-tight ">
                Login to your account
              </h1>
              <div className="space-y-4 md:space-y-6">
                <div>
                  <label className="block mb-2 text-sm font-medium ">
                    Your username
                  </label>
                  <input
                    type="text"
                    name="username"
                    id="username"
                    value={username.username}
                    className="bg-gray-50 border text-Pri-Dark border-gray-300  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5   dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="username"
                    onChange={(e) => {
                      handleChange(e);
                    }}
                  />
                </div>

                <div>
                  <label className="block mb-2 text-sm font-medium text-gray-900">
                    Password
                  </label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="••••••••"
                    value={username.password}
                    className="bg-gray-50 border text-Pri-Dark border-gray-300  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5   dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    onChange={(e) => {
                      handleChange(e);
                    }}
                  />
                </div>
                <div>
                  <label className="block mb-2 text-sm font-medium">
                    Confirm password
                  </label>
                  <input
                    type="confirm-password"
                    name="confirm-password"
                    id="confirm-password"
                    placeholder="••••••••"
                    className="bg-gray-50 border text-Pri-Dark border-gray-300  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5   dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  />
                </div>
                <div className="flex items-start">
                  <div className="flex items-center h-5">
                    <input
                      id="terms"
                      aria-describedby="terms"
                      type="checkbox"
                      className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                    />
                  </div>
                  <div className="ml-3 text-sm">
                    <label className="font-light">
                      I accept the{' '}
                      <a
                        className="font-medium text-primary-600 hover:underline dark:text-primary-500"
                        href="#"
                      >
                        Terms and Conditions
                      </a>
                    </label>
                  </div>
                </div>
                <button
                  type="submit"
                  className="w-full text-white  bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 bg-Pri-Dark bordertext-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                  onClick={(e) => {
                    handleSubmit();
                  }}
                >
                  Create an account
                </button>
                <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                  Already have an account?{' '}
                  <Link
                    href="/signin"
                    className="font-medium text-primary-600 hover:underline dark:text-primary-500"
                  >
                    Login here
                  </Link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Page;
