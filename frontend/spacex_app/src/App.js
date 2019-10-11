import React from 'react';
import Header from './components/Header'
import './App.css';
import { Router, Route  } from 'react-router-dom'
import Launches from './components/launches/Launches';

function App() {
  return (
    <React.Fragment>
      <Header />
        <Route path="/lauches" component={Launches} />
        <Route path="/lastest" component={() =>(<h2>asidhs ROTA 2</h2>)} />
    </React.Fragment>
  );
}

export default App;
