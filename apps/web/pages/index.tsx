import Image from 'next/image';

export default function Home() {
  return (
    <>
      <main className="flex h-screen items-center justify-center bg-neutral-900 text-white flex-col">
        <Image
          src="/logo.svg"
          alt="Bear Poking logo"
          width={128}
          height={128}
          priority
        />
        <h1 className="mt-6 text-3xl font-bold">Bear Poking Scaffold Running</h1>
      </main>
    </>
  );
}
