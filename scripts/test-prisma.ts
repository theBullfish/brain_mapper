-// scripts/test-prisma.ts
-import { PrismaClient } from "@bear-poking/db";
+// scripts/test-prisma.ts
+// load your root .env, then import the generated Prisma client directly
+import "dotenv/config";
+import { PrismaClient } from "@prisma/client";

async function main() {
  const prisma = new PrismaClient();

  try {
    console.log("DATABASE_URL =", process.env.DATABASE_URL);

    const count = await prisma.snippet.count();
    console.log(`✅ DB connected! You have ${count} snippets.`);
  } catch (e) {
    console.error("❌ Error connecting or querying:", e);
    process.exit(1);
  } finally {
    await prisma.$disconnect();
  }
}

main();
