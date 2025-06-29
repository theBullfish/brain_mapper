
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>Bear Poking</title>
      </Head>
      <main className="flex h-screen items-center justify-center bg-neutral-900 text-white">
        <h1 className="text-3xl font-bold">🐻 Bear Poking Scaffold Running</h1>
      </main>
    </>
  );
}
