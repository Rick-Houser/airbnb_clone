var React = require('react');

class Header extends React.Component {
  render() {
     var containerStyle = {
       height: '60px',
       width: '100%',
       display: 'flex',
       justifyContent: 'space-between',
       border: '1px solid #f2f2f2'
     }
     var logoStyle = {
       color: 'red',
       fontFamily: 'sans-serif',
       marginLeft: '10%'
     }
     var navStyle = {
       width: '200px',
       backgroundColor: '#F6F6F6'
     }
    return(
      <div style={containerStyle}>
        <div style={logoStyle}>
          <h1>airbnb</h1>
        </div>
        <div style={navStyle}></div>
      </div>
    )
  }
}

module.exports = Header;
