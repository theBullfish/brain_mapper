// packages/db/index.js
require('dotenv').config();               // ensure DATABASE_URL loaded everywhere
const { PrismaClient } = require('@prisma/client');

// Use a global singleton in dev to prevent too many connections on hot reload
const globalForPrisma = globalThis;

const prisma =
  globalForPrisma.__prisma || new PrismaClient({ log: ['error'] });

if (process.env.NODE_ENV !== 'production') {
  globalForPrisma.__prisma = prisma;
}

module.exports = { prisma };