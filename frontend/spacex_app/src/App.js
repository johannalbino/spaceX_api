import React from 'react';
import Header from './components/Header'
import './App.css';
import { Route  } from 'react-router-dom'
import Launches from './components/launches/Launches';
import LatestLaunche from './components/launches/LatestLaunche';

function App() {
  return (
    <React.Fragment>
      <Header />
        <Route path="/lauches" component={Launches} />
        <Route path="/lastest_launche" component={LatestLaunche} />
    </React.Fragment>
  );
}

export default App;
