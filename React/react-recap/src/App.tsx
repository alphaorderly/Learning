import React from 'react';

const App: React.FC = () => {
  var branch: boolean = true

  if (branch === true) {
    return <p>true</p>
  } else {
    return <p>false</p>
  }
}

export default App;
