// scripts/test-prisma.js

require('dotenv').config();             // loads /workspaces/brain_mapper/.env
const { PrismaClient } = require('@prisma/client');

async function main() {
  const prisma = new PrismaClient();
  try {
    console.log("DATABASE_URL =", process.env.DATABASE_URL);

    // count your snippets table
    const count = await prisma.snippet.count();
    console.log(`✅ DB connected! You have ${count} snippets.`);
  } catch (err) {
    console.error("❌ Error connecting or querying:", err);
    process.exit(1);
  } finally {
    await prisma.$disconnect();
  }
}

main();
