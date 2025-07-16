// packages/db/index.js
require('dotenv').config();               // always load .env

const path = require('path');

// Try the normal location first …
let PrismaClient;
try {
  PrismaClient = require('@prisma/client').PrismaClient;
} catch {
  // … then fall back to where Prisma actually wrote the client
  const fallback = path.join(__dirname, 'prisma/node_modules/@prisma/client');
  PrismaClient = require(fallback).PrismaClient;
}

// One global instance so dev hot-reload doesn’t open 100 connections
const globalForPrisma = global;
const prisma = globalForPrisma.prisma || new PrismaClient({ log: ['error'] });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;

module.exports = { prisma };
