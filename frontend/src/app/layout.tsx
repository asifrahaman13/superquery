import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import ApolloClientProvider from './apolloProvider';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'SuperQuery',
  description: 'AI powered data query platform',
};


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ApolloClientProvider>{children}</ApolloClientProvider>
      </body>
    </html>
  );
}
