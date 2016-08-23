import React from 'react';
import ReactDOM from 'react-dom';
import Header from './Components/Header.js';
import LeftColumn from './Components/LeftColumn.js';
import Footer from './Components/Footer.js';

var bodyStyle = {
  height: '100%',
  margin: '0'
}

ReactDOM.render(
  <div style={bodyStyle}>
    <Header />
    <LeftColumn />
    <Footer />
  </div>,
  document.getElementById('root')
);
