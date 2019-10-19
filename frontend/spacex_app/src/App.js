import React from 'react';
import Header from './components/Header'
import './App.css';
import { Route, Redirect  } from 'react-router-dom'
import Launches from './components/launches/Launches'
import LatestLaunche from './components/launches/LatestLaunche'
import NextLaunche from './components/launches/NextLaunche'

function App({ match }) {
  return (
    <React.Fragment>
      <Header />
        <Route path="/lauches" component={Launches} />
        <Route path="/lastest_launche" component={LatestLaunche} />
        <Route path="/next_launche" component={NextLaunche} />
        <Redirect from="/" exact to={'/launches' } />
    </React.Fragment>
  );
}

export default App;
