module.exports = {
   collectCoverageFrom: [
      'src/**/*.{js,jsx}',
      //   '**/*.{js,jsx,ts,tsx}',
      //   '!**/*.d.ts',
      //   '!**/node_modules/**',
      //   '!**/config/**',
      //   '!**/settings/**',
      //   '!**/__test__/**',
      //   '!**/*.config.{js,jsx,ts,tsx}',
   ],
   coverageThreshold: {
      global: {
         branches: 100,
         functions: 100,
         lines: 100,
         statements: 100,
      },
   },
   coverageDirectory: '__test__/coverage',
   testEnvironment: 'node',
   verbose: true,
   globals: {
      __DEV__: true,
   },
   testMatch: ['**/?(*.)+(spec|test).[jt]s?(x)'],
   // transformIgnorePatterns: ['/node_modules/(?!@)/'],
   rootDir: './',
}
