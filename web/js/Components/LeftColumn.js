var React = require('react');

class LeftColumn extends React.Component {
  render() {
    var contentContainer = {
      width: '100%',
      display: 'flex',
      minHeight: 'calc(100vh - 100px)'
    }
    var asideStyle = {
     width: '300px',
     backgroundColor: '#F6F6F6'
    }
    return(
      <div style={contentContainer}>
        <div style={asideStyle}></div>
      </div>
    )
  }
}

module.exports = LeftColumn;
