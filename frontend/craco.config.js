// const { defaults } = require('jest-config');

module.exports = {
  plugins: [{ plugin: require('@semantic-ui-react/craco-less') }],
  jest: {
    configure: {
      globals: {
        CONFIG: true,
      },
      setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
      // "coveragePathIgnorePatterns": [...defaults.coveragePathIgnorePatterns, '<rootDir>/src/index.js'],
      // "snapshotSerializers": ["enzyme-to-json/serializer"],
      verbose: true,
      testEnvironment: 'jsdom',
      moduleNameMapper: {
        'react-i18next': '<rootDir>/src/__mock__/react-i18next.js'
      },
    },
  },
};
