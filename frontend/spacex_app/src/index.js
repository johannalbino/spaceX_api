import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/styles';
import theme from './theme'

ReactDOM.render(
    <ThemeProvider >
        <BrowserRouter>
            <App theme={theme} />
        </BrowserRouter>
    </ThemeProvider>
    ,
    document.getElementById('root')
);
