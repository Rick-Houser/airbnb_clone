var React = require('react');

class Footer extends React.Component {
  render() {
    var footerStyle = {
      height: '40px',
      border: '1px solid #f2f2f2',
      textAlign: 'center',
      display: 'flex',
      flexDirection: 'row',
      alignItems: 'center',
      justifyContent: 'center',
      color: '#535353',
      fontFamily: 'sans-serif'
    }
    return(<div style={footerStyle}>&copy; Rick Houser & Steven Garcia 2016</div>)
  }
}

module.exports = Footer;
