var webpack = require('webpack'),
    path = require('path');

module.exports = {
    debug: true,
    entry: {
      main: './js/app.js',
    },
    output: {
        path: __dirname,
        filename: './static/bundle.js'
    },
    module: {
        loaders: [
          {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: '/nodes-modules/',
            query: {
              presets: ['es2015', 'react']
            }
          }
        ]
    },
};
